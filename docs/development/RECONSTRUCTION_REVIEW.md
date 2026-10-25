# Reconstruction review and Surya experiment

Reviewed on 2026-10-25. This is an inspection and experiment design, not a measured
claim that adding Surya improves Qwen.

## Material inspected

- All 9 pages of `results/pdfs/ie643_lec07_model_outline.pdf` as rendered images,
  with larger views of pages 7 and 8.
- All 3 pages of `results/pdfs/mlt_week06_model_outline.pdf` as rendered images.
- Extracted text from both PDFs, the clean adapter predictions, selected processed
  source images, Surya tags and the renderer/outline implementation.
- PDF image source dimensions and displayed dimensions, read with pdfplumber.

The PDFs use model predictions, whereas the earlier 42-unit mock check used labels.
Their block counts therefore differ. Keeping extracted text is not evidence that
the extraction matches the source image.

## Verified observations

| Location | Observation | Cause or evidence | Improvement |
|---|---|---|---|
| Both PDFs, figures | Every image is displayed at approximately 274.2 x 203.6 PDF points, regardless of its shape. | `figure_md` emits both `width=55%` and `height=30%`. Week 6's image is 667 x 134 px (4.98:1), displayed at 1.35:1. | Fit inside a maximum rectangle while preserving aspect ratio. Test displayed aspect ratios automatically. |
| Week 6, PDF p2 | The K-fold illustration appears only as a diagram description. | The source page 3 contains the fold boxes. Surya detects that region as `b5`, type `table`; `page_figures` selects only `figure`. | Consider table regions as candidates for an unmatched diagram, using spatial/text evidence. Do not treat every table as a figure globally. |
| Lecture 7, PDF p7 | Figure 7 contains a large part of the original page, including equations already typeset below/after it. | Source page 17 has six Markdown blocks, but Surya provides one full-page figure box. | Detect mixed-content/whole-page regions; flag or refine the figure boundary instead of assuming the box is a clean drawing. |
| Lecture 7, PDF p8 | The figure crop cuts through lower handwritten labels. | Source page 18 figure `b4` ends at normalized y=720; the nearby equation region overlaps it. | Flag boundary ink/overlapping regions; inspect a contextual crop and refine bounds. Blindly enlarging can pull equations back into the figure. |
| Lecture 7, PDF pp3-5,7-8 | Added section titles repeat local headings/labels, e.g. Directional Derivative / Directional derivative, Descent Direction / Descent direction, and Forward Chain Rule / forward chain rule. | The outline inserts a heading before an existing bold text block; heading handling only recognizes Markdown `#` headings. | Promote an existing title block when supported, retaining its exact wording once; use a clear hierarchy. |
| Lecture 7, PDF p2 | `NP-hard` and `local minimum` appear as detached lines below a figure that already contains labels. | Their relationship to the figure is lost during linear reconstruction. | Represent label-to-figure relations; move verified labels into a caption or associated note while preserving text and provenance. |
| Week 6, PDF p1 | One equation is displayed as raw LaTeX with a warning. | Prediction contains malformed math/text markup, including `&` in a text context. | Keep the warning, add a source-region image fallback and a targeted reread. Any proposed repair must be logged and source-checked. |
| Week 6, PDF p3 | `Ridge` is inserted into the formula's minimization subscript. | Prediction contains `\min_{l> \text{Ridge}}`. The source image shows a separate green arrow annotation saying Ridge. The formula compiles despite the error. | Use source geometry to distinguish annotations from math, and targeted crop verification. Compilation measures syntax, not mathematical fidelity. |
| Lecture 7, PDF p9 | `(blank page - no content)` is shown as document content. | The extraction marker is passed through. | Represent verified blank-page status as metadata; preserve traceability without presenting a placeholder as lecture content. |

## What the models currently do

Recognition uses the fine-tuned clean adapter. The outline pass does **not** load
that adapter: `call_llm` loads base Qwen2.5-VL-7B-Instruct in 4-bit, text-only.
Its input is block id, Markdown-derived type and at most 90 characters per block.
It sees neither images nor Surya metadata. Reusing base model weights is convenient,
but there is no evidence that our transcription adapter improves outlining.

