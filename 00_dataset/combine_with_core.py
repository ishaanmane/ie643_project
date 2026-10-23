"""Merge external equation records into our core training set, capped so they can't
outweigh our own 205 pages (see data/EXTERNAL_DATASETS.md, "keep it a minority").

Only run this if the trigger condition is met: our own fine-tuned model is weak on
equations on the test split. Writes data/train_combined.jsonl; never overwrites
data/train.jsonl, so the original core-only file is always still there to fall back to.

Usage:
    python3 00_dataset/combine_with_core.py --external data/external_train.jsonl
    python3 00_dataset/combine_with_core.py --external data/external_train.jsonl --cap 100
"""
import argparse
import json
import random


def load(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def combine(core_path, external_path, out_path, cap, seed):
    core = load(core_path)
    external = load(external_path)

    cap = cap if cap is not None else len(core)
    if len(external) > cap:
        random.Random(seed).shuffle(external)
        external = external[:cap]

    combined = core + external
    random.Random(seed).shuffle(combined)

    with open(out_path, "w") as f:
        for r in combined:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"core: {len(core)}, external used: {len(external)}, combined: {len(combined)} -> {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", default="data/train.jsonl")
    parser.add_argument("--external", required=True)
    parser.add_argument("--out", default="data/train_combined.jsonl")
    parser.add_argument("--cap", type=int, default=None, help="default: len(core), i.e. at most 50/50")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    combine(args.core, args.external, args.out, args.cap, args.seed)
