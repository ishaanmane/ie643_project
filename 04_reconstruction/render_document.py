"""Stage 4, step 1: deterministic renderer. Per-page Markdown + figure crops -> one document -> PDF.

No model is involved: every sentence and equation is copied from the per-page Markdown
(the labels, or the extractor's predictions), so nothing can be invented here. This is
the baseline any learned "generator" has to beat.

For each unit (a lecture, a week, a notebook):
  1. pages in order, each page's Markdown split into blocks
  2. every [Diagram: ...] line matched to a Surya figure crop by position on the page
     (both are in reading order; unequal counts are allowed); the crop replaces nothing,
     it is placed above the description, which becomes its caption
  3. figure crops cut from the preprocessed page and cleaned (chalkboards inverted to
     dark-on-white, contrast stretched)
  4. equations checked: by LaTeX when xelatex is installed (exact), otherwise by pandoc's
     math parser (approximate); a failing equation is shown verbatim with a warning,
     never altered
  5. pandoc -> PDF (xelatex), or HTML when no LaTeX is installed

Usage (from the repo root):
    python3 04_reconstruction/render_document.py --unit ie643_lec07
    python3 04_reconstruction/render_document.py --unit ie643_lec07 --pages-md preds/lora_clean_val
    python3 04_reconstruction/render_document.py --all
Output: out/documents/<unit>/<unit>.md, .pdf (or .html), figures/, report.json
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import uuid

from PIL import Image, ImageOps, ImageStat
from pdf_audit import audit_pdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "data")
DIAGRAM = re.compile(r"^\s*\*?\[Diagram:(.*)\]\*?\s*$")
DISPLAY_MATH = re.compile(r"\$\$(.+?)\$\$", re.S)
INLINE_MATH = re.compile(r"(?<![\\$])\$(?!\$)([^$\n]+?)(?<!\\)\$(?!\$)")
MIN_EXTRA_FIGURE_AREA = 0.03  # unmatched Surya figures smaller than 3% of the page are skipped
SKIP_COST = 0.35              # alignment: cost of leaving a description or a figure unmatched

UNIT_NAMES = {"ie643": "IE643 Lecture {n}", "mlt": "MLT Week {n}", "ie802": "IE802 Notes", "hlcs": "CS Notes {n}"}


# ---- pages and units ----------------------------------------------------------------

def unit_of(page):
    src, unit, _ = page.split("_")
    return f"{src}_{unit}"


def unit_title(unit):
    src, u = unit.split("_")
    num = re.sub(r"\D", "", u).lstrip("0") or u
    return UNIT_NAMES.get(src, unit).format(n=num)


def all_units(split=None):
    """unit -> its pages in order; with split ("val"/"test"), only that split's pages
    (IE802 is split by page block, so a unit can be partly in a split)."""
    pages = sorted(f[:-3] for f in os.listdir(os.path.join(D, "annotations")) if f.endswith(".md"))
    if split:
        keep = set(json.load(open(os.path.join(D, "splits.json")))["splits"][split])
        pages = [p for p in pages if p in keep]
    units = {}
    for p in pages:
        units.setdefault(unit_of(p), []).append(p)
    return units


# ---- blocks ---------------------------------------------------------------------------

def split_blocks(md):
    """Blank-line separated blocks; a $$...$$ display never gets split."""
    blocks, cur, in_math = [], [], False
    for line in md.strip().splitlines():
        if not line.strip() and not in_math:
            if cur:
                blocks.append("\n".join(cur))
                cur = []
            continue
        cur.append(line)
        if line.count("$$") % 2 == 1:
            in_math = not in_math
    if cur:
        blocks.append("\n".join(cur))
    return blocks


def align(desc_pos, fig_pos):
    """Order-preserving alignment of two position lists (values 0-1). Returns pairs (i, j)."""
    n, m = len(desc_pos), len(fig_pos)
    INF = float("inf")
    cost = [[INF] * (m + 1) for _ in range(n + 1)]
    back = [[None] * (m + 1) for _ in range(n + 1)]
    cost[0][0] = 0.0
    for i in range(n + 1):
        for j in range(m + 1):
            if cost[i][j] == INF:
                continue
            steps = []
            if i < n and j < m:
                steps.append((i + 1, j + 1, abs(desc_pos[i] - fig_pos[j]), "match"))
            if i < n:
                steps.append((i + 1, j, SKIP_COST, "skip_desc"))
            if j < m:
                steps.append((i, j + 1, SKIP_COST, "skip_fig"))
            for a, b, c, kind in steps:
                if cost[i][j] + c < cost[a][b]:
                    cost[a][b], back[a][b] = cost[i][j] + c, (i, j, kind)
    pairs, i, j = [], n, m
    while (i, j) != (0, 0):
        pi, pj, kind = back[i][j]
        if kind == "match":
            pairs.append((pi, pj))
        i, j = pi, pj
    return sorted(pairs)


# ---- figures --------------------------------------------------------------------------

def clean_crop(page_img, bbox, pad=0.01):
    w, h = page_img.size
    x0, y0, x1, y1 = (bbox[0] * w / 1000, bbox[1] * h / 1000, bbox[2] * w / 1000, bbox[3] * h / 1000)
    box = (max(0, int(x0 - pad * w)), max(0, int(y0 - pad * h)),
           min(w, int(x1 + pad * w)), min(h, int(y1 + pad * h)))
    crop = page_img.crop(box)
    gray = ImageOps.grayscale(crop)
    if ImageStat.Stat(gray).mean[0] < 100:
        # chalkboard: grayscale first (inverting a green board in colour gives pink), then
        # invert so strokes are dark on white for print
        return ImageOps.autocontrast(ImageOps.invert(gray), cutoff=1).convert("RGB")
    return ImageOps.autocontrast(crop, cutoff=1)


def merge_split_figures(figs, target):
    """Surya sometimes boxes one drawing as several pieces (e.g. three document icons).
    While there are more figures than `target` (the page's number of descriptions), merge
    the closest pair of figure boxes that sit on the same row or column; stop as soon as
    the counts match, so drawings that each have a description are never glued together."""
    def gap(a, b):
        ax0, ay0, ax1, ay1 = a["bbox"]
        bx0, by0, bx1, by1 = b["bbox"]
        v_overlap = max(0, min(ay1, by1) - max(ay0, by0)) / max(1, min(ay1 - ay0, by1 - by0))
        h_overlap = max(0, min(ax1, bx1) - max(ax0, bx0)) / max(1, min(ax1 - ax0, bx1 - bx0))
        h_gap = max(0, max(ax0, bx0) - min(ax1, bx1))
        v_gap = max(0, max(ay0, by0) - min(ay1, by1))
        if v_overlap > 0.5 and h_gap < 200:
            return h_gap
        if h_overlap > 0.5 and v_gap < 100:
            return v_gap
        return None

    def union(a, b):
        bbox = [min(a["bbox"][0], b["bbox"][0]), min(a["bbox"][1], b["bbox"][1]),
                max(a["bbox"][2], b["bbox"][2]), max(a["bbox"][3], b["bbox"][3])]
        return {"block": a["block"] + "+" + b["block"], "bbox": bbox, "pos": (a["pos"] + b["pos"]) / 2,
                "area": (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / 1e6}

    figs = list(figs)
    while len(figs) > target:
        best = None
        for i in range(len(figs)):
            for j in range(i + 1, len(figs)):
                g = gap(figs[i], figs[j])
                if g is not None and (best is None or g < best[0]):
                    best = (g, i, j)
        if best is None:
            break
        _, i, j = best
        merged = union(figs[i], figs[j])
        figs = [f for k, f in enumerate(figs) if k not in (i, j)] + [merged]
        figs.sort(key=lambda f: f["pos"])
    return figs


def page_figures(page, data_dir=None):
    """Surya figure blocks of a page, with their position (0-1) in reading order."""
    path = os.path.join(data_dir or D, "tags", page + ".json")
    if not os.path.exists(path):
        return [], 0
    tags = json.load(open(path))
    blocks = sorted(tags["blocks"], key=lambda b: b["order"])
    n = max(len(blocks) - 1, 1)
    figs = [{"block": b["id"], "bbox": b["bbox"], "pos": k / n,
             "area": (b["bbox"][2] - b["bbox"][0]) * (b["bbox"][3] - b["bbox"][1]) / 1e6}
            for k, b in enumerate(blocks) if b["type"] == "figure"]
    return figs, tags["image_size"]


# ---- equations ------------------------------------------------------------------------

def find_math(md):
    return [m.group(1) for m in DISPLAY_MATH.finditer(md)] + \
           [m.group(1) for m in INLINE_MATH.finditer(DISPLAY_MATH.sub(" ", md))]


class MathCheckError(RuntimeError):
    """The checker could not finish; this is not evidence of valid equations."""


def check_latex(snippets, engine, max_rounds=None):
    """Remove one diagnosed bad snippet at a time, then compile the remainder.

    Halt at the first TeX error so later errors cannot be mistaken for independent
    failures. Infrastructure errors and an exhausted retry budget remain explicit.
    """
    bad, remaining = set(), list(snippets)
    head = [r"\documentclass{article}", r"\usepackage{amsmath,amssymb,mathtools,cancel}",
            r"\usepackage{unicode-math}", r"\begin{document}"]
    rounds = len(remaining) + 1 if max_rounds is None else max_rounds
    for _ in range(rounds):
        if not remaining:
            return bad
        lines = head + [r"\[" + s.replace("\n", " ") + r"\]" for s in remaining] + [r"\end{document}"]
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "m.tex"), "w") as f:
                f.write("\n".join(lines))
            cmd = ([engine, "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "m.tex"]
                   if engine == "xelatex" else [engine, "m.tex"])
            r = subprocess.run(cmd, cwd=tmp, capture_output=True, text=True, timeout=300)
            log = r.stderr + "\n" + r.stdout
            log_path = os.path.join(tmp, "m.log")
            if os.path.exists(log_path):
                with open(log_path, errors="replace") as f:
                    log += "\n" + f.read()
        if r.returncode == 0:
            return bad
        if engine == "tectonic":
            # Warnings (including overfull boxes) can precede the actual error.
            # They must not cause a valid, wide equation to be neutralised.
            m = re.search(r"^error:.*?m\.tex:(\d+):", log, re.M)
        else:
            m = re.search(r"m\.tex:(\d+):", log) or re.search(r"^l\.(\d+)", log, re.M)
        k = int(m.group(1)) - len(head) - 1 if m else -1
        if not 0 <= k < len(remaining):
            raise MathCheckError(f"{engine} failed outside a mapped equation: {log[-1200:]}")
        bad.add(remaining.pop(k))
    raise MathCheckError(f"{engine}: equation check exceeded {rounds} attempts")


def bad_math_latex(snippets):
    return check_latex(snippets, "xelatex")


def bad_math_tectonic(snippets, max_rounds=None):
    return check_latex(snippets, "tectonic", max_rounds)


def bad_math_pandoc(snippets, pandoc):
    """Approximate syntax check; does not establish LaTeX compilation success."""
    bad = set()
    for s in snippets:
        r = subprocess.run([pandoc, "-f", "markdown", "-t", "html", "--mathml"],
                           input=f"$${s}$$", capture_output=True, text=True, timeout=60)
        if r.returncode:
            raise MathCheckError(f"pandoc checker failed: {r.stderr[-1200:]}")
        if "Could not convert TeX math" in r.stderr:
            bad.add(s)
    return bad


def equation_check(snippets):
    pandoc = shutil.which("pandoc")
    if shutil.which("xelatex"):
        how, checker = "xelatex", bad_math_latex
    elif shutil.which("tectonic"):
        how, checker = "tectonic", bad_math_tectonic
    elif pandoc:
        how, checker = "pandoc math parser (approximate)", lambda xs: bad_math_pandoc(xs, pandoc)
    else:
        return set(), {"status": "unchecked", "checked_with": "none", "error": "no equation checker installed"}
    try:
        bad = checker(snippets)
    except (MathCheckError, OSError, subprocess.TimeoutExpired) as e:
        return set(), {"status": "error", "checked_with": how, "error": str(e)}
    return bad, {"status": "completed", "checked_with": how, "error": None}


FONT_DIR = os.path.join(ROOT, "04_reconstruction", "fonts")


def pdf_style_header(out):
    """LaTeX header for the PDF look: style.tex plus the fonts available on this machine.
    Merriweather (bundled in 04_reconstruction/fonts/ or installed) for text; characters it
    lacks (arrows, circled numbers, check marks, Greek) come from DejaVu Serif."""
    installed = subprocess.run(["fc-list"], capture_output=True, text=True).stdout if shutil.which("fc-list") else ""
    lines = []
    if os.path.exists(os.path.join(FONT_DIR, "Merriweather-Regular.ttf")):
        lines.append("\\setmainfont{Merriweather}[Path=" + FONT_DIR + "/, UprightFont=*-Regular, "
                     "BoldFont=*-Bold, ItalicFont=*-Italic, BoldItalicFont=*-BoldItalic, Extension=.ttf]")
    elif "Merriweather" in installed:
        lines.append("\\setmainfont{Merriweather}")
    elif "DejaVu Serif" in installed:
        lines.append("\\setmainfont{DejaVu Serif}")
    lines.append("\\input{" + os.path.join(ROOT, "04_reconstruction", "style.tex") + "}")
    if "DejaVu Serif" in installed and len(lines) > 1 and "DejaVu" not in lines[0]:
        lines.append("\\newfontfamily\\symbolfont{DejaVu Serif}")
        lines.append("\\input{" + os.path.join(ROOT, "04_reconstruction", "fallback_chars.tex") + "}")
    path = os.path.join(out, "style_header.tex")
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    return path


def figure_width_percent(size):
    # Explicit letter paper and 2.2 cm margins below. Specify only width so Pandoc
    # preserves aspect ratio, while also fitting tall drawings within 30% height.
    text_width, text_height = 8.5 - 4.4 / 2.54, 11 - 4.4 / 2.54
    return min(55.0, 30.0 * text_height / text_width * size[0] / size[1])


def missing_source_blocks(sources, doc):
    """Ordered, occurrence-aware Markdown text check, before math fallback.

    This checks intermediate text retention, not final PDF fidelity or OCR accuracy.
    """
    flat = re.sub(r"\s+", " ", doc)
    cursor, missing = 0, []
    for block in sources:
        if block.lstrip().startswith("#"):
            keys = [block.lstrip().lstrip("#").strip()]
        elif DIAGRAM.match(block):
            key = DIAGRAM.match(block).group(1).strip()
            keys = [key, key.replace("[", "\\[").replace("]", "\\]")]
        else:
            keys = [block]
        found = []
        for key in keys:
            key = re.sub(r"\s+", " ", key).strip()
            pos = flat.find(key, cursor)
            if pos >= 0:
                found.append((pos, len(key)))
        if found:
            pos, length = min(found)
            cursor = pos + length
        else:
            missing.append(block[:80])
    return missing


def neutralise(md, bad):
    """Show failing equations verbatim (never edit them) with a visible marker."""
    def disp(m):
        if m.group(1) in bad:
            return ("\n```latex\n" + m.group(1).strip() + "\n```\n\n"
                    "*Warning: equation could not be typeset; shown as written.*\n")
        return m.group(0)

    def inl(m):
        return f"`{m.group(1)}` (not typeset)" if m.group(1) in bad else m.group(0)
    md = DISPLAY_MATH.sub(disp, md)
    return INLINE_MATH.sub(inl, md)


# ---- document -------------------------------------------------------------------------

def heading_text(block):
    return re.sub(r"\s+", " ", block.lstrip().lstrip("#").strip().strip("*")).lower()


def render_unit(unit, pages, md_dir, out_root, fmt, outline=None, run_id=None, reviewed_fixes=None, data_dir=None, document_title=None, source_pages=None, secure_input=False):
    """outline: {"sections": [{"start": "p4.3", "title": ..., "level": 1|2}]} from outline.py, or None."""
    data_dir = data_dir or D
    reviewed_fixes = reviewed_fixes or {}
    starts = {sec["start"]: sec for sec in (outline or {}).get("sections", [])}
    out = os.path.join(out_root, unit)
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(os.path.join(out, "figures"))
    report = {"unit": unit, "run_id": run_id, "pages": [], "missing_pages": [],
              "expected_pages": len(pages), "input_directory": os.path.abspath(md_dir),
              "outline_sections": len(starts), "requested_format": fmt,
              "outline": f"{len(starts)} sections" if starts else "none (page order)"}
    report["reviewed_figure_links"] = []
    applied_sections = set()
    sources = []  # every source block, to verify nothing is lost
    font = ""  # chosen in pdf_style_header() at PDF build time
    # figures stay where they are in the notes (no LaTeX floating); long verbatim lines wrap
    pin = ("header-includes:\n  - \\usepackage{float}\n  - \\floatplacement{figure}{H}\n"
           "  - \\usepackage{fvextra}\n"
           "  - \\DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,breakanywhere,commandchars=\\\\\\{\\}}\n")
    pin += "  - \\usepackage{cancel}\n"
    parts = [f"---\ntitle: {json.dumps(document_title or unit_title(unit))}\ngeometry: margin=2.2cm\npapersize: letter\nfontsize: 10pt\n{font}{pin}---\n"]

    for page in pages:
        src = os.path.join(md_dir, page + ".md")
        if not os.path.exists(src):
            report["missing_pages"].append(page)
            continue
        blocks = split_blocks(open(src).read())
        desc_idx = [k for k, b in enumerate(blocks) if DIAGRAM.match(b)]
        nb = max(len(blocks) - 1, 1)
        figs, _ = page_figures(page, data_dir)
        n_split = len(figs)
        if len(figs) > len(desc_idx):
            figs = merge_split_figures(figs, max(1, len(desc_idx)))
        pairs = align([k / nb for k in desc_idx], [f["pos"] for f in figs])
        matched_desc = {desc_idx[i]: figs[j] for i, j in pairs}
        matched_figs = {j for _, j in pairs}
        page_img = Image.open(os.path.join(data_dir, "processed", page + ".jpg")).convert("RGB")

        if figs:
            _, tagged_size = page_figures(page, data_dir)
            if tuple(tagged_size) != page_img.size:
                raise ValueError(f"{page}: Surya image size differs from the processed image")
        for link in reviewed_fixes.get("figures", []):
            if link["page"] != page:
                continue
            candidates = [k for k in desc_idx
                          if DIAGRAM.match(blocks[k]).group(1).strip() == link["description"]]
            if not candidates:
                continue  # the reviewed caption does not occur in this input variant
            if len(candidates) != 1 or candidates[0] in matched_desc:
                raise ValueError(f"{page}: reviewed caption is ambiguous or already matched")
            with open(os.path.join(data_dir, "tags", page + ".json")) as f:
                tags = json.load(f)
            tagged = [b for b in tags["blocks"] if b["id"] == link["surya_block"]]
            if (len(tagged) != 1 or tagged[0]["bbox"] != link["bbox"]
                    or tuple(tags["image_size"]) != page_img.size
                    or tuple(link["image_size"]) != page_img.size):
                raise ValueError(f"{page}: reviewed Surya box or image dimensions have changed")
            if tagged[0]["type"] not in ("figure", "table"):
                raise ValueError(f"{page}: reviewed box is not a figure or table")
            matched_desc[candidates[0]] = {"block": link["surya_block"], "bbox": link["bbox"]}
            report["reviewed_figure_links"].append(link)

        def figure_md(fig, caption):
            name = f"{page}_{fig['block'].replace('+', '-')}.png"
            crop = clean_crop(page_img, fig["bbox"])
            crop.save(os.path.join(out, "figures", name))
            # a captioned image alone in a paragraph becomes a numbered, centred figure;
            # brackets in the caption are escaped so they cannot end the caption early
            cap = caption.replace("[", "\\[").replace("]", "\\]").replace("\n", " ")
            return f"![{cap}]({'figures/' + name}){{width={figure_width_percent(crop.size):.4f}%}}"

        # Page marker for the Markdown file. With secure_input the PDF is built with raw HTML
        # off, so an HTML comment would be printed as text on the page; leave it out there.
        body = [] if secure_input else [f"<!-- page: {page} -->"]
        pnum = int(re.search(r"page(\d+)$", page).group(1))
        for k, b in enumerate(blocks):
            bid = f"p{pnum}.{k}"
            sources.append(b)
            sec = starts.get(bid)
            if sec:
                applied_sections.add(bid)
            if sec and b.lstrip().startswith("#"):
                # the section starts on a heading: print that heading, verbatim, at the section level
                body.append("#" * sec["level"] + " " + b.lstrip().lstrip("#").strip())
                continue
            if sec:
                body.append("#" * sec["level"] + " " + sec["title"])
            if starts and b.lstrip().startswith("#"):
                body.append("### " + b.lstrip().lstrip("#").strip())  # in-page heading under the sections
                continue
            if k in matched_desc:
                body.append(figure_md(matched_desc[k], DIAGRAM.match(b).group(1).strip()))
            elif DIAGRAM.match(b):
                body.append(f"*[Diagram: {DIAGRAM.match(b).group(1).strip()}]*")  # no crop found: keep the text
            else:
                body.append(b)
        extra = [f for j, f in enumerate(figs) if j not in matched_figs and f["area"] >= MIN_EXTRA_FIGURE_AREA]
        for f in extra:
            body.append(figure_md(f, "drawing from the page (no description in the notes)"))
        parts.append("\n\n".join(body))
        report["pages"].append({"page": page, "descriptions": len(desc_idx), "surya_figures": len(figs),
                                "merged_from": n_split, "matched": len(matched_desc), "extra_figures_added": len(extra),
                                "descriptions_without_figure": len(desc_idx) - len(matched_desc)})

    report["outline_sections"] = len(applied_sections)
    report["outline_unapplied_starts"] = sorted(set(starts) - applied_sections)
    report["outline"] = f"{len(applied_sections)} sections" if applied_sections else "none (page order)"
    doc = "\n\n".join(parts) + "\n"
    missing = missing_source_blocks(sources, doc)
    report["preservation"] = {"blocks": len(sources), "missing": len(missing), "missing_list": missing[:10],
                              "scope": "ordered occurrences in Markdown before math fallback; not PDF accuracy"}
    pandoc = shutil.which("pandoc")
    snippets = sorted(set(find_math("\n\n".join(parts[1:]))))
    bad, check = equation_check(snippets)
    repairs = []
    replacements = {fix["original"]: fix for fix in reviewed_fixes.get("math", [])}
    # Apply a reviewed repair only to an actually diagnosed failure and only if
    # the same checker confirms its replacement. Keep every original in the report.
    for original in sorted(bad):
        fix = replacements.get(original)
        if not fix:
            continue
        rejected, repaired_check = equation_check([fix["replacement"]])
        if repaired_check["status"] == "completed" and not rejected:
            repairs.append(fix)
    accepted = {fix["original"]: fix["replacement"] for fix in repairs}
    def replace_math(match):
        original = match.group(1)
        return "$$" + accepted[original] + "$$" if original in accepted else match.group(0)
    # This opt-in manifest currently targets display math only.
    applied = {m.group(1) for m in DISPLAY_MATH.finditer(doc)} & set(accepted)
    doc = DISPLAY_MATH.sub(replace_math, doc)
    remaining_bad = bad - applied
    doc = neutralise(doc, remaining_bad)
    report["math"] = {"equations": len(snippets), "failed": len(bad), "failed_list": sorted(bad)[:20],
                      "reviewed_repairs": [f for f in repairs if f["original"] in applied],
                      "remaining_failed": len(remaining_bad), **check}
    if source_pages:
        # Preserve original scans when fresh layout/crops are unavailable. Explicit
        # appendix, not a claim that diagrams were reconstructed or recognized.
        os.makedirs(os.path.join(out, "sources"), exist_ok=True)
        doc += "\n# Original source pages\n\nOriginal scans for checking transcription and diagrams.\n"
        for number, source in enumerate(source_pages, 1):
            with Image.open(source) as image:
                width, height = image.size
                name = f"source_{number:03d}.jpg"
                # For checking only: 1600 px is legible on screen and keeps the PDF small
                # (full 4000 px pages at quality 95 made a few-page PDF over 5 MB).
                small = image.convert("RGB")
                small.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
                small.save(os.path.join(out, "sources", name), quality=80, optimize=True)
            percent = min(90.0, 80.0 * (11 - 4.4/2.54) / (8.5 - 4.4/2.54) * width / height)
            doc += f"\n![Original source page {number}](sources/{name}){{width={percent:.4f}%}}\n"
        report["source_appendix_pages"] = len(source_pages)
    md_path = os.path.join(out, unit + ".md")
    open(md_path, "w").write(doc)

    report["output"] = None
    if pandoc and fmt in ("pdf", "html"):
        target = os.path.join(out, f"{unit}.{fmt}")
        cmd = [pandoc, md_path, "-o", target, "--resource-path", out]
        if secure_input:
            cmd += ["--from=markdown-raw_tex-raw_html"]
        engine = "xelatex" if shutil.which("xelatex") else "tectonic"  # tectonic: small LaTeX engine for laptops
        cmd += [f"--pdf-engine={engine}", "--lua-filter", os.path.join(ROOT, "04_reconstruction", "fit_display_math.lua"),
                "--include-in-header", os.path.join(ROOT, "04_reconstruction", "fit_display_math.tex"),
                "--include-in-header", pdf_style_header(out)] if fmt == "pdf" else ["--standalone", "--mathjax"]
        if fmt == "pdf" and engine == "xelatex":
            cmd += ["--pdf-engine-opt=-no-shell-escape"]
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=out, timeout=600)
        report["output"] = target if r.returncode == 0 and os.path.exists(target) else None
        report["pandoc_errors"] = r.stderr[-1500:] if r.returncode else ""
        report["pandoc_warnings"] = r.stderr[-3000:] if not r.returncode else ""
        if report["output"] and fmt == "pdf":
            report["pdf_audit"] = audit_pdf(target)
    json.dump(report, open(os.path.join(out, "report.json"), "w"), indent=1)
    return report


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--unit", action="append", help="e.g. ie643_lec07 (repeatable)")
    p.add_argument("--all", action="store_true")
    p.add_argument("--split", choices=["train", "val", "test"], help="only the pages of this split")
    p.add_argument("--pages-md", default=os.path.join(D, "annotations"),
                   help="folder of per-page Markdown (labels or model predictions)")
    p.add_argument("--out", default=os.path.join(ROOT, "out", "documents"))
    p.add_argument("--outlines", default=None, help="folder of outlines from outline.py (adds sections)")
    p.add_argument("--format", choices=["pdf", "html", "md"], default=None,
                   help="default: pdf if xelatex is installed, else html if pandoc is, else md")
    p.add_argument("--reviewed-fixes", help="opt-in JSON of explicit, audited math and crop fixes")
    a = p.parse_args()
    reviewed_fixes = json.load(open(a.reviewed_fixes)) if a.reviewed_fixes else None
    a.out, a.pages_md = os.path.abspath(a.out), os.path.abspath(a.pages_md)  # pandoc runs inside the output folder
    latex = shutil.which("xelatex") or shutil.which("tectonic")
    fmt = a.format or ("pdf" if latex and shutil.which("pandoc") else "html" if shutil.which("pandoc") else "md")
    units = all_units(a.split)
    chosen = sorted(units) if a.all else (a.unit or [])
    if not chosen:
        sys.exit("give --unit <name> or --all; units: " + ", ".join(sorted(units)))
    unknown = set(chosen) - set(units)
    if unknown:
        sys.exit("unknown units: " + ", ".join(sorted(unknown)))
    os.makedirs(a.out, exist_ok=True)
    run_id = uuid.uuid4().hex
    with open(os.path.join(a.out, "run.json"), "w") as f:
        json.dump({"run_id": run_id, "units": chosen, "pages_md": a.pages_md, "format": fmt}, f, indent=2)
    failed_outputs = []
    for u in chosen:
        outline = None
        if a.outlines and os.path.exists(os.path.join(a.outlines, u + ".json")):
            outline = json.load(open(os.path.join(a.outlines, u + ".json")))["outline"]  # None if rejected
        r = render_unit(u, units[u], a.pages_md, a.out, fmt, outline, run_id, reviewed_fixes)
        if fmt in ("pdf", "html") and not r["output"]:
            failed_outputs.append(u)
        pg = r["pages"]
        print(f"{u:14s} pages {len(pg):3d} (missing {len(r['missing_pages'])}) | figures matched "
              f"{sum(x['matched'] for x in pg)}/{sum(x['descriptions'] for x in pg)} descriptions, "
              f"+{sum(x['extra_figures_added'] for x in pg)} extra | equations {r['math']['equations']}, "
              f"failed {r['math']['failed']}, repaired {len(r['math']['reviewed_repairs'])}, remaining {r['math']['remaining_failed']} ({r['math']['checked_with']}: {r['math']['status']}) | sections: {r['outline']} | "
              f"blocks kept {r['preservation']['blocks'] - r['preservation']['missing']}/{r['preservation']['blocks']} | "
              f"output: {r['output'] or 'md only'}")

    if failed_outputs:
        sys.exit("Requested output failed for: " + ", ".join(failed_outputs) + "; inspect report.json pandoc_errors")


if __name__ == "__main__":
    main()
