"""Run NotesPreprocessor over the raw scans and write a QA report.

Usage (from the repo root):
    python3 01_preprocessing/batch_preprocess.py                  # all pages, resumable
    python3 01_preprocessing/batch_preprocess.py --force          # redo everything
    python3 01_preprocessing/batch_preprocess.py --sample 12 --out /tmp/pp_test --force
    python3 01_preprocessing/batch_preprocess.py --workers 4      # parallel
    python3 01_preprocessing/batch_preprocess.py --deskew         # opt in to skew correction

Skips images that already have an output (resumable) unless --force is given.
Writes <out>/preprocess_report.csv with what each step did per page.
"""
import argparse
import csv
import os
import sys
from concurrent.futures import ProcessPoolExecutor

import cv2

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from preprocess import NotesPreprocessor

RAW_DIR = "data/raw_scans"
OUT_DIR = "data/processed"
FIELDS = ["file", "in_w", "in_h", "out_w", "out_h", "crop", "page_frac", "skew_deg",
          "skew_gain", "scale", "illum", "brightness", "contrast", "sharpness"]


def _quality(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return {"brightness": round(float(gray.mean()), 1),
            "contrast": round(float(gray.std()), 1),
            "sharpness": round(float(cv2.Laplacian(gray, cv2.CV_64F).var()), 1)}


def _work(args):
    fname, raw_dir, out_dir, deskew = args
    try:
        pre = NotesPreprocessor(deskew=deskew)
        out, info = pre.process_with_info(os.path.join(raw_dir, fname))
        cv2.imwrite(os.path.join(out_dir, fname), out)
        info.update(_quality(out))
        info["file"] = fname
        return info, None
    except Exception as e:  # keep going; report at the end
        return None, (fname, str(e))


def run(raw_dir=RAW_DIR, out_dir=OUT_DIR, force=False, sample=0, workers=1, deskew=False):
    os.makedirs(out_dir, exist_ok=True)
    files = sorted(f for f in os.listdir(raw_dir) if f.lower().endswith((".jpg", ".jpeg", ".png")))
    if sample:
        step = max(1, len(files) // sample)
        files = files[::step][:sample]
    todo = [f for f in files if force or not os.path.exists(os.path.join(out_dir, f))]
    jobs = [(f, raw_dir, out_dir, deskew) for f in todo]

    rows, failed = [], []
    if workers > 1:
        with ProcessPoolExecutor(workers) as ex:
            results = ex.map(_work, jobs)
            for i, (info, err) in enumerate(results, 1):
                (rows.append(info) if info else failed.append(err))
                if i % 25 == 0:
                    print(f"...{i}/{len(jobs)}")
    else:
        for i, job in enumerate(jobs, 1):
            info, err = _work(job)
            (rows.append(info) if info else failed.append(err))
            if i % 25 == 0:
                print(f"...{i}/{len(jobs)}")

    report = os.path.join(out_dir, "preprocess_report.csv")
    new_file = not os.path.exists(report) or force
    with open(report, "w" if new_file else "a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, extrasaction="ignore")
        if new_file:
            w.writeheader()
        w.writerows(rows)

    quad = sum(r["crop"] == "quad" for r in rows)
    print(f"processed {len(rows)} file(s): {quad} page-warped, {len(rows) - quad} brightness-crop; "
          f"{len(failed)} failure(s). Report: {report}")
    for fname, err in failed:
        print(f"  FAILED {fname}: {err}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--raw", default=RAW_DIR)
    p.add_argument("--out", default=OUT_DIR)
    p.add_argument("--force", action="store_true")
    p.add_argument("--sample", type=int, default=0, help="only N evenly spaced pages")
    p.add_argument("--workers", type=int, default=1)
    p.add_argument("--deskew", action="store_true")
    a = p.parse_args()
    run(a.raw, a.out, a.force, a.sample, a.workers, a.deskew)
