"""Run src/preprocess.py's NotesPreprocessor over every raw scan.

Usage: python3 scripts/batch_preprocess.py [--force]
Skips images that already have a processed output (resumable), unless
--force is passed to regenerate everything (e.g. after a preprocessing
algorithm change).
"""
import os
import sys

import cv2

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.preprocess import NotesPreprocessor

RAW_DIR = "data/raw_scans"
OUT_DIR = "data/processed"


def run(force=False):
    os.makedirs(OUT_DIR, exist_ok=True)
    pre = NotesPreprocessor()
    files = sorted(f for f in os.listdir(RAW_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png")))
    done, failed = 0, []
    for i, fname in enumerate(files, 1):
        out_path = os.path.join(OUT_DIR, fname)
        if os.path.exists(out_path) and not force:
            continue
        try:
            out = pre.process(os.path.join(RAW_DIR, fname))
            cv2.imwrite(out_path, out)
            done += 1
        except Exception as e:
            failed.append((fname, str(e)))
        if i % 25 == 0:
            print(f"...{i}/{len(files)}")
    print(f"processed {done} new file(s), {len(failed)} failure(s)")
    for fname, err in failed:
        print(f"  FAILED {fname}: {err}")


if __name__ == "__main__":
    run(force="--force" in sys.argv)
