# IE643 — Handwritten lecture notes to structured PDF (final version)

This branch (`final`) is the clean, single-version project: every stage is re-run from the
source data in order, and every result reported comes from this branch. The development
history (all earlier runs, findings and experiments) is on branch `akshat/dataset-and-preprocessing`.

## Source data (the only inputs that cannot be regenerated)

- `data/raw_scans/` — 410 page images
- `data/annotations/` — 410 Markdown labels (test labels audited: `data/TEST_LABEL_AUDIT.md`)

Split by unit (lecture/week/notebook): train 303, val 31, test 76 — fixed in `00_dataset/build_dataset.py`.

## Pipeline, run in this order (GPU machine, from this folder)

| Stage | Command | Output |
|---|---|---|
| 0 Dataset | `python3 00_dataset/build_dataset.py && python3 00_dataset/check_dataset.py` | `data/splits.json`, `data/{train,val,test}.jsonl` |
| 1 Preprocessing | `python3 01_preprocessing/batch_preprocess.py --workers 8 --force` | `data/processed/` (not in git), `preprocess_report.csv` |
| 2 Layout (Surya v2, zero-shot) | `python3 02_layout/run_layout.py` | `data/tags/`, `data/crops/` (not in git) |
| 3 Recognition (Qwen2.5-VL-7B QLoRA) | `python3 03_recognition/finetune_qwen25vl.py --test` | `runs/final_clean/` (not in git), `preds/final_clean_*` |
| 4 Reconstruction | `04_reconstruction/` (render_document.py, outline.py) | PDFs |
| 5 Evaluation | `05_evaluation/evaluate.py` | scores |
| 6 Interface | `python3 06_interface/manage.py start` | Notes2PDF upload page at https://notes2pdf.<tailnet>.ts.net |

Findings per stage: [findings/](findings/). Each stage folder has its own README; `experiments/` subfolders hold alternatives that were
tried and are reported, but are not part of the final pipeline.
