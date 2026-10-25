"""Build train/val/test JSONL splits and a manual-verification checklist.

Usage: python3 00_dataset/build_dataset.py [--include-flagged] [--variant boxed]

--variant boxed writes data/boxed/{train,val,test}.jsonl instead: the same pages in the
same splits, but pointing at data/processed_boxed/ (Surya boxes drawn on, made by
02_layout/experiments/draw_boxes.py) and using BOXED_PROMPT. The clean files are not touched.

Pairs every page in data/raw_scans/ with its data/annotations/<stem>.md and writes
data/train.jsonl, data/val.jsonl, data/test.jsonl, data/splits.json, data/VERIFICATION.md.
The JSONL records point at data/processed/<stem>.jpg, so run preprocessing before
training (pages are listed from raw_scans/, which is committed, so this works on a
fresh clone where data/processed/ does not exist yet).

Pages whose annotation contains "[illegible]" (a reading the labeller could not make out)
are left out of every split by default: as a training target they would teach the model
to write it, and in val/test they would count our own uncertainty as model error.
A literal "??" is not a flag: the lecturers write it in their notes, so it is content.
Flagged pages are listed in VERIFICATION.md; once fixed, a rebuild puts them back.
Check the result with: python3 00_dataset/check_dataset.py

The split is by unit (lecture or week), not by random page: consecutive pages from
the same source repeat the same equations and diagrams, so a random split would leak
near-duplicates into val/test and inflate every metric.

Sources, told apart by filename prefix (the unit is the second part):
  ie643_lecNN_pageNNN   chalkboard (Class Scribes), unit = lecture
  mlt_weekNN_pageNNN    digital stylus notes (MLT Notes), unit = week
  ie802_notes_pageNNN   notebook (IE802), one unit "notes"
  hlcs_noteNN_page001   HumynLabs notebooks, unit = note
Units not listed in HELD_OUT go to train.

IE802 is a single notebook, so it cannot be held out by unit. Instead a contiguous block
of its last pages is held out (HELD_OUT_PAGES): pages 41-44 val, 45-56 test. Contiguous
blocks keep page-to-page repetition on one side; check_dataset.py's near-duplicate test
confirms no held-out page copies a train page. Without this, notebook photos (the messiest
input) would never be measured.
"""
import json
import os
import re
import sys

from prompts import BOXED_PROMPT, PAGE_PROMPT, build_record

RAW_DIR = "data/raw_scans"
PROCESSED_DIR = "data/processed"
ANNOTATIONS_DIR = "data/annotations"
DATA_DIR = "data"

# Units (lecture or week) held out from training; every other unit goes to train.
# ie643 test spans two topics (perceptron convergence, softmax/cross-entropy).
# mlt test/val picks are arbitrary weeks, not chosen for topic -- fine, since the
# point of holding out by unit is just to avoid near-duplicate leakage, not topic
# balance.
HELD_OUT = {
    "test": ["lec03", "lec09", "week03", "week09", "note17", "note18", "note19", "note20"],
    "val": ["lec07", "week06", "note16"],
}
HELD_OUT_PAGES = {  # source prefix -> split -> page numbers (for single-unit sources)
    "ie802_notes": {"val": range(41, 45), "test": range(45, 57)},
}
MIN_VAL_SPOT_CHECK = 5


def split_of(stem):
    # unit can be "lec03", "week09" (letters+digits) or a bare word like "notes"
    # (single-unit sources with no natural sub-division, e.g. ie802) -- both match.
    m = re.match(r"([a-z0-9]+_([a-z0-9]+))_page(\d+)$", stem)
    for split, pages in HELD_OUT_PAGES.get(m.group(1), {}).items():
        if int(m.group(3)) in pages:
            return split
    unit = m.group(2)
    for split, units in HELD_OUT.items():
        if unit in units:
            return split
    return "train"


VARIANTS = {  # image folder, output folder, prompt
    "clean": (PROCESSED_DIR, DATA_DIR, PAGE_PROMPT),
    "boxed": ("data/processed_boxed", "data/boxed", BOXED_PROMPT),
}


def checklist_lines(title, stems):
    lines = [f"## {title}", ""]
    for s in stems:
        lines.append(f"- [ ] [{s}](annotations/{s}.md) · [image](raw_scans/{s}.jpg)")
    lines.append("")
    return lines


def build(include_flagged=False, variant="clean"):
    image_dir, out_dir, prompt = VARIANTS[variant]
    stems = sorted(
        os.path.splitext(f)[0]
        for f in os.listdir(RAW_DIR)
        if f.lower().endswith(".jpg") and "_debug" not in f
    )
    if variant == "boxed":
        missing = [s for s in stems if not os.path.exists(f"{image_dir}/{s}.jpg")]
        if missing:
            sys.exit(f"{len(missing)} pages have no boxed image in {image_dir}/ "
                     f"(run 02_layout/experiments/draw_boxes.py first): {missing[:5]}")
        no_tags = [s for s in stems if not os.path.exists(f"data/tags/{s}.json")]
        if no_tags:
            print(f"WARNING: {len(no_tags)} of {len(stems)} pages have no Surya tags, so their "
                  f"'boxed' image has no boxes. Run Surya on all pages first.")
    elif not os.path.isdir(PROCESSED_DIR):
        print(f"note: {PROCESSED_DIR}/ does not exist yet; run preprocessing before training")
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
        if "[illegible]" in text:
            flagged.append(stem)
            if not include_flagged:
                continue
        split = split_of(stem)
        splits[split].append(stem)
        records[split].append(build_record(f"{image_dir}/{stem}.jpg", prompt, text))

    os.makedirs(out_dir, exist_ok=True)
    for split, recs in records.items():
        with open(os.path.join(out_dir, f"{split}.jsonl"), "w") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    if variant != "clean":
        print(f"{variant}: " + ", ".join(f"{k} {len(v)}" for k, v in splits.items()) + f" -> {out_dir}/")
        return

    with open(os.path.join(DATA_DIR, "splits.json"), "w") as f:
        json.dump({"held_out_lectures": HELD_OUT, "held_out_pages": {k: {s: [min(r), max(r)] for s, r in v.items()} for k, v in HELD_OUT_PAGES.items()}, "splits": splits}, f, indent=2)

    out = [
        "# Manual verification checklist",
        "",
        "Regenerate with `python3 00_dataset/build_dataset.py`. The flagged list shrinks as you "
        "resolve the `[illegible]` marks from the annotation files.",
        "",
    ]
    excluded = "" if include_flagged else ", left out of all splits until fixed"
    out += checklist_lines(f"1. Flagged pages (`[illegible]` = unreadable), {len(flagged)} remaining{excluded}",
                           flagged)
    out += checklist_lines(f"2. Test split: verify 100% ({len(splits['test'])} pages)", splits["test"])
    out += checklist_lines(
        f"3. Val split: spot-check at least {MIN_VAL_SPOT_CHECK} of {len(splits['val'])}", splits["val"]
    )
    with open(os.path.join(DATA_DIR, "VERIFICATION.md"), "w") as f:
        f.write("\n".join(out))

    total = sum(len(v) for v in splits.values())
    print(f"total {total}: " + ", ".join(f"{k} {len(v)}" for k, v in splits.items()))
    print(f"flagged for review: {len(flagged)}" + ("" if include_flagged else " (left out of the splits)"))


if __name__ == "__main__":
    build(include_flagged="--include-flagged" in sys.argv,
          variant="boxed" if "--variant" in sys.argv and "boxed" in sys.argv else "clean")
