"""Draw the Surya layout boxes onto the preprocessed pages (the "boxed" variant).

For the clean-vs-boxed comparison: the boxed training set uses these images, the
clean set uses data/processed/ as is. Boxes come from data/tags_draft/ (written by
02_layout/surya_to_tags.py) and are drawn thin, in cyan by default, a colour none of
our inks use (MLT notes use red, green, blue and purple; IE802 has red notes).

Usage (from the repo root):
    python3 02_layout/experiments/draw_boxes.py                       # all pages -> data/processed_boxed/
    python3 02_layout/experiments/draw_boxes.py --labels              # also write the block type above each box

A page with no tags file (Surya not run on it, or Surya failed) is copied without
boxes, and counted in the summary, so the boxed set always has every page.
The same drawing must be applied at inference time if a model is trained on it.
"""
import argparse
import json
import os

from PIL import Image, ImageDraw


def draw(image, blocks, colour, labels):
    d = ImageDraw.Draw(image)
    w, h = image.size
    width = max(2, round(0.0015 * max(w, h)))  # 3 px on a 2000 px page
    for b in blocks:
        if b["type"] == "blank":
            continue
        x0, y0, x1, y1 = (b["bbox"][0] * w / 1000, b["bbox"][1] * h / 1000,
                          b["bbox"][2] * w / 1000, b["bbox"][3] * h / 1000)
        d.rectangle([x0, y0, x1, y1], outline=colour, width=width)
        if labels:
            d.text((x0 + 2, max(0, y0 - 12)), b["type"], fill=colour)
    return image


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--images", default="data/processed")
    p.add_argument("--tags", default="data/tags_draft")
    p.add_argument("--out", default="data/processed_boxed")
    p.add_argument("--colour", default="0,255,255", help="R,G,B")
    p.add_argument("--labels", action="store_true")
    a = p.parse_args()

    colour = tuple(int(c) for c in a.colour.split(","))
    os.makedirs(a.out, exist_ok=True)
    pages = sorted(f[:-4] for f in os.listdir(a.images) if f.endswith(".jpg"))
    boxed, plain, wrong_size = 0, [], []
    for pid in pages:
        image = Image.open(os.path.join(a.images, pid + ".jpg")).convert("RGB")
        tag_path = os.path.join(a.tags, pid + ".json")
        if os.path.exists(tag_path):
            tags = json.load(open(tag_path))
            if list(image.size) != tags["image_size"]:
                wrong_size.append(pid)  # tags made from a different version of this page
                plain.append(pid)
            else:
                image = draw(image, tags["blocks"], colour, a.labels)
                boxed += 1
        else:
            plain.append(pid)
        image.save(os.path.join(a.out, pid + ".jpg"), quality=95)

    print(f"{len(pages)} pages -> {a.out}: {boxed} with boxes, {len(plain)} copied WITHOUT boxes")
    if wrong_size:
        print(f"  {len(wrong_size)} skipped because the image size differs from the tags "
              f"(re-run Surya on the current data/processed): {wrong_size[:5]}")
    if plain and not wrong_size:
        print(f"  no tags for: {plain[:5]}{' ...' if len(plain) > 5 else ''}")


if __name__ == "__main__":
    main()
