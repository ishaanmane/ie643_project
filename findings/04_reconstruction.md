# 04 · Reconstruction (deterministic renderer + LLM outline)

Run (re-run with trimmed crops): `04_reconstruction/run_reconstruction.sh` on the fine-tuned clean model's predictions;
reports and PDFs in `results/reconstruction/`. No hand fixes applied.

| | val (4 units, 31 pages) | test (9 units, 76 pages) |
|---|---|---|
| Blocks kept (no content lost, plain and outlined) | 189 / 189 | 529 / 529 |
| Outlines accepted | 4 / 4, 28 sections | 9 / 9, 55 sections |
| Section titles dropped by the word check (invented words) | 2 | 6 |
| Equations failing the LaTeX check (shown verbatim with a warning) | 1 / 192 (0.5%) | 3 / 471 (0.6%) |
| `[Diagram]` descriptions matched to a Surya crop | 20 / 22 | 37 / 42 |
| PDFs built | 4 / 4 | 9 / 9 |

- **Plain vs outlined:** identical content (same blocks, equations, figures); the outline only
  adds section headings. Titles are faithful: when a section starts on a heading the notes' own
  wording is used, and a model title with words not in the notes drops that section break
  (e.g. "Kullback-Leibler Divergence", "Mistake Analysis" were proposed but not used).
  Examples of accepted structure: lec09 Announcements -> Backward Pass (Recall) ->
  Vanishing/Exploding Grad -> ... -> Soft-Max Function.
- **Hand-graded figures** (all 58 placed in val + test, `results/crop_review/summary.md`):
  72% correct, 12% partial crop, 12% wrong drawing, 3% not a drawing; right drawing 84.5%.
  Chalkboard 15/16 and digital ink 17/18 correct; IE802 notebook pages only 10/24 (dense small
  sketches: Surya splits/merges them and position matching picks a neighbour).
- **PDF style:** Merriweather text (bundled, OFL), Latin Modern maths, DejaVu Serif for arrows,
  circled numbers and check marks Merriweather lacks; uniform green headings, 1.18 line spacing,
  paragraph gaps, grey captions with green labels, running title and page numbers.
- **Fixes from looking at the PDFs:** stray `<!-- page -->` text on uploads; running title on
  page 1; loose Surya boxes left large white areas around drawings, so crops are now trimmed to
  the ink with a small margin.
- **Known limitations:** partial crops when Surya's box cuts a drawing (lec07 Figure 1); a
  sentence continuing onto the next page is not joined; recaps are not marked; equation checks
  are syntax only.