Surya is currently used mainly for figure crops. Its documented layout output
contains region types and reading order, and OCR can provide region text:
<https://huggingface.co/datalab-to/surya-ocr-2/blob/main/README.md>.
Our saved tags are layout-only: inspected blocks have `text_preview: null`.
We need region text or another source-grounded association step to align them
reliably with Markdown. A region's position in one list is not its identity in
the other list. Page 17's 6-to-1 mismatch is a direct counterexample.

## Proposed combined pipeline

1. Keep full-page clean-adapter recognition as the primary transcript. Do not
   discard blocks merely because Surya did not detect them; the boxed model
   previously lost side notes.
2. Run Surya alongside it. Retain page id, image dimensions, region id, type,
   box, reading order and overlap information. Obtain region OCR for alignment,
   starting with headings, figure labels and suspicious equation regions.
3. Build a common block representation with original text, source ids,
   candidate region associations and an explicit association status. Support
   one-to-many/many-to-one matches and an unmatched state. Use text similarity,
   region type and order jointly; page-level confidence is not a calibrated
   per-region match confidence.
4. Give the organiser both the text and grounded layout evidence. Ask for
   relationships: section start/level, label-to-figure, caption-to-figure,
   continuation of a paragraph/derivation. Have it cite existing ids and abstain
   where the source is ambiguous. Do not permit free rewriting of equations.
5. Validate the relationships, preserve every content block and render
   deterministically. Retain source references and log any presentation changes.
6. Reread selected source crops when models disagree or an equation fails.
   Compare a clean-adapter crop read against its full-page read, using context;
   crop inference is a new condition and must be tested rather than assumed better.

This uses Surya to improve grounding throughout reconstruction. Simply adding a
list of boxes to the existing prompt would not establish which text belongs to
which box, and would not fix stretched images or extraction mistakes.

## Experiment before a full GPU run

First fix renderer geometry and establish a small source-checked evaluation set.
Use all 25 validation pages (lecture 7 and week 6) for model-prediction comparisons.
Add a separately reported diagnostic sample of difficult notebook/low-resolution
pages; training pages are diagnostics, not held-out accuracy measurements. Human
check the references used for this experiment.

Compare with the same predictions, renderer and model settings:

| Variant | Structure input | Purpose |
|---|---|---|
| A | Existing Markdown headings, no second LLM pass | Cheapest structure baseline |
| B | Current text-only Qwen outline | Current behaviour |
| C | Same base Qwen with text plus aligned Surya evidence | Isolate the benefit of layout grounding |
| D, later | C plus targeted source-crop rereads | Isolate extraction repair from structural changes |

First inspect the alignment accuracy independently. If it is poor, an apparent
outline failure may actually be a bad text-to-region match. A fine-tuned-adapter
versus base-model outline comparison is a separate experiment, after C; our
adapter was trained for transcription rather than document organisation.

Judge against source images, not visual polish alone:

- Lost, duplicated or reordered blocks, including occurrences of repeated text.
  The current substring-based preservation check cannot establish all three.
- Correct section boundaries and levels, judged on a small human reference.
- Correct figure-description matches and complete crops; a high match count can
  hide incorrect pairings.
- Correct assignment of labels/captions/annotations to their parent region.
- Source-faithful equations, independently from compilation success.
- Figure aspect ratio, overflow, heading repetition, page breaks and readable
  figure labels in the rendered PDF.
- Runtime/VRAM and the number of uncertain cases requiring review.

## Priority

1. Preserve figure aspect ratios; add visible PDF checks.
2. Repair figure candidate handling and flag mixed/partial crops.
3. Ground text blocks to Surya regions and test C against A/B on validation.
4. Add targeted verification of equations and spatial annotations.
5. Refine heading promotion, captions and page-break behaviour.

Real LLM comparison remains pending on the GPU. This review makes no claim of an
accuracy improvement from a combined model run.
