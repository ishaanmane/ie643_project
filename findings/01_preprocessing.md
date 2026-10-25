# 01 · Preprocessing

Steps (`01_preprocessing/preprocess.py`, same code for training and uploads): find and flatten the
page -> resize to 2000 px long edge -> flatten illumination -> CLAHE contrast -> denoise. Not
binarised (the model uses pen colour); deskew off by default (it rotated straight pages).

- **New: desk whitening.** 21 IE802 photos sit on a white canvas with only strips of desk and spiral
  binding visible, so no page edge is found and the old crop kept the desk (and a tilt wedge on
  page 049, a test page). Large dark or saturated regions touching the border are now painted
  white before cropping; thin ink strokes are untouched.
- Measured on all 410 raw pages: fires on **19** IE802 pages and on **no** chalkboard, digital-ink or
  HumynLabs page. Final run: brightness crop 336, page warp 55, whiten + crop 19, **0 failures**
  (`results/preprocessing/preprocess_report.csv`).
- The rule was designed by looking at pages from all splits; it has no learned parameters.
- Earlier fixes still in place: no warp on dark (chalkboard) images, page-shape and page-area
  checks for the warp, 2% margin so edge writing is not clipped.
- Alternatives kept as experiments: Sauvola binarisation (`experiments/`), not compared on accuracy.
- **Raw vs preprocessed input** (same trained clean model, `05_evaluation/raw_vs_processed.py`):
  test NED 0.311 preprocessed vs 0.319 raw; paired difference +0.008 (95% CI -0.015 to +0.029),
  preprocessed better on 44 of 76 pages, worse on 25. Val: +0.001 (CI -0.019 to +0.021).
  **Not significant**: the model trained on preprocessed pages reads raw scans about as well.
  Preprocessing's clear benefits are elsewhere: smaller, upright, desk-free images for Surya crops
  and for the PDF appendix, and consistent input for uploads.
