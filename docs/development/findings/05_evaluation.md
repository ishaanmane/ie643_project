# 05 · Evaluation

Code: `05_evaluation/evaluate.py`. References use `data/annotations/` when present, with the split-record answer as fallback. Split membership comes from the JSONL.

## Metrics

| Metric | Meaning | Better |
|---|---|---|
| CER | Character error rate on the whole page | lower |
| WER | Word error rate on the whole page | lower |
| text-only CER | CER after removing math and `[Diagram: ...]` lines | lower |
| equation exact match | Share of `$$...$$` equations reproduced exactly (whitespace ignored) | higher |

Per-page CER/WER is capped at 1.0 so a single runaway page cannot dominate the mean. Text-only CER is skipped on pages with under 20 characters of plain text. Results are reported per source and overall.

## Checks on the scorer

For identical nonempty references/predictions, CER/WER/text CER are 0.000 and equation match is 1.000 when reference display equations exist; randomly dropping 5% of characters gives plausible values; missing predictions are counted, not scored.

## How to read the numbers

- **Diagram descriptions inflate CER.** They are free text, so a correct description in other words counts as errors. Report text-only CER next to CER.
- **Equation exact match is strict.** One different symbol or spacing inside `\left(` counts as a miss; partial credit is not given.
- **Small evaluation set.** Validation is 25 pages from two units. The first 10 validation pages are all one chalkboard lecture, so scores on 10 pages are not representative; use all 25.
- **Topic overlap.** A few val/test pages share equations with neighbouring lectures in train (similarity up to 0.49); see `01_dataset.md`.
- **Labels are unverified,** so part of the measured error may be label error.

## Remaining evaluation work

- Layout metric: box overlap (IoU / mAP) and reading-order agreement between Surya and hand-checked tags on about 20 pages.
- Independent PDF content/visual accuracy evaluation. Implemented checks already cover compiler completion, diagnosed math failures, Markdown block preservation and PDF word bounds; these do not establish semantic accuracy.

## Generation pipeline smoke check (2026-10-25, Mac)

`outline.py --all --mock`, followed by `render_document.py --all --format md`
and `evaluate_generation.py`, ran on all labels. Results:

- 42 units, 410 pages, no missing pages; **2,579/2,579 blocks retained**.
- 42 mock outlines used, 227 sections; no rejected outlines or validation problems.
- 227/243 diagram descriptions matched to crops.
- 2,739 equation snippets checked with Tectonic; 10 flagged (0.37%).
- 0 PDFs requested; this run checks Markdown reconstruction, not PDF compilation.

Table: `results/generation_eval_mock.md`. Mock outlines use existing headings, so
these numbers do not evaluate LLM section choices. The real GPU run subsequently completed; see the results below. This section retains the earlier mock result for comparison.

Testing found and fixed false missing-block reports for two unmatched lecture 9
diagram descriptions containing square brackets. Captions escape brackets; plain
descriptions do not. The evaluator now distinguishes HTML from PDF output and
includes the equation check method. Additional checks covered accepted, rejected
and absent outlines, Markdown export and empty report folders.

Tectonic crashed inside the sandbox; the full run was repeated outside it, where a
minimal document also compiled successfully. That historical renderer could silently report zero failures after an infrastructure error. Subsequent changes record completed/incomplete math checks explicitly; zero diagnosed failures still does not prove mathematical correctness.

## Metric interpretation corrections

Overall recognition errors are means of capped per-page errors, not corpus CER/WER. Missing prediction files are counted but excluded from the score average; always report coverage. Equation exact match checks each reference display equation for membership in a set of predicted equations; extras and duplicate predictions are not fully penalized. This is a reference-recall-like string score, not semantic equation accuracy. Pages with no reference display equations have no equation score.

## Completed GPU reconstruction and upload checks

| Run | Preservation / layout | Math and PDF checks |
|---|---|---|
|42-unit annotation run|2,579/2,579 blocks;41 outlines/384 sections;227/243 descriptions matched|42 PDFs,410 input pages;2,739 snippets,6 failures;XeLaTeX checks completed|
|Two-unit prediction comparison|128/128 blocks in plain/outlined versions;9/10 matches|One math failure; outlines added duplication/misplaced headings rather than demonstrated fidelity improvement|
|Reviewed validation rendering|128/128 blocks;10/10 matches after one reviewed table link|One reviewed syntax repair leaves zero remaining failures|
|Reviewed notebook rendering|622/622 blocks;58/62 matches +6 extras|Three remaining syntax failures;wide expressions fit;zero outside words|
|Automatic lecture14 upload|47/47 blocks;16/16 descriptions assigned|10 source pages,94.12s;23 snippets,one failure;13 PDF pages;zero outside words|

See [generation review](../docs/GENERATION_RUN_REVIEW.md), [prediction comparison](../docs/PREDICTION_COMPARISON_REVIEW.md) and [upload findings](08_upload_interface_and_reconstruction.md). Annotation-input results, model-prediction results and manually assisted repairs must be kept separate. The latest PDF has visibly incorrect crop-caption associations despite 16/16 assignments; counts alone are insufficient.

Recognition validation remains 25 pages from two units, clean CER 0.277 / text CER 0.222; no new recognition score is claimed from these rendering runs. Test scoring and manual layout metrics remain pending.
