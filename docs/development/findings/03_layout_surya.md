# 03 · Layout detection (Surya v2)

Model: `surya-ocr` 0.22.1 with `datalab-to/surya-ocr-2` (0.7B), zero-shot, served by vLLM 0.32 on a Kaggle T4. Weights are free for research use. Detailed write-up of the 10-page test: `02_layout/experiments/SURYA_FINDINGS.md`.

## 10-page test on raw scans

Worked: one box per line or paragraph on clean pages; tables and diagrams labelled correctly (`lec05_page004` truth table and neuron sketch); show-through ignored; headers and footers separated; sensible reading order.

Did not work:
1. Missed red margin notes on `ie802_notes_page001`.
2. Mixed text-and-equation blocks under one label on dense notebook pages.
3. Overlapping boxes on busy, low-resolution chalkboards (`lec02_page005`).
4. Neighbouring page detected as text (`ie802_notes_page031`, "Integer").
5. Some wrong labels (a one-hot vector as `Diagram`), captions merged into equations.

## Same pages after preprocessing

| Page | Boxes raw → processed | Change |
|---|---|---|
| `ie802_notes_page001` | 14 → 41 | Margin notes now found |
| `ie802_notes_page031` | 28 → 26 | Neighbouring-page bleed gone; two headings now labelled text |
| `lec09_page006` | 7 → 6 | Vector no longer mislabelled as a diagram |
| `hlcs_note08` | 12 → 12 | Title became page header |

Preprocessing helped where it is meant to (busy notebook photos) and changed a few labels both ways. Surya therefore runs on preprocessed pages.

## Full run (corrected images)

410 pages, 0 errors; 21 pages took 69 s on the T4. 4,283 blocks: text 2,166 · equation 1,350 · figure 333 · page footer 165 · heading 164 · list 54 · page header 37 · table 14. Only the 2 blank pages have no blocks.

## Outputs

- `02_layout/experiments/surya_results_all.json`: raw Surya output, the only part that needs a GPU.
- `data/tags/<page>.json` (`surya_to_tags.py`): blocks in reading order with type, box normalised to 0-1000, header/footer flag. Unverified drafts.
- `data/crops/` (gitignored): figure and table crops for the PDF stage.
- `data/processed_boxed/` (`draw_boxes.py`): thin cyan boxes, no labels (labels would cover handwriting and could be copied into the output).

## Properties to design around

- `confidence` is one value per page, so it cannot rank boxes.
- Coordinates are in each image's pixels; stored normalised so they survive resizing. Boxes only map onto the exact image Surya saw: the converter refuses to crop otherwise.
- Surya v2 needs a model server (vLLM on NVIDIA). The upload app now manages that server in an isolated process before recognition. A boxed-input recognition variant would also require compatible layout inputs; the chosen clean variant does not.

## Fresh-upload integration and limitations (2026-10-25)

Verified the GPU client is Surya 0.22.1 with vLLM 0.32.0 and the same `datalab-to/surya-ocr-2` checkpoint used for the reviewed Kaggle run. Surya 0.7.0 found in the recognition environment was not substituted. Separate Python 3.11 environments avoid dependency changes to Qwen. Layout runs on job-local processed images, with coverage/dimension/bounds checks before normalized tags and crops are written.

Lecture12 manual rebuild assigned 9 descriptions, inserted 3 extras and left 2 unmatched. Visual inspection confirmed missing real diagrams on source pages 17/19: their regions were classified as equations/text. Automatic lecture14 assigned 16/16 descriptions, but some caption associations and crop extents were wrong. One page's 12 raw regions were merged to one figure. This motivates conservative matching and review flags; assignment coverage is not layout accuracy. Details: [upload findings](08_upload_interface_and_reconstruction.md).
