# Dataset audit

Checked against the repo as of this commit (410 pages, `data/`). "Fix" means a concrete action; items marked **decision** need a team choice before anyone changes files.

## What is consistent

- 410 raw images, 410 annotation files, no missing or extra pairs. No empty annotations; 2 deliberately blank pages are marked as such (`ie643_lec07_page020`, `mlt_week01_page013`).
- Splits are by unit, so near-duplicate consecutive pages do not leak: train 324, val 26, test 60.
- The 7 landscape IE802 pages are upright scans, so no rotation fix is needed.
- JSONL files reference `data/processed/<stem>.jpg`; the stems exist in `data/raw_scans/`.

## Problems, most important first

1. **`data/processed/` from before this commit is wrong for many pages.** The old skew step rotated about 80% of the digital-ink and chalkboard pages by up to 14 degrees and clipped content (see `01_preprocessing/README.md`). The JSONL files point at those images. **Fix:** regenerate with `python3 01_preprocessing/batch_preprocess.py --workers 4 --force`; no JSONL change is needed because the file names stay the same. Do this before any fine-tuning or Surya run on processed pages.

2. **The test and validation sets contain no notebook-photo pages. (decision)** All 56 `ie802_*` and 20 `hlcs_*` pages are in train; test is 34 chalkboard + 26 digital-ink pages, val is 20 + 6. The notebook-photo case, the messy-photo case the project is about and the one Surya found hardest, is never measured. Suggestion: hold out a contiguous block of IE802 (for example pages 41 to 56, same notebook so no leakage) and 4 of the 20 HumynLabs notes for test, and a few more for val. That moves about 20 pages out of train and adds them to the pages that need manual checking. Change `HELD_OUT` in `00_dataset/build_dataset.py` and re-run it.

3. **Region-level tags and context exist for 1 page out of 410.** `data/tags/` and `data/context/` only hold the worked example `ie643_lec12_page007`, with hand-estimated boxes. Layout evaluation needs boxes. **Fix:** hand-box about 20 test-split pages (including some notebook pages if item 2 is done). Fastest route: run Surya on those pages, convert its boxes to the tags format, then correct them by hand. Store boxes normalised to 0 to 1000 (Surya's native scale) so they survive resizing.

4. **Labels are AI-written and unverified.** *(Partly handled: the 12 `??` pages are now left out of all splits until fixed, giving train 318, val 25, test 55.)* 11 pages came from the Gemini API and 399 from direct transcription. Open work in `data/VERIFICATION.md`: 12 flagged `??` pages, 100% of test (60), a sample of val. A spot check of 2 early pages found 1 error, so the rest almost certainly contain some. Test labels are what every reported number is measured against, so they need a human pass first.

5. **Low writer and style diversity.** Each source is mostly one person's handwriting (one lecturer on the board, one student's MLT notes, one IE802 notebook, a few HumynLabs notebooks). The model may learn those writers, and test numbers will not show how it does on a stranger's writing. **Fix:** say so in the report; if time allows add pages from other writers (for example the HumynLabs dataset has more notebooks than the 20 we took).

6. **Low-resolution chalkboard pages.** The 16 pages of `ie643_lec02` are 2044x1228 while the other chalkboard frames are 7168x4320. They give blocky images and the worst Surya result (`ie643_lec02_page005`). Keep them but note them in the report; do not read them as typical.

7. **Diagram handling is text only.** 195 of 410 annotations contain a `[Diagram: …]` style description; the diagram crop itself is not stored. That is fine for training the VLM, but the reconstruction stage needs crops (from layout boxes) if the PDF should show the figure, not only describe it.

## Fixed in the pipeline check

- `build_dataset.py` listed pages from `data/processed/` (gitignored), so on a fresh clone it would have written empty training files. It now lists from `data/raw_scans/`.
- The prompt said "LaTeX ($$...$$) for all math", but 336 of 410 labels also use inline `$...$`. The prompt now says `$...$` inline, `$$...$$` display, and `[Diagram: ...]` for figures, matching the labels. JSONL rebuilt.
- `evaluate.py` compared against the copy of the label inside the JSONL, which goes stale when a label is corrected. It now reads `data/annotations/`.
- New `00_dataset/check_dataset.py` checks pairing, split leakage, stale JSONL, near-duplicates and label format in one run.

## Not a problem, but worth knowing

- Blank pages: 1 in train, 1 in val. Harmless.
- Short annotations (`mlt_week07_page010`, 20 characters) are real page fragments from page breaks.
- The tags example `ie643_lec12_page007` uses pixel boxes with the image size; keep that format only for the example. Normalise real tags.

## Suggested order

1. Regenerate `data/processed/` (item 1).
2. Decide the split change (item 2) and re-run `build_dataset.py`.
3. Verify the test labels and the 12 flagged pages (item 4).
4. Box about 20 test pages (item 3) and compute the Surya metric.
