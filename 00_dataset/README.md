# Step 0 - Dataset building

Scripts that produce everything in `data/`. Run from the repo root.

| Script | Purpose |
|---|---|
| `render_pages.py` | IE643 Class Scribes PDFs -> `data/raw_scans/ie643_lecNN_pageNNN.jpg` (PyMuPDF, 4x zoom) |
| `render_mlt_pages.py` | MLT Notes PDFs -> `mlt_weekNN_pageNNN.jpg` |
| `render_ie802_pages.py` | IE802 notebook PDF -> `ie802_notes_pageNNN.jpg` |
| `annotate_gemini.py` | Optional Gemini API auto-transcription (resumable; needs `GEMINI_API_KEY`; free tier is about 20 requests/day) |
| `prompts.py` | `PAGE_PROMPT`, `EQUATION_PROMPT` and `build_record()` for the chat-format JSONL |
| `pdf_to_images.py` | Any PDF, photo or folder -> page images (PyMuPDF), for new input |
| `build_dataset.py` | Pairs `data/processed/` images with `data/annotations/*.md`, splits by unit, writes JSONL, `splits.json` and `data/VERIFICATION.md` |
| `build_external_dataset.py`, `combine_with_core.py` | Opt-in contingency for external equation datasets (see `data/EXTERNAL_DATASETS.md`); not run on real data yet |

Dataset details, splits and annotation methods: [../data/README.md](../data/README.md).
