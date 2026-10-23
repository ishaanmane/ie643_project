# Handwritten Notes to Digital PDF: Pipeline and Project Status

Last updated: 2026-09-22

This document lists every step of the project: what the final system does, what is already done, and what remains. Status labels: **Done**, **In progress**, **To do**.

Related files: [PROJECT_STATEMENT.md](PROJECT_STATEMENT.md) (official task), [FINAL_IMPLEMENTATION_PLAN.md](FINAL_IMPLEMENTATION_PLAN.md) (original plan), [data/README.md](data/README.md) (dataset notes), [data/VERIFICATION.md](data/VERIFICATION.md) (manual-check checklist), [data/EXTERNAL_DATASETS.md](data/EXTERNAL_DATASETS.md) (equation-dataset contingency plan).

---

## 1. Goal

Given scanned or photographed handwritten lecture notes, produce a clean, structured, searchable PDF that keeps the text, equations, diagrams and page structure, together with an editable source file.

Deliverables required by the project statement:

| # | Pipeline deliverable | Where it is covered here |
|---|---|---|
| 1 | Preprocessing: enhancement, noise removal, skew correction, page segmentation, layout analysis | Run-time stages 1 and 2 |
| 2 | Content recognition with a fine-tuned vision-language model (text, equations, symbols, tables) | Run-time stage 3 |
| 3 | Structure and layout understanding (headings, bullets, equations, diagrams) | Stages 2 and 3 |
| 4 | Digital note reconstruction (clean, well-formatted pages) | Run-time stage 4 |
| 5 | PDF generation and quality evaluation | Run-time stages 5 and 6 |

Final submission: trained models with documented code, an upload interface, quantitative and qualitative results, a stage-wise report, and everything done by the intensive assessment (date to be confirmed with the TAs).

---

## 2. The pipeline at a glance

```
RUN TIME (a user uploads pages)

scan/photo -> 1 Preprocess -> 2 Layout detection (diagram boxes) ---+
                  |                                                  |
                  +--> 3 VLM recognition -> Markdown + [Diagram: ...] tags
                                                                     |
                       4 Reconstruction  <---------------------------+
                       (merge pages, clean, validate LaTeX, insert diagram crops)
                                   |
                       5 PDF generation (Pandoc + XeLaTeX) + editable .md
                                   |
                       6 Evaluation (test-set metrics + side-by-side grid)


BUILD TIME (how we get the model)

PDFs -> render -> preprocess -> label -> verify -> split by lecture
     -> zero-shot baseline -> LoRA fine-tune (Kaggle) -> evaluate on test -> package
```

---

## 3. Run-time pipeline (what happens to an upload)

| Stage | Input | Output | Tool | Status | File |
|---|---|---|---|---|---|
| 1. Preprocess | Page image | Cleaned colour image, 2000 px long edge | OpenCV | **Done** | `src/preprocess.py` |
| 2. Layout detection | Cleaned image | Figure boxes and reading order | Surya | **To do** (untested on chalkboard) | `src/layout.py` |
| 3. Recognition | Cleaned image + fixed prompt | Markdown with LaTeX and `[Diagram: ...]` tags | Qwen2.5-VL + LoRA | **To do** | `src/recognize.py` |
| 4. Reconstruction | Per-page Markdown + diagram crops | One cleaned Markdown document | Python | **To do** | `src/postprocess.py` |
| 5. PDF generation | Cleaned Markdown | Searchable PDF + editable `.md` + crops | Pandoc + XeLaTeX | **To do** | `src/pdf_gen.py` |
| 6. Evaluation | Predictions + reference Markdown | Metric scores | jiwer, sacrebleu, custom | **To do** | `src/evaluate.py` |

### Stage 1: Preprocess (done)

Cleans the image before the model sees it.

1. **Border removal.** Otsu threshold, then crop to the content.
2. **Skew correction.** Estimate the tilt of the writing (`minAreaRect`) and rotate the page straight. Angles under 0.5 or over 20 degrees are ignored.
3. **Contrast enhancement (CLAHE).** Local contrast equalization on the lightness channel only, so faint chalk strokes stand out and colours are kept.
4. **Denoising.** Non-local means removes speckle and compression noise.
5. **Resolution normalization.** Resize so the longest side is 2000 px.

The output is deliberately **not binarized**. A vision-language model can use shading and colour, and binarizing throws them away. `binarize()` exists only as a debug view.

On the current chalkboard photos most steps change little because the images are already tight and straight. They matter more for phone scans of paper.

