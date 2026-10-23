"""
Sauvola adaptive binarization for handwritten pages.

Sauvola (like most binarizers) assumes DARK ink on a LIGHT background.
Pages with a dark background (blackboard, dark-green board, dark-mode ink)
are therefore inverted first. --invert auto decides this per image from the
median gray level.

Modes (pick exactly one):
    python sauvola.py --image data/page.jpg
    python sauvola.py --step 10                    # every 10th image of data/

Tuning (several values => one output per combination, names include the params):
    python sauvola.py --image data/page.jpg --window 31 51 75 --k 0.1 0.2 0.35

Side-by-side original | result images for quick eyeballing:
    python sauvola.py --step 10 --compare
"""

import argparse
import itertools
from pathlib import Path

import numpy as np
from PIL import Image
from skimage.filters import threshold_sauvola

IMAGE_EXTS = {".jpg", ".jpeg", ".png"}


def parse_args():
    p = argparse.ArgumentParser(description="Sauvola binarization")
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--image", help="path of one specific image")
    mode.add_argument("--step", type=int, help="take every Nth image from --data")

    p.add_argument("--data", default="data")
    p.add_argument("--out", default="binarized_sauvola")
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--window", type=int, nargs="+", default=[51],
                   help="odd window size(s) in pixels (default 51)")
    p.add_argument("--k", type=float, nargs="+", default=[0.2],
                   help="Sauvola k value(s); higher = thinner strokes, less noise (default 0.2)")
    p.add_argument("--invert", choices=["auto", "yes", "no"], default="auto",
                   help="flip dark-background images before thresholding (default auto)")
    p.add_argument("--compare", action="store_true",
                   help="also save side-by-side original|result into <out>/compare/")
    p.add_argument("--overwrite", action="store_true")
    return p.parse_args()


def collect_images(args):
    if args.image:
        path = Path(args.image)
        if not path.is_file():
            raise SystemExit(f"Image not found: {path.resolve()}")
        return [path]
    if args.step < 1:
        raise SystemExit("--step must be >= 1")
    data_dir = Path(args.data)
    if not data_dir.is_dir():
        raise SystemExit(f"Data folder not found: {data_dir.resolve()}")
    images = sorted(p for p in data_dir.iterdir() if p.suffix.lower() in IMAGE_EXTS)
    if not images:
        raise SystemExit(f"No images found in {data_dir.resolve()}")
    chosen = images[args.offset :: args.step]
    print(f"Found {len(images)} images; taking every {args.step} (offset {args.offset}) -> {len(chosen)}")
    return chosen


def is_dark_background(gray, mode):
    if mode == "yes":
        return True
    if mode == "no":
        return False
    return float(np.median(gray)) < 128


def sauvola(gray, window, k):
    """gray: uint8 2D array (dark ink on light bg). Returns uint8 0/255 (ink = 0)."""
    thresh = threshold_sauvola(gray, window_size=window, k=k)
    return ((gray > thresh) * 255).astype(np.uint8)


def main():
    args = parse_args()
    windows = [w if w % 2 == 1 else w + 1 for w in args.window]  # must be odd
    combos = list(itertools.product(windows, args.k))
    tag_names = len(combos) > 1

    images = collect_images(args)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    if args.compare:
        (out_dir / "compare").mkdir(exist_ok=True)

    for i, img_path in enumerate(images, start=1):
        orig = Image.open(img_path).convert("L")
        gray = np.asarray(orig)
        inverted = is_dark_background(gray, args.invert)
        work = 255 - gray if inverted else gray

        for window, k in combos:
            name = f"{img_path.stem}_w{window}_k{k}" if tag_names else img_path.stem
            out_path = out_dir / f"{name}.png"
            if out_path.exists() and not args.overwrite:
                print(f"[{i}/{len(images)}] skip (exists): {out_path.name}")
                continue

            result = sauvola(work, window, k)
            Image.fromarray(result).save(out_path)

            if args.compare:
                both = np.concatenate([gray, result], axis=1)
                Image.fromarray(both).save(out_dir / "compare" / f"{name}.png")

            flag = "inverted" if inverted else "as-is"
            print(f"[{i}/{len(images)}] {img_path.name} ({flag}, w={window}, k={k}) -> {out_path}")

    print("Done.")


if __name__ == "__main__":
    main()