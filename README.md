# Handwritten Lecture Notes to Digital PDF

IE643 course project (Team InTra): convert photos or scans of handwritten lecture notes into clean, searchable, structured PDFs.
The official problem statement is in [docs/PROJECT_STATEMENT.md](docs/PROJECT_STATEMENT.md); the full design is in [docs/PIPELINE.md](docs/PIPELINE.md).

## Pipeline and repo layout

The folders are numbered in pipeline order. Each has its own README.

| Step | Folder | What it does | Status |
|---|---|---|---|
| 0 | [00_dataset/](00_dataset/) | Render source PDFs to page images, write ground-truth Markdown, build train/val/test JSONL | Done (410 pages, labels not yet human-verified) |
| 1 | [01_preprocessing/](01_preprocessing/) | Page-boundary warp, deskew, contrast, denoise (`preprocess.py`); Sauvola binarization as an alternative (`sauvola.py`) | 410 corrected pages: 55 warped, 355 cropped; deskew off |
| 2 | [02_layout/](02_layout/) | Layout detection (Surya / YOLOv8): figures, equations, reading order | 410 pages, 4,283 blocks; manual layout metric pending |
| 3 | [03_recognition/](03_recognition/) | Fine-tune Qwen2.5-VL-7B (4-bit LoRA) to turn a page into Markdown + LaTeX | Implemented; see current findings |
| 4 | [04_reconstruction/](04_reconstruction/) | Merge pages into one Markdown document, then Pandoc + XeLaTeX to a searchable PDF | Implemented; see current findings |
| 5 | [05_evaluation/](05_evaluation/) | CER/WER, equation exact-match, LaTeX compile rate and other metrics | Implemented; see current findings |

Other folders:

- [data/](data/) - page images (`raw_scans/`), ground truth (`annotations/`), region tags and context examples, JSONL splits. See [data/README.md](data/README.md).
- [docs/HANDOFF.md](docs/HANDOFF.md) - full context for a new session: setup, results, gotchas, current work.
- [findings/](findings/) - what was built, measured and learned, one file per stage.
- [docs/](docs/) - project statement, pipeline design, [dataset audit](docs/DATASET_AUDIT.md), and earlier planning notes in `docs/planning/`.

## Quick start

```bash
pip install -r requirements.txt

# run everything from the repo root
python3 01_preprocessing/batch_preprocess.py --workers 4 --force   # data/raw_scans -> data/processed + QA report
python3 00_dataset/build_dataset.py                   # -> data/train.jsonl, val.jsonl, test.jsonl, splits.json
python3 01_preprocessing/sauvola.py --step 10 --compare   # optional: Sauvola binarization samples
```

Rendering pages from PDFs (`00_dataset/render_*.py`) needs the original lecture PDFs, which are not in this repo.

## Dataset at a glance

410 handwritten pages from four sources (IE643 chalkboard scribes, MLT digital-ink notes, IE802 notebook photos, HumynLabs CS notes), split by lecture or week to reduce leakage: 318 train, 25 val, 55 test, and 12 excluded uncertain pages. Unit-level splitting reduces near-duplicate leakage; validation and test contain no notebook-photo pages.

## Notes

- `data/processed/` is generated and gitignored (about 150 MB); the JSONL files reference it, so preprocess before training.
- Ground-truth labels are AI-generated and unverified. The checklist for manual review is [data/VERIFICATION.md](data/VERIFICATION.md).

## Current demo and evidence

See [06_interface/README.md](06_interface/README.md) for inference on new images/PDFs and the local upload interface. It reuses the clean trained adapter; automatic Surya v2 layout and isolated GPU recognition are verified. Detected diagram crops are inserted and original pages remain appended; matching/captions still need review.

Clean adapter validation CER is 0.277 on 25 pages (capped per-page macro metric against unverified labels). Test scoring remains pending. Reconstruction checks, syntax checks and manual rendering repairs do not establish OCR or equation correctness. See [submission readiness](docs/SUBMISSION_READINESS.md) and [findings](findings/).

## Continuing this project

Read [the current handoff](docs/HANDOFF.md) first, then [the complete work history](docs/WORK_LOG_2026-10-25.md) and [service runbook](docs/OPERATIONS.md). [Latest automatic upload evidence](results/upload_automated_review/README.md) includes the full downloadable bundle and checksums.