### Stage 2: Layout detection (to do)

- Detect figure and table regions and reading order so diagrams can be cropped for the PDF.
- Surya is the planned tool. It was built mostly for printed documents, so it must be tested on chalkboard pages first. The plan's example code may not match the current Surya API, so check its documentation.
- Fallback if Surya fails: have the model output bounding boxes, which requires box labels.

### Stage 3: Recognition (to do)

- The model receives the page image plus the fixed instruction prompt. The prompt must be identical to the training prompt (`PROMPT` in `scripts/build_dataset.py`).
- It outputs Markdown with LaTeX for equations. Wherever a diagram appears, it writes a one-line tag: `[Diagram: <caption>]`. Text and equations inside the diagram are written out so they stay searchable.
- Pages are processed one at a time and merged in stage 4.
- Runs on a GPU (Kaggle) or slowly on CPU (kanjur).

### Stage 4: Reconstruction (to do)

- Merge pages and normalize heading levels and bullet styles.
- Validate LaTeX (balanced delimiters, ideally a test compile of each equation). A failing equation falls back to plain text so one bad `$` cannot break the whole PDF.
- Match the k-th diagram tag to the k-th detected figure in reading order, save the crop, and replace the tag with the image plus caption. If the counts differ, show the caption only.
- Do **not** reuse the plan's original cleanup code as written. Its regex that turns single newlines into spaces would flatten lists, tables and equation blocks, and its blind `l`/`1` and `O`/`0` swaps would corrupt math.
- The project statement says to "develop/finetune a model" for reconstruction. Our single fine-tuned model produces structured Markdown, so it covers recognition, structure and reconstruction in one pass. State this explicitly in the report, or add a small learned cleanup step.

### Stage 5: PDF generation (to do)

- Pandoc converts Markdown to LaTeX and XeLaTeX renders the PDF. LaTeX gives the best math typesetting, XeLaTeX handles Unicode symbols and fonts, and the PDF text is selectable, so it is searchable.
- Exports: the PDF, the editable `.md`, and the diagram crops.
- Compile errors are caught and reported. Alternatives if TeX is hard to install: HTML with KaTeX (WeasyPrint) or Typst.

### Stage 6: Evaluation (to do)

Run on the test pages. Scores are computed on normalized text with diagram tags stripped.

| Metric | Measures | Note |
|---|---|---|
| CER, WER (`jiwer`) | Character and word edit distance | Standard for handwriting and OCR |
| BLEU (`sacrebleu`) | N-gram overlap | Secondary; comes from machine translation and is weak for math |
| Equation exact-match rate | Share of equations identical after LaTeX normalization | Standard for handwritten math (CROHME) |
| LaTeX compile rate | Share of equations and PDFs that compile | Catches broken output |
| Heading and block-type accuracy | Structure preserved | Covers the "structure" deliverable |
| Diagram detection overlap | Crop boxes vs reference | Only if we crop with Surya or model boxes |
| Qualitative grid | Scan, Markdown, PDF side by side for 10+ pages | Required by the statement |

SSIM (rendered-image similarity) from the original plan is dropped: one line shift wrecks the score. The plan's numeric targets (for example CER under 8%) are guesses, not validated numbers.

---

## 4. Build-time pipeline (how we get the model)

### Phase A: Dataset (mostly done)

| Step | What | Status | Code |
|---|---|---|---|
| A1 | Render every page of every source PDF to images (PyMuPDF, 4x zoom) | **Done** (410 pages, 4 sources) | `scripts/render_pages.py`, `scripts/render_mlt_pages.py`, `scripts/render_ie802_pages.py` |
| A2 | Preprocess all pages | **Done** | `scripts/batch_preprocess.py` |
| A3 | Generate ground-truth Markdown for every page | **Done** (unverified) | `scripts/annotate_gemini.py`, plus direct Claude transcription |
| A4 | Build train/val/test JSONL files by unit, plus splits file and checklist | **Done** | `scripts/build_dataset.py` |
| A5 | Manually verify labels | **In progress** (you) | see `data/VERIFICATION.md` |
| A6 | Shorten diagram tags to one line and list in-diagram text | **To do** | one-off script plus a manual pass |
| A7 | Add diversity: notebook-paper scans and other people's handwriting | **Done** | see `data/README.md` — 4 sources now (chalkboard, digital ink, notebook paper x2) |

Dataset facts:

