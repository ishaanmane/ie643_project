# Surya layout detection: zero-shot results on raw scans

Test of Surya v2 (`surya-ocr` 0.22.1, model `datalab-to/surya-ocr-2`, served with vLLM 0.32 on a Kaggle T4) as the Stage 2 layout detector. No fine-tuning, no preprocessing: the **raw** page images from `data/raw_scans/` were fed in as they are. Raw output is in [surya_raw_results.json](surya_raw_results.json).

10 pages, chosen across all four sources: `ie643_lec12_page007`, `ie643_lec02_page005`, `ie643_lec05_page004`, `ie643_lec09_page006` (chalkboard); `mlt_week03_page001`, `mlt_week08_page004` (digital ink); `ie802_notes_page001`, `ie802_notes_page031` (notebook photos); `hlcs_note01_page001`, `hlcs_note08_page001` (HumynLabs notebook photos).

Judged by eye from the overlay images. This is a qualitative check on 10 pages, not a metric (see "Still to do").

## What worked

| Area | Evidence |
|---|---|
| Runs end to end | All 10 pages returned boxes. No errors, none rejected for length. |
| Separates content types | Text lines, `Equation` blocks, `SectionHeader`, `PageFooter`, `Diagram` and `Table` labels were used sensibly. |
| Clean pages | `mlt_week03_page001`, `hlcs_note01_page001`, `hlcs_note08_page001` are essentially perfect: one box per line or paragraph, headers and page numbers separated. |
| Tables | `ie643_lec05_page004`: the hand-drawn truth table is `Table`, the neuron sketch is `Diagram`. |
| Diagrams | The compile-flow figure (`hlcs_note01`) and the circle sketch (`ie802_notes_page001`) are `Diagram`. |
| Ignores show-through | Faint text from the reverse side of notebook paper was not boxed. |
| Reading order | Returned as `position`; matches top-to-bottom order on single-column pages. |
| Printed extras | Page headers and footers (page numbers, the printed "Camlin" brand) are labelled `PageHeader`/`PageFooter`, so they can be dropped. |

## What did not work

Ranked by how much it matters for us.

1. **Missed handwritten content (`ie802_notes_page001`).** The red margin annotations ("Both schemes are equivalent… more tighter than above") and the "f(x̂)+∇…" line on the right got no box. Content that is not in the main column of a busy notebook page can be silently dropped.
2. **Blocks that mix content types (`ie802_notes_page001`).** `Text-12` (bottom) and `Text-9` each cover text and equations under one `Text` label; several `Equation` boxes overlap neighbouring `Text` boxes.
3. **Overlapping boxes on busy chalkboards (`ie643_lec02_page005`).** The full-width `Text-3` crosses three `Equation` boxes because content and arrows are interleaved. `Equation-0` is clipped at the top edge. This is one of the lowest-resolution pages (2044x1228).
4. **Neighbouring page bleeding in (`ie802_notes_page031`).** `Text-22` ("Integer") is the adjacent page showing at the left margin. Background removal should discard it, which is a reason to feed Surya preprocessed pages.
5. **Wrong label.** The one-hot column vector on `ie643_lec09_page006` is `Diagram` but is an `Equation`; an equation fragment on `ie802_notes_page031` (`Text-24`) is labelled `Text`.
6. **Captions merged (`ie643_lec12_page007`).** The "sample 1 true o/p…" captions under the matrix are part of the last equation box. Our hand tags have them as their own block.
7. **Limits of the source, not of Surya.** `mlt_week08_page004` `Equation-0` is stroke fragments from a page break, and the last equation on `mlt_week03_page001` loses its denominator for the same reason.

## Properties to design around

- **`confidence` is one value per page**, repeated on every box (0.75 to 0.85 here). It cannot be used to filter boxes.
- **Coordinates are in the image's own pixel size**, which varies (7168x4320 for most chalkboard frames, 2044x1228 for the low-resolution ones, about 2448x3170 for MLT). The `raw` field in the JSON holds the model's native 0 to 1000 scale. Store our tags normalised (0 to 1000) so they survive resizing in preprocessing.
- **Needs an inference server.** Surya v2 runs as a client of a vLLM (NVIDIA) or llama.cpp server. On Kaggle there is no Docker, so vLLM must be started by hand with video input disabled (otherwise its start-up memory check fails on a T4); see [README.md](README.md). This makes Surya awkward to bundle into the final app.
- **The model weights are free for research use only** (modified AI Pubs Open RAIL-M).

## Verdict so far

Usable zero-shot on neat pages (digital ink, tidy notebooks) and on chalkboard pages with well-spaced content. Weak on dense notebook pages with margin notes and on chalkboards where items touch. This is not yet enough evidence to decide between "use Surya as it is" and "train a detector on our own boxes".

## Same 10 pages on preprocessed images

Output: [surya_processed_results.json](surya_processed_results.json). Box counts, raw to processed:

| Page | Boxes | What changed |
|---|---|---|
| `ie802_notes_page001` | 14 to 41 | **Big improvement.** The red margin notes ("Both schemes are equivalent…", "any point that satisfies above") and the "f(x̂)+∇…" line are now found, split into line-level boxes. Some overlap remains around the faint pencil sketch, and the crop still shows desk at the top and edges. |
| `ie802_notes_page031` | 28 to 26 | The neighbouring-page bleed ("Integer") is gone. But the two `SectionHeader` boxes ("IInd idea", "IIIrd idea") are now `Text`. |
| `ie643_lec09_page006` | 7 to 6 | The one-hot vector is no longer mislabelled `Diagram`. |
| `hlcs_note08_page001` | 12 to 12 | The title is now `PageHeader`, not `SectionHeader`. |
| `ie643_lec05_page004` | 4 to 4 | One `Equation` became `Text`. |
| `mlt_week08_page004` | 5 to 4 | One `Equation` box fewer. |
| `ie643_lec02_page005`, `ie643_lec12_page007`, `hlcs_note01_page001`, `mlt_week03_page001` | about the same | `ie643_lec12_page007` still merges the captions into the last equation. |

Read: preprocessing helped on the hardest notebook page and removed the bleed, which is what it is for. It did not fix the chalkboard cases, and it slightly changed some labels in both directions (headers lost on two pages). From 10 pages that is a pattern to confirm with the metric, not a result.

Preprocessing problems seen while doing this comparison are in `01_preprocessing/README.md`.

## Still to do

1. ~~Re-run the same 10 pages on the preprocessed images~~ (done, above). Re-run once on the fixed preprocessing for all 410 pages.
2. Hand-box about 20 test-split pages and report IoU / mAP and reading-order accuracy for Surya. Pre-filling the boxes from Surya's output and correcting them by hand is faster than drawing from scratch.
3. Only if the numbers are poor on our pages: train a YOLOv8 detector on those boxes.
