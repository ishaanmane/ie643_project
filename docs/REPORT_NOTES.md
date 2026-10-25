# Notes for the final report

Running list of points the report must mention. Add to it as stages are reviewed.

## Interface (Notes2PDF): limits and extreme cases

Limits are enforced on the server (`06_interface/server.py`, `pipeline.py`); the page checks file
count and total size before uploading, but **not** the number of pages inside a PDF or TIFF.

| Case | What happens | When |
|---|---|---|
| **Under 25 MiB but more than 20 pages** (e.g. one 30-page PDF) | Upload is accepted, then the job stops with "Input exceeds the 20-page limit; split the document." No partial PDF is made. | Right after upload, before any model runs (a few seconds) |
| More than 25 MiB in total | Rejected before upload by the page; the server also rejects it (HTTP 413) | Immediately |
| More than 20 files | Rejected ("Choose at most 20 files") | Immediately |
| 20 pages exactly | Allowed; the slowest normal case (about 6-10 s per page for recognition once models are loaded) | — |
| Empty file, unsupported type (e.g. .docx), or content not matching its extension | Rejected with a message | Immediately / at decoding |
| Password-protected or corrupt PDF | Job error: "Password-protected PDFs are not supported" / "could not be opened" | At decoding |
| Photo above 40 megapixels | Job error asking for a smaller export (protects memory); images up to that are scaled to at most 4000 px | At decoding |
| PDF page larger than 20000 pt | Rejected as invalid | At decoding |
| HEIC/HEIF from iPhone | Supported (pillow-heif); EXIF rotation applied | — |
| Transparent PNG | Transparency becomes white paper, not black | — |
| Blank page | Processed; output is near-empty for that page | — |
| Very dense page | Recognition stops at 2048 tokens; the PDF is still made with a warning that the page may be cut off | Recognition |
| Model writes LaTeX the PDF engine rejects | That equation is shown verbatim with a warning; the rest of the PDF is typeset | Rendering |
| Model output contains file/command TeX (e.g. `\input`) | Job stops for safety; raw prediction kept for review | After recognition |
| Diagram described but no crop found | PDF still made; warning lists the pages; original pages are appended for checking | Rendering |
| Second upload while one is running | Rejected: "Another conversion is running" (one GPU, one job at a time) | Immediately |
| First upload after start or after 15 idle minutes | Extra ~1 min to load both models; later uploads start immediately | — |
| Server restarted during a job | That job is marked failed; upload again | — |
| Results older than 24 h | Deleted automatically | — |
| 50 stored jobs or under 1 GB free disk | New uploads refused until old jobs are deleted | Immediately |
| Wrong access key 8 times in a minute | Sign-in paused for a minute | — |
| Browser session older than 8 h | Must sign in again | — |
| GPU busy with training | Uploads would run out of GPU memory: the interface must be stopped during training | — |

Possible improvement (not done): count PDF pages in the browser before uploading, so a >20-page PDF
is refused before it is sent.

## Data and evaluation (from the dataset review)

- Split by unit: train 303, val 31, test 76. IE802 is one notebook, split by page block
  (41-44 val, 45-56 test); its test pages share the writer with its training pages.
- Test labels were audited page by page against the images (AI-assisted, user-confirmed readings);
  `??` written by the lecturers is kept as content. Three hard readings on IE802 pages 048/049 are
  best readings (`data/TEST_LABEL_AUDIT.md`).
- Few writers overall; scores do not show performance on unseen handwriting.
- The desk-whitening preprocessing rule was designed by looking at pages from all splits (it has
  no learned parameters).
- Surya v2 is used zero-shot, only for figure crops; its weights are licensed for research use.
- Earlier results (old split, 25 val pages) are superseded by the `final_*` runs and must not be
  mixed with them.

## Metrics (see 05_evaluation/README.md)

- Report the standard set: corpus CER and NED (comparable with Nougat / OmniDocBench), token
  precision/recall/F1 (hallucination vs omission), BLEU-4, normalised equation F1 and edit score,
  diagram-count accuracy, heading recall, each with 95% bootstrap intervals over test pages.
- Strict equation match (0.137 on test) understates quality: after LaTeX normalisation equation F1
  is 0.338 and the mean equation edit score 0.703 (final_clean, test). Explain the difference.
- Fine-tuned vs zero-shot (test, NED): fine-tuned better on 74 of 76 pages, difference
  0.284 (95% CI 0.247-0.324).
- CDM (rendered-formula matching) not used: needs its own toolchain; mention as future work.
