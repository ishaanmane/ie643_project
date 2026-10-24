"""Stage 4, step 2: outline generator. An LLM proposes section structure; it never writes content.

The document's blocks (from the per-page Markdown) get ids like p4.3 (page 4, block 3).
The LLM sees id | type | first words of each block and returns only:
    {"sections": [{"start": "p1.0", "title": "...", "level": 1}, ...]}
Sections are contiguous runs of blocks in reading order, so the renderer can never drop,
duplicate or reorder content: it copies every block verbatim and only inserts headings.

Checks (in code, not trusted to the model):
  - valid JSON with a non-empty "sections" list
  - every start id exists; starts strictly increase in reading order; levels are 1 or 2
  - every content word of a title (4+ letters, not a stop word) occurs in the notes;
    otherwise the title is replaced by the first line of the block it starts at
A failing outline is not used: the document falls back to plain page order.

Usage (from the repo root):
    python3 04_reconstruction/outline.py --unit ie643_lec07 --pages-md preds/lora_clean_val          # LLM (GPU)
    python3 04_reconstruction/outline.py --unit ie643_lec07 --mock                                   # no model
then render with the outline:
    python3 04_reconstruction/render_document.py --unit ie643_lec07 --outlines out/outlines
Output: out/outlines/<unit>.json (validated outline + check report).
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from render_document import DIAGRAM, all_units, split_blocks, unit_title  # noqa: E402

D = os.path.join(ROOT, "data")
STOP = set("""this that with from into over under then than their there these those which where when what
about after before between because while would could should have been being does done also only very more
most such each other some many much part notes note page pages lecture week section introduction overview
summary basics basic using used use""".split())


# ---- blocks ---------------------------------------------------------------------------

def page_number(page):
    return int(re.search(r"page(\d+)$", page).group(1))


def block_type(text):
    t = text.lstrip()
    if t.startswith("#"):
        return "heading"
    if DIAGRAM.match(text):
        return "figure"
    if t.startswith("$$"):
        return "equation"
    if t.startswith("|"):
        return "table"
    if re.match(r"^(\s*[-*]|\s*\d+[.)])\s", t):
        return "list"
    return "text"


def collect_blocks(pages, md_dir):
    """All blocks of a unit in reading order: id, page, type, text."""
    blocks = []
    for page in pages:
        path = os.path.join(md_dir, page + ".md")
        if not os.path.exists(path):
            continue
        for k, text in enumerate(split_blocks(open(path).read())):
            blocks.append({"id": f"p{page_number(page)}.{k}", "page": page, "type": block_type(text), "text": text})
    return blocks


def preview(text, n=90):
    t = re.sub(r"\s+", " ", DIAGRAM.sub(lambda m: "[figure] " + m.group(1), text)).strip()
    return t[:n] + ("…" if len(t) > n else "")


# ---- prompt and model -----------------------------------------------------------------

def build_prompt(unit, blocks):
    listing = "\n".join(f"{b['id']} | {b['type']} | {preview(b['text'])}" for b in blocks)
    return (
        f"These are the blocks of handwritten lecture notes ({unit_title(unit)}), in reading order, "
        "as `id | type | beginning of text`.\n\n" + listing + "\n\n"
        "Organise them into sections. You do NOT write or change any content: you only choose where "
        "each section starts, give it a short title, and a level (1 = main topic, 2 = sub-topic).\n"
        "Rules:\n"
        f"- the first section starts at {blocks[0]['id']}\n"
        "- section starts are block ids, in increasing reading order\n"
        "- titles are 2-8 words and use only words that appear in the blocks (prefer an existing heading)\n"
        "- start a new section where the topic changes, not on every page\n"
        f"- between 2 and {max(3, len(blocks) // 6)} sections\n"
        'Answer with JSON only: {"sections": [{"start": "<id>", "title": "<title>", "level": 1}]}'
    )


_MODEL = {}


def call_llm(prompt, model_id, max_new_tokens=1536):
    """Text-only generation with Qwen2.5-VL (already downloaded for extraction) in 4-bit.
    The model is loaded once and reused for every unit."""
    import torch
    from transformers import AutoProcessor, BitsAndBytesConfig, Qwen2_5_VLForConditionalGeneration
    if model_id not in _MODEL:
        bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
                                 bnb_4bit_compute_dtype=torch.bfloat16)
        _MODEL[model_id] = (Qwen2_5_VLForConditionalGeneration.from_pretrained(
            model_id, quantization_config=bnb, dtype=torch.bfloat16, device_map={"": 0}),
            AutoProcessor.from_pretrained(model_id))
    model, proc = _MODEL[model_id]
    messages = [{"role": "system", "content": [{"type": "text", "text":
                 "You organise lecture notes into sections. You never write, add or change content."}]},
                {"role": "user", "content": [{"type": "text", "text": prompt}]}]
    text = proc.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = proc(text=[text], return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
    return proc.batch_decode(out[:, inputs["input_ids"].shape[1]:], skip_special_tokens=True)[0]


def mock_outline(blocks):
    """No model: a section at every Markdown heading (level from # count). For testing."""
    secs = []
    for b in blocks:
        if b["type"] == "heading":
            level = 1 if b["text"].lstrip().startswith("# ") else 2
            secs.append({"start": b["id"], "title": b["text"].lstrip("# ").strip(), "level": level})
    if not secs or secs[0]["start"] != blocks[0]["id"]:
        secs.insert(0, {"start": blocks[0]["id"], "title": first_line(blocks[0]["text"]), "level": 1})
    return json.dumps({"sections": secs})


# ---- checks ---------------------------------------------------------------------------

def first_line(text, n=60):
    t = re.sub(r"[#*$`\\{}_^]", " ", DIAGRAM.sub(lambda m: m.group(1), text.splitlines()[0]))
    t = re.sub(r"\s+", " ", t).strip()
    return t[:n].rsplit(" ", 1)[0] if len(t) > n else (t or "Notes")


def content_words(s):
    return [w for w in re.findall(r"[a-zA-Z]{4,}", s.lower()) if w not in STOP]


def parse_sections(raw):
    """Accept {"sections": [...]} or a bare [...] list, with or without ```json fences."""
    text = re.sub(r"```(?:json)?", "", raw).strip()
    for pattern in (r"\{.*\}", r"\[.*\]"):
        m = re.search(pattern, text, flags=re.S)
        if not m:
            continue
        try:
            obj = json.loads(m.group(0))
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and isinstance(obj.get("sections"), list):
            return obj["sections"]
        if isinstance(obj, list):
            return obj
    return None


def validate(raw, blocks):
    """Parse and check the model's outline. Returns (outline or None, report)."""
    report = {"ok": False, "problems": [], "titles_replaced": []}
    secs = parse_sections(raw)
    if not isinstance(secs, list) or not secs:
        report["problems"].append("no valid JSON with a 'sections' list")
        return None, report
    order = {b["id"]: i for i, b in enumerate(blocks)}
    vocab = {w[:5] for b in blocks for w in content_words(b["text"])}
    clean, last = [], -1
    for s in secs:
        if not isinstance(s, dict) or s.get("start") not in order:
            report["problems"].append(f"unknown start {s.get('start') if isinstance(s, dict) else s!r}")
            continue
        i = order[s["start"]]
        if i <= last:
            report["problems"].append(f"start {s['start']} is not after the previous section")
            continue
        level = s.get("level") if s.get("level") in (1, 2) else 2
        title = str(s.get("title", "")).strip().lstrip("#").strip()  # models sometimes add '# '
        start_text = blocks[i]["text"]
        if blocks[i]["type"] == "heading":
            # a section that starts on a heading keeps the notes' exact wording
            title = start_text.lstrip().lstrip("#").strip().strip("*").strip().rstrip(":").strip()
        else:
            unknown = [w for w in content_words(title) if w[:5] not in vocab]
            if not title or unknown:
                # no faithful title available: drop this section break rather than invent one
                report["titles_replaced"].append({"start": s["start"], "model_title": title,
                                                  "words_not_in_notes": unknown, "used": "(section dropped)"})
                continue
        if clean and title.lower() == clean[-1]["title"].lower():
            report.setdefault("merged_repeats", []).append(s["start"])  # same title twice in a row
            continue
        clean.append({"start": s["start"], "title": title, "level": level})
        last = i
    if not clean or len(report["problems"]) > len(clean):
        report["problems"].append("no usable sections" if not clean else
                                  "more invalid sections than valid ones: outline rejected")
        return None, report
    report["ok"] = True
    report["sections"] = len(clean)
    report["first_section_at_first_block"] = clean[0]["start"] == blocks[0]["id"]
    return {"sections": clean}, report


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--unit", action="append")
    p.add_argument("--all", action="store_true", help="every unit")
    p.add_argument("--pages-md", default=os.path.join(D, "annotations"))
    p.add_argument("--out", default=os.path.join(ROOT, "out", "outlines"))
    p.add_argument("--model", default="Qwen/Qwen2.5-VL-7B-Instruct")
    p.add_argument("--mock", action="store_true", help="outline from existing headings, no model")
    a = p.parse_args()
    a.out, a.pages_md = os.path.abspath(a.out), os.path.abspath(a.pages_md)
    os.makedirs(a.out, exist_ok=True)
    units = all_units()
    if not (a.all or a.unit):
        sys.exit("give --unit <name> or --all")
    for unit in (sorted(units) if a.all else a.unit):
        blocks = collect_blocks(units[unit], a.pages_md)
        prompt = build_prompt(unit, blocks)
        raw = mock_outline(blocks) if a.mock else call_llm(prompt, a.model)
        outline, report = validate(raw, blocks)
        json.dump({"unit": unit, "outline": outline, "report": report, "raw_model_output": raw,
                   "blocks": len(blocks)}, open(os.path.join(a.out, unit + ".json"), "w"), indent=1)
        status = "OK" if outline else "REJECTED (page order will be used)"
        print(f"{unit}: {len(blocks)} blocks -> {status}; sections {report.get('sections', 0)}, "
              f"titles replaced {len(report['titles_replaced'])}, problems {len(report['problems'])}")
        if outline:
            for s in outline["sections"]:
                print(f"   {'  ' if s['level'] == 2 else ''}{s['start']:7s} {s['title']}")


if __name__ == "__main__":
    main()
