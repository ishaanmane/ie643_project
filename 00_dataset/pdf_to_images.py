"""Turn any input (PDF, a single image, or a folder of either) into page images.

This is the pipeline's entry point for new material. The 00_dataset/render_*.py
scripts do the same job for our three fixed source folders.

Usage (from the repo root):
    python3 00_dataset/pdf_to_images.py notes.pdf --out input_pages/
    python3 00_dataset/pdf_to_images.py photo.jpg --out input_pages/
    python3 00_dataset/pdf_to_images.py scans_folder/ --out input_pages/ --prefix mynotes

Output names: <prefix>_pageNNN.jpg, numbered in order. PDF pages are rendered at
--zoom (default 3.0, about 216 DPI); images are copied as JPEG unchanged.
"""
import argparse
import os

from PIL import Image

IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".webp")


def render_pdf(path, out_dir, prefix, start, zoom):
    import fitz  # PyMuPDF
    doc = fitz.open(path)
    mat = fitz.Matrix(zoom, zoom)
    for i in range(doc.page_count):
        doc[i].get_pixmap(matrix=mat).save(os.path.join(out_dir, f"{prefix}_page{start + i:03d}.jpg"))
    return doc.page_count


def main():
    p = argparse.ArgumentParser()
    p.add_argument("input", help="a .pdf, an image, or a folder of them")
    p.add_argument("--out", required=True)
    p.add_argument("--prefix", default="", help="default: the input's file or folder name")
    p.add_argument("--zoom", type=float, default=3.0)
    a = p.parse_args()

    os.makedirs(a.out, exist_ok=True)
    prefix = a.prefix or os.path.splitext(os.path.basename(a.input.rstrip("/")))[0].lower()
    if os.path.isdir(a.input):
        files = sorted(os.path.join(a.input, f) for f in os.listdir(a.input)
                       if f.lower().endswith((".pdf",) + IMAGE_EXTS))
    else:
        files = [a.input]

    n = 1
    for f in files:
        if f.lower().endswith(".pdf"):
            n += render_pdf(f, a.out, prefix, n, a.zoom)
        elif f.lower().endswith(IMAGE_EXTS):
            Image.open(f).convert("RGB").save(os.path.join(a.out, f"{prefix}_page{n:03d}.jpg"), quality=95)
            n += 1
    print(f"wrote {n - 1} page image(s) to {a.out}")


if __name__ == "__main__":
    main()
