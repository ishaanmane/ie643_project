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

from PIL import Image, ImageOps, ImageStat

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


def all_units():
    pages = sorted(f[:-3] for f in os.listdir(os.path.join(D, "annotations")) if f.endswith(".md"))
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


def page_figures(page):
    """Surya figure blocks of a page, with their position (0-1) in reading order."""
    path = os.path.join(D, "tags_draft", page + ".json")
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


def bad_math_latex(snippets):
    """Exact check: typeset every snippet with xelatex; return the ones that fail."""
    if not snippets:
        return set()
    lines = [r"\documentclass{article}", r"\usepackage{amsmath,amssymb,mathtools}",
             r"\usepackage{unicode-math}", r"\begin{document}"]
    first = len(lines) + 1
    for s in snippets:
        lines.append(r"\[" + s.replace("\n", " ") + r"\]")
    lines.append(r"\end{document}")
    with tempfile.TemporaryDirectory() as tmp:
        open(os.path.join(tmp, "m.tex"), "w").write("\n".join(lines))
        subprocess.run(["xelatex", "-interaction=nonstopmode", "m.tex"],
                       cwd=tmp, capture_output=True, text=True, timeout=300)
        log = open(os.path.join(tmp, "m.log"), errors="ignore").read() if os.path.exists(os.path.join(tmp, "m.log")) else ""
    bad = set()
    for ln in re.findall(r"^l\.(\d+)", log, flags=re.M):
        k = int(ln) - first
        if 0 <= k < len(snippets):
            bad.add(snippets[k])
    return bad


def bad_math_tectonic(snippets, max_rounds=40):
    """Exact check with Tectonic, which stops at the first error: find the failing line,
    set that equation aside, retry until the rest compiles."""
    if not snippets:
        return set()
    bad, remaining = set(), list(snippets)
    head = [r"\documentclass{article}", r"\usepackage{amsmath,amssymb,mathtools}",
            r"\usepackage{unicode-math}", r"\begin{document}"]
    for _ in range(max_rounds):
        lines = head + [r"\[" + s.replace("\n", " ") + r"\]" for s in remaining] + [r"\end{document}"]
        with tempfile.TemporaryDirectory() as tmp:
            open(os.path.join(tmp, "m.tex"), "w").write("\n".join(lines))
            r = subprocess.run(["tectonic", "m.tex"], cwd=tmp, capture_output=True, text=True, timeout=600)
        if r.returncode == 0:
            return bad
        m = re.search(r"m\.tex:(\d+):", r.stderr + r.stdout)
        k = int(m.group(1)) - len(head) - 1 if m else -1
        if not 0 <= k < len(remaining):
            break  # error outside the equations (e.g. a missing package): give up quietly
        bad.add(remaining.pop(k))
    return bad


def bad_math_pandoc(snippets, pandoc):
    """Approximate check without LaTeX: pandoc's math parser (texmath) must accept it."""
    bad = set()
    for s in snippets:
        r = subprocess.run([pandoc, "-f", "markdown", "-t", "html", "--mathml"],
                           input=f"$${s}$$", capture_output=True, text=True)
        if "Could not convert TeX math" in r.stderr:
            bad.add(s)
    return bad


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

