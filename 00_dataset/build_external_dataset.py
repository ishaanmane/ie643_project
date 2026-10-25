"""Turn a public handwritten-equation dataset into JSONL, using EQUATION_PROMPT.

This is the contingency plan in data/EXTERNAL_DATASETS.md — not run yet, no external
data has been downloaded. Kept separate from build_dataset.py on purpose: external
data must never silently mix into our own 205-page train.jsonl.

Each public dataset (MathWriting, CROHME, HME100K, ...) stores its images and labels
in its own format. Rather than writing one script per dataset, this script expects a
single common input: a directory of images plus a labels.json mapping
{"filename.png": "latex string"}. Write one small converter per dataset (parsing its
InkML files, or its own label format) that produces that labels.json — that converter
is the only dataset-specific code; everything downstream is shared.

Usage:
    python3 00_dataset/build_external_dataset.py \
        --images-dir data/external/mathwriting/images \
        --labels data/external/mathwriting/labels.json \
        --out data/external_train.jsonl
"""
import argparse
import json
import os

from prompts import EQUATION_PROMPT, build_record


def build(images_dir, labels_path, out_path):
    with open(labels_path) as f:
        labels = json.load(f)

    records, missing = [], []
    for filename, latex in labels.items():
        image_path = os.path.join(images_dir, filename)
        if not os.path.exists(image_path):
            missing.append(filename)
            continue
        ground_truth = latex.strip()
        if not ground_truth.startswith("$"):
            ground_truth = f"$${ground_truth}$$"
        records.append(build_record(image_path, EQUATION_PROMPT, ground_truth))

    with open(out_path, "w") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"wrote {len(records)} equation record(s) -> {out_path}")
    if missing:
        print(f"skipped {len(missing)} label(s) with no matching image (first 5): {missing[:5]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--images-dir", required=True)
    parser.add_argument("--labels", required=True, help="JSON file: {filename: latex}")
    parser.add_argument("--out", default="data/external_train.jsonl")
    args = parser.parse_args()
    build(args.images_dir, args.labels, args.out)
