# 05 · Evaluation

Code: `05_evaluation/evaluate.py`. References are always read from `data/annotations/` (the current labels).

## Metrics

| Metric | Meaning | Better |
|---|---|---|
| CER | Character error rate on the whole page | lower |
| WER | Word error rate on the whole page | lower |
| text-only CER | CER after removing math and `[Diagram: ...]` lines | lower |
| equation exact match | Share of `$$...$$` equations reproduced exactly (whitespace ignored) | higher |

Per-page CER/WER is capped at 1.0 so a single runaway page cannot dominate the mean. Text-only CER is skipped on pages with under 20 characters of plain text. Results are reported per source and overall.

## Checks on the scorer

Perfect predictions score 0.000 on every metric; randomly dropping 5% of characters gives plausible values; missing predictions are counted, not scored.

## How to read the numbers

- **Diagram descriptions inflate CER.** They are free text, so a correct description in other words counts as errors. Report text-only CER next to CER.
- **Equation exact match is strict.** One different symbol or spacing inside `\left(` counts as a miss; partial credit is not given.
- **Small evaluation set.** Validation is 25 pages from two units. The first 10 validation pages are all one chalkboard lecture, so scores on 10 pages are not representative; use all 25.
- **Topic overlap.** A few val/test pages share equations with neighbouring lectures in train (similarity up to 0.49); see `01_dataset.md`.
- **Labels are unverified,** so part of the measured error may be label error.

## Still to build

- Layout metric: box overlap (IoU / mAP) and reading-order agreement between Surya and hand-checked tags on about 20 pages.
- PDF-level checks once reconstruction exists (LaTeX compile rate, text recoverable from the PDF).
