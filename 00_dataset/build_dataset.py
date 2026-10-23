"""Build train/val/test JSONL splits and a manual-verification checklist.

Usage: python3 00_dataset/build_dataset.py

Pairs every image in data/processed/ with its data/annotations/<stem>.md and writes
data/train.jsonl, data/val.jsonl, data/test.jsonl, data/splits.json, data/VERIFICATION.md.

The split is by unit (lecture or week), not by random page: consecutive pages from
the same source repeat the same equations and diagrams, so a random split would leak
near-duplicates into val/test and inflate every metric.

Two sources feed data/processed/ right now, told apart by filename prefix:
  ie643_lecNN_pageNNN.jpg  -- chalkboard photos (Class Scribes)
  mlt_weekNN_pageNNN.jpg   -- digital stylus notes (MLT Notes)
Adding a third source later just means adding its held-out units to HELD_OUT below;
split_of() itself doesn't change.
"""
import json
import os
import re

from prompts import PAGE_PROMPT, build_record

PROCESSED_DIR = "data/processed"
ANNOTATIONS_DIR = "data/annotations"
DATA_DIR = "data"

# Units (lecture or week) held out from training; every other unit goes to train.
# ie643 test spans two topics (perceptron convergence, softmax/cross-entropy).
# mlt test/val picks are arbitrary weeks, not chosen for topic -- fine, since the
# point of holding out by unit is just to avoid near-duplicate leakage, not topic
# balance.
HELD_OUT = {
    "test": ["lec03", "lec09", "week03", "week09"],
    "val": ["lec07", "week06"],
}
MIN_VAL_SPOT_CHECK = 5


def split_of(stem):
    # unit can be "lec03", "week09" (letters+digits) or a bare word like "notes"
    # (single-unit sources with no natural sub-division, e.g. ie802) -- both match.
    unit = re.match(r"[a-z0-9]+_([a-z0-9]+)_page\d+$", stem).group(1)
    for split, units in HELD_OUT.items():
        if unit in units:
            return split
    return "train"


def record(stem, ground_truth):
    return build_record(f"{PROCESSED_DIR}/{stem}.jpg", PAGE_PROMPT, ground_truth)


def checklist_lines(title, stems):
    lines = [f"## {title}", ""]
    for s in stems:
        lines.append(f"- [ ] [{s}](annotations/{s}.md) · [image](raw_scans/{s}.jpg)")
    lines.append("")
    return lines


def build():
    stems = sorted(
        os.path.splitext(f)[0]
        for f in os.listdir(PROCESSED_DIR)
        if f.lower().endswith(".jpg") and "_debug" not in f
    )
    splits = {"train": [], "val": [], "test": []}
    records = {"train": [], "val": [], "test": []}
    flagged = []

    for stem in stems:
        md_path = os.path.join(ANNOTATIONS_DIR, stem + ".md")
        if not os.path.exists(md_path):
            print(f"skip {stem}: no annotation")
            continue
        with open(md_path) as f:
            text = f.read().strip()
        if "??" in text:
            flagged.append(stem)
        split = split_of(stem)
        splits[split].append(stem)
        records[split].append(record(stem, text))

    for split, recs in records.items():
        with open(os.path.join(DATA_DIR, f"{split}.jsonl"), "w") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

    with open(os.path.join(DATA_DIR, "splits.json"), "w") as f:
        json.dump({"held_out_lectures": HELD_OUT, "splits": splits}, f, indent=2)

    out = [
        "# Manual verification checklist",
        "",
        "Regenerate with `python3 00_dataset/build_dataset.py`. The flagged list shrinks as you "
        "remove the `??` marks from the annotation files.",
        "",
    ]
    out += checklist_lines(f"1. Flagged pages (`??` = uncertain reading), {len(flagged)} remaining", flagged)
    out += checklist_lines(f"2. Test split: verify 100% ({len(splits['test'])} pages)", splits["test"])
    out += checklist_lines(
        f"3. Val split: spot-check at least {MIN_VAL_SPOT_CHECK} of {len(splits['val'])}", splits["val"]
    )
    with open(os.path.join(DATA_DIR, "VERIFICATION.md"), "w") as f:
        f.write("\n".join(out))

    total = sum(len(v) for v in splits.values())
    print(f"total {total}: " + ", ".join(f"{k} {len(v)}" for k, v in splits.items()))
    print(f"flagged for review: {len(flagged)}")


if __name__ == "__main__":
    build()
