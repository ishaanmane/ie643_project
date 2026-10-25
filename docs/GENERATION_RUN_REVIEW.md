# Review of GPU reconstruction run — 2026-10-25

Reviewed commit `66e36dc`: 42 report files and three annotation-input PDFs.
This is a reconstruction smoke test, not a held-out OCR accuracy result.

## Confirmed run results

42 PDFs, 410 input pages, no missing reports/pages. Ordered intermediate Markdown
retention 2,579/2,579. Outlines used for 41 units (384 sections); IE802 fell back to
page order. 227/243 diagram descriptions matched. All XeLaTeX checks completed;
six unique equation snippets (counted per unit) were diagnosed as failures.

## Visual and programmatic inspection

- IE643 lecture 7: eight PDF pages, eight images. Reviewed the whole-document
  contact sheet. Figure dimensions preserve source aspect ratios (maximum relative
  error below 0.000001). Duplicate-looking labels/headings remain, e.g. “Supervised
  Learning”, “Descent Direction”, “Forward Chain Rule”. Crops still include nearby
  handwriting; correct scaling does not establish crop completeness or matching.
- MLT week 6: three pages, individually reviewed. No embedded raster images in
  this annotation-based version: its table and fold notation are typeset from
  annotations. This must not be confused with the model-prediction version, which
  contains diagram descriptions and a crop. The long first heading hyphenates.
- IE802: 59 pages, 64 images. Reviewed all pages as contact sheets and inspected
  pages 25 and 29 at larger resolution. All image aspect ratios are preserved
  (maximum relative error below 0.000001). Some crops retain scan borders and
  nearby handwriting. Some text glyphs appear as missing-glyph boxes in the sheets.
- **Confirmed clipping:** IE802 page 25 has 11 characters beyond the right media
  edge (ending “weak relaxation”); page 29 has nine (ending “column 1, Rank 1”).
  Both are long display equations containing prose. Visible content is lost despite
  100% intermediate Markdown retention and successful PDF compilation.
  The other two PDFs have no character coordinates outside horizontal media edges.
  This coordinate check is not an exhaustive overlap or mathematical-fidelity audit.

## Notebook outline diagnosis

The first run was truncated. The 4,096-token retry is complete and ends with a
closed list/code fence. It fails JSON decoding at line 12, column 72 because a
LaTeX `\leq` command is not JSON-escaped. There are 57 proposed section entries,
contrary to the prompt's maximum 24; many titles are dates, equations or generic
labels. Increasing tokens again is not an appropriate next step. Keep page-order
fallback for this delivery; later use smaller input chunks or select existing
heading IDs with titles copied deterministically. Do not blindly repair and accept
this response as evidence of good structure.

## Six diagnosed equation failures

IE802 (four): `\[0,10\]`, `x_1\in\[0,5\]`,
`\min \bcancel{c^Tx}`, and an exponential-constraint expression with unescaped
`&` inside `\text{...}`. MLT week 4 (two): `\[0,1\]`, `p \in \[0,1\]`.

The bracket sequences are display delimiters used where literal interval brackets
were intended; this requires source verification before editing annotations.
`\bcancel` requires the `cancel` package, absent from the checker/renderer preamble:
this is a package-support issue, not proof of bad recognition. The ampersand is a
LaTeX escaping issue. The current visible verbatim fallback preserves the strings.
Do not report all six as incorrect mathematics or recognition mistakes.

## Next work, in priority order

1. Generate separate outlines for `preds/lora_clean_val` (lecture 7 and MLT week 6).
   Never apply annotation-derived block IDs to prediction-derived blocks.
2. Render actual predictions with and without these outlines; compare the same
   source pages for missing content, formula fidelity, section duplication, and crops.
3. Fix display overflow without changing formula meaning; add PDF bounds checks.
   Add consistent `cancel` support to the checker and PDF preamble, then validate.
4. Diagnose missing glyphs and improve figure crop/description grounding, with
   source-image checks. Avoid arbitrary crop expansion or treating every table as
   a diagram. Keep Surya disagreement as review evidence, not automatic correction.
5. Keep existing trained recognition weights for the deadline. A new training run
   needs a concrete error target and a held-out comparison before replacing them.

Evidence: `results/generation_eval.md`, `results/generation_review/reports/`,
`results/generation_review/ie802_outline_rejected.json`, and PDFs in
`results/generation_review/`. Local read-only raster previews are in
`out/gpu_pdf_review/` (gitignored).
