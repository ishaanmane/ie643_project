# Handwritten Lecture Notes to Digital PDF

IE643 course project (Team InTra): convert photos or scans of handwritten lecture notes into clean, searchable, structured PDFs.
The official problem statement is in [docs/PROJECT_STATEMENT.md](docs/PROJECT_STATEMENT.md); the full design is in [docs/PIPELINE.md](docs/PIPELINE.md).

## Pipeline and repo layout

The folders are numbered in pipeline order. Each has its own README.

| Step | Folder | What it does | Status |
|---|---|---|---|
| 0 | [00_dataset/](00_dataset/) | Render source PDFs to page images, write ground-truth Markdown, build train/val/test JSONL | Done (410 pages, labels not yet human-verified) |
| 1 | [01_preprocessing/](01_preprocessing/) | Page-boundary warp, deskew, contrast, denoise (`preprocess.py`); Sauvola binarization as an alternative (`sauvola.py`) | Done; full re-run with the newest background removal pending |
| 2 | [02_layout/](02_layout/) | Layout detection (Surya / YOLOv8): figures, equations, reading order | To do |
| 3 | [03_recognition/](03_recognition/) | Fine-tune Qwen2.5-VL-7B (4-bit LoRA) to turn a page into Markdown + LaTeX | To do |
| 4 | [04_reconstruction/](04_reconstruction/) | Merge pages into one Markdown document, then Pandoc + XeLaTeX to a searchable PDF | To do |
| 5 | [05_evaluation/](05_evaluation/) | CER/WER, equation exact-match, LaTeX compile rate and other metrics | To do |

Other folders:

- [data/](data/) - page images (`raw_scans/`), ground truth (`annotations/`), region tags and context examples, JSONL splits. See [data/README.md](data/README.md).
- [docs/](docs/) - project statement, pipeline design, and earlier planning notes in `docs/planning/`.

## Quick start

```bash
pip install -r requirements.txt

# run everything from the repo root
python3 01_preprocessing/batch_preprocess.py          # data/raw_scans -> data/processed (add --force to redo all)
python3 00_dataset/build_dataset.py                   # -> data/train.jsonl, val.jsonl, test.jsonl, splits.json
python3 01_preprocessing/sauvola.py --step 10 --compare   # optional: Sauvola binarization samples
```

Rendering pages from PDFs (`00_dataset/render_*.py`) needs the original lecture PDFs, which are not in this repo.

## Dataset at a glance

410 handwritten pages from four sources (IE643 chalkboard scribes, MLT digital-ink notes, IE802 notebook photos, HumynLabs CS notes), split by lecture or week so near-duplicate pages never leak between train and test: 324 train, 26 val, 60 test.

## Notes

- `data/processed/` is generated and gitignored (about 150 MB); the JSONL files reference it, so preprocess before training.
- Ground-truth labels are AI-generated and unverified. The checklist for manual review is [data/VERIFICATION.md](data/VERIFICATION.md).
