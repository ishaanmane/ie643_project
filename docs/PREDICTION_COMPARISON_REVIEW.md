# Prediction PDF comparison — 2026-10-25

Input commit `cdb2658`; `preds/lora_clean_val`, 25 validation predictions across
IE643 lecture 7 and MLT week 6. Compared page-order rendering to the new base-Qwen
outline (16 and five sections respectively). No recognition weights changed.

## Result and recommendation

Keep **page-order rendering as the current baseline** and the outline optional.
This small comparison does not demonstrate an accuracy improvement from outlining.
It does not establish that semantic outlining is unnecessary for all documents.

| Check | Page order | Outline |
|---|---|---|
| Lecture 7 PDF pages | 8 | 9 |
| MLT week 6 PDF pages | 3 | 3 |
| Intermediate blocks retained | 128/128 | 128/128 |
| Unique math snippets per unit, total | 128 | 128 |
| Diagnosed syntax failures | 1 | 1 |
| Diagram descriptions matched | 9/10 | 9/10 |
| Characters outside horizontal PDF media edges | none detected | none detected |

Both variants use the same predictions and figure matching. Lecture 7 page010 is
absent because it is outside the validation split pending label verification;
all 25 available validation predictions are rendered. Zero measured overflow here
does not negate the overflow found in the separate annotation-based notebook PDF.

## What the additional outline actually changed

Compared Markdown diffs and raster contact sheets of all 23 output PDF pages.

- MLT week 6: the Markdown diff contains exactly one change: `## Training Set vs
  Validation Set` becomes a level-one heading. No equations, crops or content change.
- Lecture 7: adds eight headings and changes heading levels. Some inserted labels
  help navigation, but there is visible repetition: “Directional Derivative” and
  “Directional derivative:”; “Descent Direction” and “Descent direction:”; “Negative
  Gradient Direction” and the original bold label; “Forward Chain Rule” and the
  original bold line. The added “Directional Derivative” section starts at source
  page004's local-minima figure, preceding the explicit definition on page005.
- A new `Blank Page` section is added above an existing blank-page marker. This is
  administrative content, not a useful topic heading.
- Added headings change pagination: lecture 7 is nine pages, and the final page
  contains the end of the equations and the unnecessary blank-page section.
- The code's outline validation checks syntax, IDs and vocabulary. It does not
  establish correct topic boundaries or eliminate semantic duplication. Whole-unit
  vocabulary permits a real topic title to be placed at the wrong block.

## Remaining accuracy problems

MLT week 6 still shows its first failing expression verbatim: the predicted LaTeX
contains an unescaped ampersand and nested dollar delimiters inside `\text{...}`.
Its K-fold diagram description still has no matched crop. The lecture's network
crops still include surrounding handwritten equations, duplicating nearby typeset
material. These problems persist with and without outline generation.

Do not treat successful equation compilation as mathematical correctness. Existing
predictions also contain suspicious formula content (including the Ridge formula)
that requires checking against the original page, not correction by a text-only LLM.

## Concrete next work

1. Use the plain PDFs as the current comparison/demo baseline; keep outlined PDFs
   as an ablation, not a proven improvement. No further outline rerun is justified
   by these two examples alone.
2. Fix rendering defects independently: consistent support for `cancel`, display
   overflow handling, and PDF coordinate/glyph checks. Preserve original strings
   and record any purely syntactic repairs rather than silently modifying labels.
3. Test Surya-assisted figure/table grounding on a small inspected page set. The
   K-fold diagram is a concrete failure case: inspect the source image and layout
   tags before expanding accepted block types. Do not assume that all table blocks
   are diagrams, or constrain recognition to Surya's detected boxes.
4. For future outline work, choose section boundaries from existing heading IDs,
   copy their titles deterministically, exclude blank-page markers, and evaluate
   local topic alignment. For long notebooks use chunks with explicit boundary
   handling rather than repeatedly increasing the output budget.

## Artifacts

- `results/predictions_review/plain/ie643_lec07/ie643_lec07.pdf`
- `results/predictions_review/outlined/ie643_lec07/ie643_lec07.pdf`
- `results/predictions_review/plain/mlt_week06/mlt_week06.pdf`
- `results/predictions_review/outlined/mlt_week06/mlt_week06.pdf`
- Corresponding Markdown/report files and saved outline JSON are in the same tree.
- Local raster previews and extracted text: `out/prediction_comparison/` (ignored).