def render_unit(unit, pages, md_dir, out_root, fmt):
    out = os.path.join(out_root, unit)
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(os.path.join(out, "figures"))
    report = {"unit": unit, "pages": [], "missing_pages": []}
    font = ""
    if fmt == "pdf" and shutil.which("fc-list"):
        fonts = subprocess.run(["fc-list"], capture_output=True, text=True).stdout
        if "DejaVu Serif" in fonts:  # covers arrows and symbols used in the notes (⇒, →, ⚠)
            font = "mainfont: DejaVu Serif\n"
    # figures stay where they are in the notes (no LaTeX floating); long verbatim lines wrap
    pin = ("header-includes:\n  - \\usepackage{float}\n  - \\floatplacement{figure}{H}\n"
           "  - \\usepackage{fvextra}\n"
           "  - \\DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,breakanywhere,commandchars=\\\\\\{\\}}\n")
    parts = [f"---\ntitle: \"{unit_title(unit)}\"\ngeometry: margin=2cm\nfontsize: 11pt\n{font}{pin}---\n"]

    for page in pages:
        src = os.path.join(md_dir, page + ".md")
        if not os.path.exists(src):
            report["missing_pages"].append(page)
            continue
        blocks = split_blocks(open(src).read())
        desc_idx = [k for k, b in enumerate(blocks) if DIAGRAM.match(b)]
        nb = max(len(blocks) - 1, 1)
        figs, _ = page_figures(page)
        n_split = len(figs)
        if len(figs) > len(desc_idx):
            figs = merge_split_figures(figs, max(1, len(desc_idx)))
        pairs = align([k / nb for k in desc_idx], [f["pos"] for f in figs])
        matched_desc = {desc_idx[i]: figs[j] for i, j in pairs}
        matched_figs = {j for _, j in pairs}
        page_img = Image.open(os.path.join(D, "processed", page + ".jpg")).convert("RGB")

        def figure_md(fig, caption):
            name = f"{page}_{fig['block'].replace('+', '-')}.png"
            clean_crop(page_img, fig["bbox"]).save(os.path.join(out, "figures", name))
            # a captioned image alone in a paragraph becomes a numbered, centred figure;
            # brackets in the caption are escaped so they cannot end the caption early
            cap = caption.replace("[", "\\[").replace("]", "\\]").replace("\n", " ")
            return f"![{cap}]({'figures/' + name}){{width=55% height=30%}}"

        body = [f"<!-- page: {page} -->"]
        for k, b in enumerate(blocks):
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
                                "merged_from": n_split, "matched": len(pairs), "extra_figures_added": len(extra),
                                "descriptions_without_figure": len(desc_idx) - len(pairs)})

    doc = "\n\n".join(parts) + "\n"
    pandoc = shutil.which("pandoc")
    snippets = sorted(set(find_math(doc)))
    if shutil.which("xelatex"):
        bad, how = bad_math_latex(snippets), "xelatex"
    elif shutil.which("tectonic"):
        bad, how = bad_math_tectonic(snippets), "tectonic"
    elif pandoc:
        bad, how = bad_math_pandoc(snippets, pandoc), "pandoc math parser (approximate)"
    else:
        bad, how = set(), "not checked (no pandoc)"
    doc = neutralise(doc, bad)
    report["math"] = {"equations": len(snippets), "failed": len(bad), "checked_with": how, "failed_list": sorted(bad)[:20]}
    md_path = os.path.join(out, unit + ".md")
    open(md_path, "w").write(doc)

    report["output"] = None
    if pandoc and fmt in ("pdf", "html"):
        target = os.path.join(out, f"{unit}.{fmt}")
        cmd = [pandoc, md_path, "-o", target, "--resource-path", out]
        engine = "xelatex" if shutil.which("xelatex") else "tectonic"  # tectonic: small LaTeX engine for laptops
        cmd += [f"--pdf-engine={engine}"] if fmt == "pdf" else ["--standalone", "--mathjax"]
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=out)
        report["output"] = target if r.returncode == 0 and os.path.exists(target) else None
        report["pandoc_errors"] = r.stderr[-1500:] if r.returncode else ""
    json.dump(report, open(os.path.join(out, "report.json"), "w"), indent=1)
    return report


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--unit", action="append", help="e.g. ie643_lec07 (repeatable)")
    p.add_argument("--all", action="store_true")
    p.add_argument("--pages-md", default=os.path.join(D, "annotations"),
                   help="folder of per-page Markdown (labels or model predictions)")
    p.add_argument("--out", default=os.path.join(ROOT, "out", "documents"))
    p.add_argument("--format", choices=["pdf", "html", "md"], default=None,
                   help="default: pdf if xelatex is installed, else html if pandoc is, else md")
    a = p.parse_args()
    latex = shutil.which("xelatex") or shutil.which("tectonic")
    fmt = a.format or ("pdf" if latex and shutil.which("pandoc") else "html" if shutil.which("pandoc") else "md")
    units = all_units()
    chosen = sorted(units) if a.all else (a.unit or [])
    if not chosen:
        sys.exit("give --unit <name> or --all; units: " + ", ".join(sorted(units)))
    for u in chosen:
        r = render_unit(u, units[u], a.pages_md, a.out, fmt)
        pg = r["pages"]
        print(f"{u:14s} pages {len(pg):3d} (missing {len(r['missing_pages'])}) | figures matched "
              f"{sum(x['matched'] for x in pg)}/{sum(x['descriptions'] for x in pg)} descriptions, "
              f"+{sum(x['extra_figures_added'] for x in pg)} extra | equations {r['math']['equations']}, "
              f"failed {r['math']['failed']} ({r['math']['checked_with']}) | output: {r['output'] or 'md only'}")


if __name__ == "__main__":
    main()
