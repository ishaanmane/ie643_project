# Step 5 - Evaluation

`evaluate.py` scores a folder of predicted Markdown against `data/annotations/` for one split.

```bash
python3 05_evaluation/evaluate.py --pred preds/final_clean_test --split data/test.jsonl              # basic table
python3 05_evaluation/evaluate.py --pred preds/final_clean_test --split data/test.jsonl --full       # + extended metrics
python3 05_evaluation/evaluate.py --pred preds/final_clean_base_test --compare preds/final_clean_test --split data/test.jsonl
```

| Group | Metric | Why |
|---|---|---|
| Text | CER, WER (page mean, capped at 1) | the original numbers, used during training |
| | corpus CER (total edits / total characters) | standard OCR figure, not dominated by short pages |
| | NED (normalised edit distance, page mean) | as in Nougat and OmniDocBench, comparable with them |
| | text-only CER | without equations and diagram text |
| | token precision / recall / F1 | splits errors into hallucination (precision) and omission (recall) |
| | BLEU-4 | n-gram overlap, reported by Nougat |
| | length ratio | below 1 = cut off / skipped content, above 1 = verbose |
| Equations | exact match (strict, display equations) | original number |
| | normalised P / R / F1 (display + inline) | the same equation written differently (`\le` vs `\leq`, `\left(`, spacing, `x^{2}`) counts as correct |
| | edit score (1 - NED to the closest predicted equation) | partial credit: one wrong symbol is not a total miss |
| Structure | diagram count accuracy, precision, recall | one `[Diagram]` per drawing |
| | heading recall | section structure kept |
| Statistics | 95% bootstrap intervals; paired bootstrap A vs B | 76 test pages is small: shows whether differences are real |

Metrics in `metrics.py`. Considered but not used: **CDM** (renders both LaTeX formulas and matches
characters visually, CVPR 2025; needs its own rendering and detection toolchain) and an LLM judge
(not reproducible). Layout (figure detection) metrics are separate: see `docs/REPORT_NOTES.md`.

## Stage 5 extras

| Script | What | Where it runs |
|---|---|---|
| `layout_counts.py` | Surya figure/table regions vs `[Diagram]` count in the labels, per split and source | Mac, from `data/tags/` -> `results/layout/count_metrics.md` |
| `raw_vs_processed.py` | Same trained model on raw scans instead of preprocessed pages (does preprocessing help?) | GPU -> `preds/final_clean_raw_{val,test}` + paired comparison |
| `crop_review.py` | HTML sheet to hand-grade every placed figure (correct / partial / wrong / not a drawing), and its scorer | sheet built on GPU, graded in any browser |
