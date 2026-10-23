"""Render every page of the IE802 postmidsem notes PDF to data/raw_scans/.

Fourth source, kept as its own small script for the same reason as the others:
never touch the render logic for an existing source when adding a new one.
No natural weekly/lecture boundaries in this single notebook PDF, so pages are
just numbered straight through under one "notes" unit -- see data/README.md.

Usage: python3 scripts/render_ie802_pages.py
"""
import os

import fitz

SOURCE_PDF = "/Users/akshatmac/Desktop/Sem2/IE802-MINLO/IE802 Notes postmidsem.pdf"
OUTPUT_DIR = "data/raw_scans"
ZOOM = 3.0  # already a high-res phone photo per page; no need for 4x


def render_all():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    mat = fitz.Matrix(ZOOM, ZOOM)
    doc = fitz.open(SOURCE_PDF)
    n = 0
    for i in range(doc.page_count):
        out_name = f"ie802_notes_page{i+1:03d}.jpg"
        out_path = os.path.join(OUTPUT_DIR, out_name)
        if os.path.exists(out_path):
            continue
        doc[i].get_pixmap(matrix=mat).save(out_path)
        n += 1
    print(f"{doc.page_count} pages, rendered {n} new -> {OUTPUT_DIR}")


if __name__ == "__main__":
    render_all()
