# Automatic upload evidence — lecture 14

Saved from user-provided downloads on 2026-10-25. Full 66-entry ZIP retained without duplicating its 13 MB PDF and images outside the archive. `MANIFEST.json` records SHA-256 and sizes; ZIP integrity passed and archived PDF byte hash matches supplied `upload_notes (4).pdf`.

- Input: IE643_Lec14_Sept 25.pdf, 10 pages. This is a dataset lecture integration test; held-out/new-data status not established.
- Runtime 94.12 seconds; Surya 0.22.1/vLLM 0.32.0, datalab-to/surya-ocr-2; trained clean Qwen adapter.
- 16/16 descriptions assigned, 47/47 Markdown blocks, 23 math snippets / 1 syntax fallback, 13 PDF pages, 0 outside words.
- GPU user output after completion: 42 MiB, only gnome-shell. Prior completed run also returned 42 MiB.
- PDF visual review pages 1–8: Fig7/8 inaccurate crop-caption association, partial Fig 15 network crop, neighbouring writing, appendix heading before Fig 16; page 2 raw LaTeX caption fallback.

These are execution and reconstruction diagnostics, not OCR or semantic accuracy metrics. No diagrams were manually corrected in this automatic run. Proposed neutral captions / conservative merging / appendix page break are not applied.

Files: complete `document_bundle.zip`; `inference.json`; convenience copies `upload_notes.md`, `diagram_review.json`; `MANIFEST.json`. Inside ZIP: PDF, original input, source appendix images, figures, predictions, tags, raw layout, overlays/logs, preprocessing/inference/diagram reports. Extract outside the tracked tree if you only need to inspect it; original ZIP remains unchanged.
