"""Render every page of every lecture PDF in Class Scribes/ to raw scan images.

This is the documented, reproducible replacement for manually screenshotting
pages: PyMuPDF (fitz) opens each source PDF and rasterizes each page at 4x
zoom (~288 DPI equivalent, since these PDF pages are natively small/low-DPI
screen-export size).

Usage: python3 00_dataset/render_pages.py
"""
import os
import fitz

SOURCE_DIR = "/Users/akshatmac/Desktop/IE643/Class Scribes"
OUTPUT_DIR = "data/raw_scans"
ZOOM = 4.0


def render_all():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    mat = fitz.Matrix(ZOOM, ZOOM)
    total = 0
    for pdf_name in sorted(os.listdir(SOURCE_DIR)):
        if not pdf_name.lower().endswith(".pdf"):
            continue
        # "IE643_Lec02_31Jul.pdf" -> "lec02"
        lec_id = pdf_name.split("_")[1].lower()
        doc = fitz.open(os.path.join(SOURCE_DIR, pdf_name))
        for i in range(doc.page_count):
            out_name = f"ie643_{lec_id}_page{i+1:03d}.jpg"
            out_path = os.path.join(OUTPUT_DIR, out_name)
            if os.path.exists(out_path):
                continue  # already rendered
            pix = doc[i].get_pixmap(matrix=mat)
            pix.save(out_path)
            total += 1
        print(f"{pdf_name}: {doc.page_count} pages")
    print(f"\nRendered {total} new page(s) -> {OUTPUT_DIR}")


if __name__ == "__main__":
    render_all()
