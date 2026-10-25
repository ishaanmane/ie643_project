# Pipeline up to OCR: runbook

Everything that happens before Qwen reads a page. Two uses of the same stages:
**(A) building the dataset** (our 410 pages) and **(B) a new input** (a user's PDF or photo).
Run all commands from the repo root.

| Stage | Script | Needs GPU | Tested |
|---|---|---|---|
| 0. Input to page images | `00_dataset/pdf_to_images.py` | no | yes (PDF of 15 pages, single image) |
| 1. Preprocess | `01_preprocessing/batch_preprocess.py` | no | yes (410 pages before the crop fixes; fixes checked on 11 pages) |
| 2. Layout detection | Surya (`surya_layout`) with a vLLM server | yes | yes, 10 pages on Kaggle T4 |
| 3. Layout to tags + figure crops | `02_layout/surya_to_tags.py` | no | yes, on the 10 Surya pages |
| 4. Dataset finalisation | `00_dataset/build_dataset.py` + manual checks | no | script yes; manual work not done |
| 5. Hand-off to OCR | `data/*.jsonl` (page image + fixed prompt) | - | - |

## Corrections to the earlier plan

1. Surya runs on **preprocessed** pages, not raw scans. On the 10-page test this found the margin notes it missed on raw scans and removed the neighbouring-page bleed (`02_layout/experiments/SURYA_FINDINGS.md`).
2. The full preprocessing must be **re-run on the fixed code** before Surya is run on all pages. The only full run predates the two page-crop fixes.
3. Boxes are stored **normalised to 0-1000**, and figure crops are cut from **exactly the image Surya saw**. Preprocessing crops the page, so boxes from a processed image cannot be mapped onto the raw scan; the converter refuses to crop if the sizes differ.
4. Surya output goes to `data/tags_draft/` (unverified). Only hand-checked pages go to `data/tags/`.
5. The split decision (notebook pages in test) comes **before** rebuilding the JSONL and before any fine-tuning.
6. Deskew stays off (measured: it rotated straight pages and fails on chalkboards).

## Stage 0: input to page images

(A) Dataset: nothing to do; `data/raw_scans/` (410 pages) is in the repo. The `00_dataset/render_*.py` scripts recreate it from the original PDFs, which are not in the repo.

(B) New input:
```bash
python3 00_dataset/pdf_to_images.py notes.pdf --out input_pages/            # PDF, 3x zoom
python3 00_dataset/pdf_to_images.py photo.jpg --out input_pages/            # single photo
python3 00_dataset/pdf_to_images.py scans/ --out input_pages/ --prefix mine # folder of PDFs/images
```
Output: `<prefix>_pageNNN.jpg`.

## Stage 1: preprocessing

```bash
# smoke test, 15 seconds
python3 01_preprocessing/batch_preprocess.py --sample 16 --out /tmp/pp_test --force --workers 4
# (A) all 410 pages -> data/processed/ + preprocess_report.csv, about 7-8 minutes on 4 cores
python3 01_preprocessing/batch_preprocess.py --workers 4 --force
# (B) a new input
python3 01_preprocessing/batch_preprocess.py --raw input_pages --out input_processed --workers 4 --force
# visual check, raw | processed side by side
python3 01_preprocessing/compare_sheet.py --out data/processed --max 30
```
Steps per page: page crop (perspective warp for photos, content crop otherwise), resize to 2000 px, illumination flattening, CLAHE, denoise. Details and measurements: `01_preprocessing/README.md`.

Check after (A), reading `data/processed/preprocess_report.csv`: 410 rows, 0 failures; `ie643_*` all `brightness` (no `quad`), `mlt_*` all `brightness`, `hlcs_*` all `quad`, `ie802_*` mostly `quad`. Expected about 42 `quad` for IE802 (predicted from the 11-page check, not yet seen on the full set).

## Stage 2: layout detection with Surya (Kaggle, GPU T4, Internet On)

Setup, server and why each flag is there: `02_layout/README.md`. In short:
1. Create two Python 3.11 environments, `venv_vllm` (vLLM) and `venv_surya` (surya-ocr). Never install them together.
2. Start `vllm serve datalab-to/surya-ocr-2` with `--dtype half --limit-mm-per-prompt '{"video": 0}' --max-num-batched-tokens 8192 --enforce-eager`.
3. Run Surya on a folder that contains only the page images:
```python
import os, glob
os.makedirs("surya_in_all", exist_ok=True)
for f in glob.glob("data/processed/*.jpg"):
    dst = os.path.join("surya_in_all", os.path.basename(f))
    if not os.path.exists(dst): os.symlink(os.path.abspath(f), dst)
os.environ["SURYA_INFERENCE_BACKEND"] = "vllm"
os.environ["SURYA_INFERENCE_URL"] = "http://localhost:8000/v1"
!/kaggle/working/venv_surya/bin/surya_layout surya_in_all --output_dir surya_out_all
```
Time for 410 pages has not been measured; run on 20 pages first (a folder with 20 links) to time it. Add `--images` only for small folders, since it writes one overlay per page.

Output: `surya_out_all/surya_in_all/results.json`. Download it; it is the only Stage 2 file the later stages need.

## Stage 3: layout to tags and figure crops (no GPU)

```bash
python3 02_layout/surya_to_tags.py --results surya_out_all/surya_in_all/results.json --images data/processed
```
Output per page:
- `data/tags_draft/<page>.json`: blocks in reading order, each with `type` (text, equation, heading, list, caption, table, figure, page_header, page_footer…), `surya_label`, `bbox` (0-1000), `skip_in_text` (true for headers and footers), `text_preview` (empty, for manual filling) and `crop` for figures and tables.
- `data/crops/<page>_bN.png`: the figure and table crops for the PDF. Gitignored; rerun the converter to regenerate them.

Checked: on the 10 test pages it gives 128 blocks and 5 crops (neuron diagram, circle sketch, compile-flow figure and two more), and pointing it at raw scans instead writes no crops and warns.

## Stage 3b: boxed variant (for the clean-vs-boxed comparison)

```bash
python3 02_layout/experiments/draw_boxes.py                        # data/processed + data/tags_draft -> data/processed_boxed/
python3 00_dataset/build_dataset.py --variant boxed    # -> data/boxed/{train,val,test}.jsonl, same pages and splits
```
Thin cyan boxes (3 px on a 2000 px page), a colour none of our inks use. The boxed files use `BOXED_PROMPT`, which tells the model the boxes are hints and to transcribe everything, including content outside the boxes (Surya misses some). Pages without Surya tags are copied without boxes and reported; the builder warns if any are left. The clean files (`data/*.jsonl`) are not touched. A model trained on the boxed set needs Surya and `draw_boxes.py` on every input at inference time too.

## Stage 4: dataset finalisation (A only)

1. **Decide the split.** Currently no notebook-photo pages are in val or test. Option: move a block of IE802 pages and a few HumynLabs notes into test (`HELD_OUT` in `00_dataset/build_dataset.py`).
2. **Rebuild** the JSONL, split file and checklist: `python3 00_dataset/build_dataset.py`. Pages still containing `??` are left out of every split until fixed. Then run `python3 00_dataset/check_dataset.py`: it must end with `0 FAIL` (current state: 0 FAIL, 4 WARN, the warnings being the 12 left-out pages, no notebook pages in val/test, and the `??` count).
3. **Check labels by hand** (`data/VERIFICATION.md`): the 12 flagged pages, all test pages, a val sample. Edit `data/annotations/*.md`, then rebuild again.
4. **Check layout boxes for about 20 test pages:** correct `data/tags_draft/<page>.json` (boxes, types, order), fill `text_preview`, and move the file to `data/tags/`.
5. **Layout metric:** box overlap (IoU / mAP) and reading-order agreement between Surya's draft and the checked tags. Script not written yet.

## Stage 5: hand-off to OCR

What Qwen gets (both A and B): the preprocessed page image and the fixed prompt in `00_dataset/prompts.py` (inline `$...$`, display `$$...$$`, `[Diagram: ...]`, matching the labels). Checked: all 398 split pages load through `03_recognition/common.py`, about 1270 visual tokens each at the default 1,000,000-pixel budget, longest label about 570 tokens. For training these pairs are in `data/train.jsonl` / `val.jsonl` / `test.jsonl`.

What the stages after OCR get from here: reading order and block types from the tags, and the figure crops, so the final PDF can show figures instead of only describing them.

Not built yet: one command that chains stages 0-3 for a new input (the Surya server makes that a GPU-side job), and the layout metric script.
