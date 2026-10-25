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
- Planned: raw vs preprocessed recognition accuracy with the trained model (no retraining).