- Four sources feed the dataset, told apart by filename prefix — see `data/README.md` for the full table:
  - `ie643_*`: `Class Scribes/`, 11 PDFs (Lec02 to Lec12), 205 pages of chalkboard photos. Lec02 to Lec04 have low native resolution (about 511x307 px pages, upscaled).
  - `mlt_*`: `MLT Notes/`, 10 PDFs (Week01 to Week10), 129 pages of digital stylus ink (multi-colour, clean background) — a genuinely different course and medium.
  - `ie802_*`: a 56-page IE802-MINLO notebook (one continuous PDF), real notebook-paper photos. Exposed a real preprocessing gap: Otsu-based border crop only partially removes desk background when the background is bright — flagged in `data/README.md`, not yet fixed.
  - `hlcs_*`: `HumynLabs/Handwritten-Computer-Science-Notes-Dataset` on Hugging Face, 20 pages of real notebook-paper photos, downloaded via `huggingface_hub` (no ground truth included upstream, labeled the same way as the rest).
- Labels: **11** pages from the Gemini API (`gemini-3.6-flash`; the free tier allowed only 20 requests per day), and **194** pages written by Claude reading each image. All are AI-generated and unverified. State both methods in the report.
- A spot check of 2 early pages found one small error (fixed), so more exist.
- Split **by lecture**, because neighbouring board pages repeat the same equations and a random split would leak near-duplicates into val and test.

| Split | Lectures | Pages |
|---|---|---|
| train | 02, 04, 05, 06, 08, 10, 11, 12 | 151 |
| val | 07 | 20 |
| test | 03, 09 | 34 |

- 11 pages are flagged with `??` where the board was hard to read. Fix them and remove the marks; re-running `scripts/build_dataset.py` updates the checklist and JSONL files.

To rebuild from scratch, run from the project root:

```bash
python3 scripts/render_pages.py
python3 scripts/batch_preprocess.py
# labels -> data/annotations/*.md
python3 scripts/build_dataset.py
```

### Phase B: Evaluation code and baseline (to do)

| Step | What | Status |
|---|---|---|
| B1 | Write `src/evaluate.py` with the metrics in stage 6 | **To do** |
| B2 | Test Surya on about 5 diagram pages | **To do** |
| B3 | Zero-shot bake-off on the val pages: Qwen2.5-VL vs 1 or 2 other open VLMs (check for newer releases), plus TrOCR as a baseline | **To do** |
| B4 | Record the baseline scores. This is the "before" number and the model-selection experiment for the report | **To do** |

### Phase C: Fine-tuning (to do)

| Step | What | Status |
|---|---|---|
| C1 | Choose model size (7B or 3B) and an image size cap that fit a free Kaggle T4 | **To do** |
| C2 | LoRA fine-tune in 4-bit on `train.jsonl`, using val for tuning and early stopping | **To do** |
| C3 | Save the adapter (about 100 MB) and its config | **To do** |
| C4 | Evaluate on the test split and compare with the baseline | **To do** (needs verified test labels) |
| C5 | If equation recognition is weak on the test split, add public handwritten-equation data (MathWriting, CROHME, ...) and retrain — plan in `data/EXTERNAL_DATASETS.md` | **Contingency, not started** |

Notebooks: `notebooks/02_qwen_finetuning.ipynb` (Kaggle), `notebooks/03_evaluation.ipynb`.

### Phase D: Build the remaining pipeline code (to do)

| Step | File |
|---|---|
| D1 | `src/layout.py` (Surya wrapper) |
| D2 | `src/recognize.py` (load adapter, run inference) |
| D3 | `src/postprocess.py` (stage 4) |
| D4 | `src/pdf_gen.py` (stage 5) |
| D5 | `src/pipeline.py` (end-to-end orchestrator) |
| D6 | `app/gradio_app.py` (upload, convert, download PDF and `.md`, show metrics) |

### Phase E: Finish (to do)

| Step | What |
|---|---|
| E1 | Qualitative grid of 10+ pages |
| E2 | Confirm with the TAs that a Gradio interface is acceptable |
| E3 | Stage-wise report: reasons for each step, experiments, datasets and how they were extracted, interface method |
| E4 | Package: adapter, code, README with dependencies, `requirements.txt` |
| E5 | Confirm the intensive-assessment date and plan the schedule (see `FINAL_IMPLEMENTATION_PLAN.md`, section 7) |

---

## 5. Design decisions and why

