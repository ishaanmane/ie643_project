"""Render every page of every MLT Notes PDF to data/raw_scans/.

Same idea as render_pages.py, pointed at a second source: "MLT Notes/" (digital
stylus notes, one PDF per week), instead of Class Scribes (chalkboard photos).
Kept as a separate script rather than editing render_pages.py, so the existing
205-page chalkboard set can never be accidentally renamed or regenerated
differently by a change made for this new source.

Usage: python3 scripts/render_mlt_pages.py
"""
import os
import re

import fitz

SOURCE_DIR = "/Users/akshatmac/Desktop/IE643/MLT Notes"
OUTPUT_DIR = "data/raw_scans"
ZOOM = 4.0


def render_all():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    mat = fitz.Matrix(ZOOM, ZOOM)
    total = 0
    for pdf_name in sorted(os.listdir(SOURCE_DIR)):
        if not pdf_name.lower().endswith(".pdf"):
            continue
        # "MLT_Week_1.pdf" -> "week01", "MLT_Week_10.pdf" -> "week10"
        m = re.search(r"Week_(\d+)", pdf_name, re.IGNORECASE)
        if not m:
            print(f"skip {pdf_name}: doesn't match 'MLT_Week_N.pdf'")
            continue
        week_id = f"week{int(m.group(1)):02d}"
        doc = fitz.open(os.path.join(SOURCE_DIR, pdf_name))
        for i in range(doc.page_count):
            out_name = f"mlt_{week_id}_page{i+1:03d}.jpg"
            out_path = os.path.join(OUTPUT_DIR, out_name)
            if os.path.exists(out_path):
                continue  # already rendered
            pix = doc[i].get_pixmap(matrix=mat)
            pix.save(out_path)
            total += 1
        print(f"{pdf_name}: {doc.page_count} pages -> {week_id}")
    print(f"\nRendered {total} new page(s) -> {OUTPUT_DIR}")


if __name__ == "__main__":
    render_all()
