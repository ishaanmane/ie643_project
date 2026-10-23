# Step 1 - Preprocessing

Turns a raw page photo or scan into a clean page image for layout detection and the VLM.

## What the pipeline does (`preprocess.py`, `NotesPreprocessor`)

| # | Step | How | Notes |
|---|---|---|---|
| 1 | Background removal | Canny edges, close gaps, fit a rotated rectangle to the largest shape, perspective-warp it flat. Falls back to a brightness bounding-box crop. | Works on notebook photos. Chalkboard frames and digital-ink pages have no page edge, so they use the fallback (crop to content). |
| 2 | Deskew | Projection-profile estimator, strict confidence gate | **Off by default**, see below. |
| 3 | Resize | Long edge to 2000 px | Done before denoising for speed (the chalkboard frames are 7168 px wide). |
| 4 | Illumination flattening | Divide by a large-kernel morphological background | Light backgrounds only; fixes shadows and uneven light. |
| 5 | Contrast | CLAHE on the lightness channel | |
| 6 | Denoise | Non-local-means | |

The output is **not binarized**: the VLM can use shading and pen colour. `sauvola.py` is Ishaan's binarization alternative, kept for comparison; `binarize()` in `preprocess.py` is a debug view.

## Why deskew is off by default (measured)

The first version estimated skew from the bounding rectangle of all ink pixels. On a quarter of the pages it rotated **about 81% of the digital-ink and chalkboard pages** (mean 3.4 to 3.8 degrees, up to 17), although digital pages are perfectly straight. Handwriting drift, not page tilt, was being "corrected", and content got clipped at the edge (for example `mlt_week01_page016`). That estimator is removed.

The replacement (projection profile of a downsampled ink mask) was tested by rotating pages by a known 1 to 4 degrees:

| Source | recovered within 0.5 deg | within 1 deg |
|---|---|---|
| IE802 notebook scans (ruled, dense) | 100% | 100% |
| MLT digital ink | 50% | 67% |
| IE643 chalkboard | 0% | 31% |

So it only works on dense, line-structured pages (a chalkboard of equations has no text lines to align). It is therefore opt-in (`--deskew`, gated at confidence gain >= 1.3 and angle >= 0.75 degrees). Photos are straightened by the page warp in step 1.

> **`data/processed/` made before this fix is stale.** If you have an older copy, regenerate it with `--force`.

## Running

From the repo root, in this order:

```bash
pip install -r requirements.txt

# quick check: 16 evenly spaced pages to a scratch folder, plus before/after sheets
python3 01_preprocessing/batch_preprocess.py --sample 16 --out /tmp/pp_test --force --workers 4
python3 01_preprocessing/compare_sheet.py --out /tmp/pp_test --max 16

# the real run: all 410 pages -> data/processed/ (+ preprocess_report.csv), resumable
python3 01_preprocessing/batch_preprocess.py --workers 4 --force
```

Each page's `preprocess_report.csv` row records the crop method (`quad` or `brightness`), the fraction of the image the page boundary covered, the skew applied, the resize scale, and brightness / contrast / sharpness of the result. 16 pages take about 15 seconds on 4 workers on a laptop.

## Page-boundary step: bugs found by inspecting the first full run

The first full run (410 pages, 0 failures) looked fine in the report but not in the images:

- **Chalkboard frames:** 15 of them went through the page warp (`quad`). A board has no page edge, so the "page" it found was a block of strokes; the warp kept a tilted sub-region and **cut off most of the board** (`ie643_lec04_page008`, `ie643_lec03_page010`). Fix: the warp is skipped when the image is dark (mean brightness < 100).
- **Notebook photos:** on `ie802_notes_page043, 048, 049` the warp lost part of the page or left it tilted with a black wedge; the output was 0.47 to 0.55 as wide as it was tall, against 0.75 for a real page. Fix: a candidate whose short side is under 0.6 of its long side is rejected and the content crop is used instead.

After the fix, all four chalkboard test pages are content-cropped with a normal aspect, and the notebook pages that were warped correctly (`hlcs_note01`, `ie802_notes_page026`, `031`) are unchanged. This was checked on 11 pages, not on all 410. The full re-run on the fixed code is still to be done and its counts recorded here.

Before the fix the counts were: HumynLabs 20 of 20 warped, IE802 45 of 56, IE643 15 of 205, MLT 0 of 129. The 2 near-zero-contrast outputs are the 2 blank pages, as expected.

Still weak after the fix:
- `ie802_notes_page043, 048, 049` fall back to the content crop, so they keep the desk and, for 049, a tilted page with a black wedge.
- `ie802_notes_page001`: the warp keeps some desk (aspect 1.08 for a portrait page), although layout detection now works on it.
- The other IE802 pages that fell back (`007, 016, 017, 018, 030, 034, 035, 036, 039, 041, 045`) were not inspected; 016 and 017 are flat scans.

## Files

| File | Purpose |
|---|---|
| `preprocess.py` | `NotesPreprocessor` (`process`, `process_with_info`, `estimate_skew`, `binarize`) |
| `batch_preprocess.py` | Run it over `data/raw_scans/`; `--sample`, `--workers`, `--force`, `--deskew`, QA CSV |
| `compare_sheet.py` | Side-by-side raw / processed PNGs for visual QA |
| `sauvola.py`, `binarized_sauvola/` | Sauvola binarization alternative and its sample outputs |

## Known limits / not built yet

- No orientation detection (pages rotated by 90 degrees). None of the 410 pages need it: the 7 landscape IE802 pages are upright scans.
- Show-through (ink from the back of the paper) is not removed; the layout model ignored it in the Surya test, but it is still in the image.
- Photo pages can keep a strip of desk or an adjacent page (`ie802_notes_page031` shows the neighbouring page at the left edge in the raw scan); the page warp catches most of it, not all.
- No automatic pass/fail on the output. Check the report columns and the compare sheets.
- Binarized (Sauvola) versus our grayscale output has not been compared on recognition accuracy.
