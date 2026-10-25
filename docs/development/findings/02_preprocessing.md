# 02 · Preprocessing

Code: `01_preprocessing/preprocess.py` (`NotesPreprocessor`), run with `batch_preprocess.py`.

## Final pipeline

| # | Step | How |
|---|---|---|
| 1 | Page crop | Find the paper edge (Canny, close gaps, rotated rectangle) and warp it flat, only if the rectangle is page-like; otherwise crop to the content |
| 2 | Deskew | Off by default (see bug 1) |
| 3 | Resize | Long edge 2000 px, before denoising (chalkboard frames are 7168 px wide) |
| 4 | Illumination | Divide by a large-kernel background estimate; light pages only |
| 5 | Contrast | CLAHE on the lightness channel |
| 6 | Denoise | Non-local means |

Output is colour/grayscale, not binarised, because the model can use pen colour and shading. Ishaan's Sauvola binarisation (`sauvola.py`) is kept as an alternative but was not used for training.

## Five bugs found by looking at the output

| # | Bug | Evidence | Fix |
|---|---|---|---|
| 1 | Skew estimate from the bounding box of all ink | Rotated about 81% of chalkboard and digital pages, mean 3.4-3.8°, up to 17° (pages that are straight); `mlt_week01_page016` turned about 13° with text cut off | Removed. Replacement projection-profile estimator tested on pages rotated by a known 1-4°: notebook scans 100% within 0.5°, digital ink 67% within 1°, chalkboard 31% within 1°, so deskew is opt-in only |
| 2 | Page warp on chalkboard frames | 15 frames warped to a tilted block of strokes; most of the board cut off (`lec04_page008`, `lec03_page010`) | Skip the warp on dark images (mean brightness < 100) |
| 3 | Partial page on tilted photos | `ie802_notes_page043, 048, 049` came out 0.47-0.55 as wide as tall (a real page is about 0.75) | Reject warps whose short side is under 0.6 of the long side |
| 4 | Warp to part of the page | 7 IE802 pages (`001, 002, 003, 014, 015, 024, 055`) warped to a rectangle covering only 53-72% of the photo; top or bottom of the page lost. Every correct warp covers at least 85% | Minimum covered area 0.3 → 0.8 |
| 5 | Writing at the paper edge clipped | Last line of `ie802_notes_page033` half cut | Grow the page rectangle 2% per side, edge-replicate past the photo |

Bugs 2-5 were invisible in the summary numbers (0 failures every time); they were found only by viewing before/after images.

## Final result (410 pages)

| Source | Page warp | Content crop |
|---|---|---|
| HumynLabs | 20 | 0 |
| IE802 | 35 | 21 |
| Chalkboard | 0 | 205 |
| Digital ink | 0 | 129 |

55 warped, 355 content-cropped, 0 failures. About 7 minutes on 4 CPU cores. The two near-blank outputs are the two blank pages.

## Reproducibility

Rebuilt on Kaggle, a Mac and the Ubuntu GPU machine: identical image sizes on every page, pixel differences at most 0.5/255 on average (different image-library builds). Bytes are not identical, so "which pages changed" must be decided from the preprocessing report, not from file hashes.

## Known limits

- Show-through (ink from the back of the paper) is not removed.
- Pages that fall back to the content crop can keep some desk or a sliver of the neighbouring page (`ie802_notes_page031` left edge).
- No 90° orientation detection (none of our pages need it).