| Decision | Reason |
|---|---|
| Qwen2.5-VL-7B + LoRA | Open weights (the statement requires a fine-tuned model), strong document/OCR/formula results in its report, fits a T4 in 4-bit, good tooling. Alternatives: other open VLMs, OCR-specialised models, a classical OCR pipeline, closed APIs. See the bake-off in phase B. |
| Markdown with LaTeX as the target format | Compact, editable, easy for the model (lots of Markdown and LaTeX in pretraining), and Pandoc converts it to PDF, HTML or DOCX. JSON needs escaped backslashes and is token-heavy. Raw LaTeX is fragile: one error breaks compilation. |
| Markdown limits and the hybrid fix | Markdown loses position, colour and the 2D layout of a board. Diagram tags can carry coordinates, for example `[Diagram bbox=(x1,y1,x2,y2): caption]`, and JSON can be built from the output later if needed. |
| Diagrams: crop plus caption | The statement requires preserving diagrams, so the original crop goes in the PDF. A short caption adds searchable text. Redrawing diagrams as vector code (TikZ, SVG) is a stretch goal only. The model cannot generate pixels. |
| No binarization | Keeps shading and colour that the VLM can use. |
| Split by lecture | Avoids near-duplicate leakage between splits. |
| Pandoc + XeLaTeX | Best math rendering, Unicode support, searchable text. |
| CER/WER, exact-match equations, no SSIM | Standard metrics for handwriting and math. SSIM is fragile to small shifts. |

---

## 6. Risks and open questions

- **GPU memory.** 2000 px images become thousands of image tokens each, which is tight on a free T4 with the 7B model. We may cap image size or use the 3B model.
- **Surya on chalkboard.** Unverified. If it fails, use model-predicted boxes.
- **Label quality.** All labels are AI-generated. Test results are only meaningful once the test labels are verified.
- **Diversity added but still limited.** Four sources now (chalkboard, digital ink, notebook paper x2), but each is still a single writer/course — no confirmation yet that this generalizes further.
- **Preprocessing gap on real messy photos.** The IE802 pages showed border-crop under-performing when desk background is bright — worth a fix before trusting preprocessing on more real-world scans.
- **LaTeX errors.** Model output can break compilation. Validation and fallbacks are required in stages 4 and 5.
- **TeX installation.** Pandoc and XeLaTeX must be installed on kanjur.
- **Compute limits.** Kaggle GPU hours are limited per week.
- **Model choice.** A newer Qwen release or another model may beat Qwen2.5-VL. Decide by measurement.

---

## 7. Repository layout

Existing:

```
Project643/
  PROJECT_STATEMENT.md   PIPELINE.md   FINAL_IMPLEMENTATION_PLAN.md
  data/
    raw_scans/  processed/  annotations/
    train.jsonl  val.jsonl  test.jsonl  splits.json
    README.md  VERIFICATION.md
  scripts/  render_pages.py  batch_preprocess.py  annotate_gemini.py  build_dataset.py
  src/      preprocess.py
```

Planned: `src/layout.py`, `src/recognize.py`, `src/postprocess.py`, `src/pdf_gen.py`, `src/evaluate.py`, `src/pipeline.py`, `app/gradio_app.py`, `notebooks/`, `models/qwen_lora_adapter/`, `requirements.txt`.

---

## 8. Ordered to-do list

Do these in order. Items marked (you) need you.

- [ ] (you) Verify the flagged pages (12 as of this writing), all 60 test pages, and at least 5 val pages (`data/VERIFICATION.md`)
- [ ] Write `src/evaluate.py` (B1)
- [ ] Test Surya on about 5 diagram pages (B2)
- [ ] Shorten diagram tags in the labels (A6)
- [ ] Run the zero-shot bake-off and record baseline scores (B3, B4)
- [ ] Decide model size and image cap, then fine-tune on Kaggle (C1 to C3)
- [ ] Evaluate on the test split (C4)
- [ ] Build `layout.py`, `recognize.py`, `postprocess.py`, `pdf_gen.py`, `pipeline.py` (D1 to D5)
- [ ] Build the Gradio app (D6) and check with the TAs (E2)
- [ ] Qualitative grid, report, packaging (E1, E3, E4)
- [ ] Confirm the intensive-assessment date and set the schedule (E5)

## 9. Reminders

- Verify the flagged pages (list in `data/VERIFICATION.md`).
- Map the plan to the project statement (the traceability table in section 1 is a start).
- Revoke the Gemini API key that was pasted into chat and create a new one if needed.
