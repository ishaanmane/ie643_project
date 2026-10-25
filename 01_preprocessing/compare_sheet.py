"""Side-by-side raw | processed images for visual QA.

Usage: python3 01_preprocessing/compare_sheet.py [--out data/processed] [--max 20]
Writes <out>/compare/<stem>.png for each processed page (raw on the left).
"""
import argparse
import os

from PIL import Image

p = argparse.ArgumentParser()
p.add_argument("--raw", default="data/raw_scans")
p.add_argument("--out", default="data/processed")
p.add_argument("--max", type=int, default=20)
p.add_argument("--height", type=int, default=900)
a = p.parse_args()

dst = os.path.join(a.out, "compare")
os.makedirs(dst, exist_ok=True)
files = sorted(f for f in os.listdir(a.out) if f.lower().endswith(".jpg"))[: a.max]
for f in files:
    ims = []
    for path in (os.path.join(a.raw, f), os.path.join(a.out, f)):
        im = Image.open(path).convert("RGB")
        im = im.resize((int(im.width * a.height / im.height), a.height))
        ims.append(im)
    sheet = Image.new("RGB", (ims[0].width + ims[1].width + 10, a.height), "gray")
    sheet.paste(ims[0], (0, 0))
    sheet.paste(ims[1], (ims[0].width + 10, 0))
    sheet.save(os.path.join(dst, f[:-4] + ".png"))
print(f"wrote {len(files)} sheets to {dst}")
