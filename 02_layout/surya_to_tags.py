"""Convert Surya's layout output into our tags format, and crop figures and tables.

Surya writes one results.json for a folder of pages, in its own format and in each
image's pixel size. This turns it into one file per page in the format the rest of
the pipeline uses:

  <tags-out>/<page_id>.json   blocks in reading order, boxes normalised to 0-1000
  <crops-out>/<page_id>_bN.png  one crop per figure / diagram / table block

Output goes to data/tags_draft/ by default, NOT data/tags/: these are unverified
model boxes. A page's file moves to data/tags/ only after a person has checked it.

Usage (from the repo root):
    python3 02_layout/surya_to_tags.py --results surya_out/<folder>/results.json --images data/processed
"""
import argparse
import json
import os

from PIL import Image

# Surya label -> our block type
TYPE_MAP = {
    "Text": "text", "Equation": "equation", "SectionHeader": "heading",
    "ListGroup": "list", "Caption": "caption", "Footnote": "footnote",
    "Table": "table", "Picture": "figure", "Figure": "figure", "Diagram": "figure",
    "ChemicalBlock": "figure", "Code": "code", "Form": "form",
    "PageHeader": "page_header", "PageFooter": "page_footer",
    "TableOfContents": "text", "Bibliography": "text", "BlankPage": "blank",
}
CROP_TYPES = {"figure", "table"}
DROP_FROM_TEXT = {"page_header", "page_footer"}  # page numbers, notebook brand, dates


def convert_page(page_id, page, image_path, crops_out, pad=0.01):
    W, H = page["image_bbox"][2], page["image_bbox"][3]
    image = Image.open(image_path).convert("RGB") if os.path.exists(image_path) else None
    warn = None
    if image is None:
        warn = "image not found; no crops written"
    elif image.size != (int(W), int(H)):
        # Not the image Surya saw (e.g. raw scan instead of processed). Preprocessing
        # crops as well as resizes, so the boxes cannot be mapped onto it.
        warn = f"image is {image.size} but Surya saw {int(W)}x{int(H)}: wrong image, no crops written"
        image = None

    blocks = []
    for i, b in enumerate(sorted(page["bboxes"], key=lambda b: b["position"]), 1):
        x0, y0, x1, y1 = b["bbox"]
        norm = [round(1000 * x0 / W), round(1000 * y0 / H), round(1000 * x1 / W), round(1000 * y1 / H)]
        btype = TYPE_MAP.get(b["label"], b["label"].lower())
        block = {"id": f"b{i}", "type": btype, "surya_label": b["label"], "order": i,
                 "bbox": norm, "skip_in_text": btype in DROP_FROM_TEXT, "text_preview": None}
        if image is not None and btype in CROP_TYPES:
            w, h = image.size
            px = [norm[0] * w / 1000, norm[1] * h / 1000, norm[2] * w / 1000, norm[3] * h / 1000]
            dx, dy = pad * w, pad * h
            box = (max(0, int(px[0] - dx)), max(0, int(px[1] - dy)),
                   min(w, int(px[2] + dx)), min(h, int(px[3] + dy)))
            crop_path = os.path.join(crops_out, f"{page_id}_b{i}.png")
            image.crop(box).save(crop_path)
            block["crop"] = crop_path
        blocks.append(block)

    tags = {"image": image_path, "image_size": [int(W), int(H)], "coords": "normalised 0-1000",
            "source": "surya-ocr-2 zero-shot, NOT verified", "error": page.get("error", False),
            "blocks": blocks}
    return tags, warn


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--results", required=True, help="results.json written by surya_layout")
    p.add_argument("--images", default="data/processed", help="the folder Surya was run on")
    p.add_argument("--tags-out", default="data/tags_draft")
    p.add_argument("--crops-out", default="data/crops")
    a = p.parse_args()

    os.makedirs(a.tags_out, exist_ok=True)
    os.makedirs(a.crops_out, exist_ok=True)
    results = json.load(open(a.results))
    n_blocks = n_crops = 0
    for page_id, pages in sorted(results.items()):
        tags, warn = convert_page(page_id, pages[0], os.path.join(a.images, page_id + ".jpg"), a.crops_out)
        with open(os.path.join(a.tags_out, page_id + ".json"), "w") as fh:
            json.dump(tags, fh, indent=1)
        n_blocks += len(tags["blocks"])
        n_crops += sum("crop" in b for b in tags["blocks"])
        if warn or tags["error"]:
            print(f"  {page_id}: {warn or 'Surya reported an error on this page'}")
    print(f"{len(results)} page(s), {n_blocks} blocks, {n_crops} crops -> {a.tags_out}, {a.crops_out}")


if __name__ == "__main__":
    main()
