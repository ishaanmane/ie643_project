"""Stage 2: Surya v2 layout on every page of data/processed/ (GPU machine).

Starts its own vLLM server for Surya, runs surya_layout on the folder, stops the
server, then converts the result to data/tags/<page>.json and figure/table crops
in data/crops/. Same code path as the upload interface (06_interface/layout.py), so the
batch run and uploads use one version: surya-ocr 0.22.1, vllm 0.32.0.

Boxes are in the pixel space of the processed image Surya saw, so re-run this every
time data/processed/ is regenerated; old tags and crops are moved to a backup first.

Usage (from the repo root, on the GPU machine):
    python3 02_layout/run_layout.py
Output: data/tags/, data/crops/, out/layout_<time>/surya_layout/ (logs, raw results.json)
"""
import argparse
import shutil
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "06_interface"))
from layout import run_layout  # noqa: E402


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data", default=str(ROOT / "data"))
    p.add_argument("--timeout", type=int, default=7200, help="seconds for the Surya client on all pages")
    a = p.parse_args()
    data = Path(a.data).resolve()
    pages = sorted(f.stem for f in (data / "processed").glob("*.jpg"))
    if not pages:
        sys.exit("no images in data/processed/: run 01_preprocessing/batch_preprocess.py first")
    stamp = time.strftime("%Y%m%d_%H%M%S")
    output = ROOT / "out" / f"layout_{stamp}"
    output.mkdir(parents=True)
    backup = ROOT / "out" / f"layout_backup_{stamp}"
    for name in ("tags", "crops"):
        if (data / name).exists():
            backup.mkdir(exist_ok=True)
            shutil.move(str(data / name), str(backup / name))
        (data / name).mkdir()
    # surya_layout reads every file in the folder: keep only the page images there while it runs
    others = [f for f in (data / "processed").iterdir() if f.suffix.lower() != ".jpg"]
    for f in others:
        shutil.move(str(f), str(output / f.name))
    start = time.time()
    try:
        info = run_layout(data, pages, output, lambda msg: print(msg, flush=True), timeout=a.timeout)
    finally:
        for f in others:
            shutil.move(str(output / f.name), str(data / "processed" / f.name))
    shutil.copy2(output / "surya_layout" / "processed" / "results.json", output / "results.json")
    crops = len(list((data / "crops").glob("*.png")))
    print(f"pages {info['pages']}, tags {len(list((data / 'tags').glob('*.json')))}, "
          f"crops {crops}, {time.time() - start:.0f} s; raw results {output / 'results.json'}"
          + (f"; previous tags/crops in {backup}" if backup.exists() else ""))


if __name__ == "__main__":
    main()
