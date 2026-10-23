# External Equation Datasets: Contingency Plan

Status: not used yet. This is a fallback, not part of the current 205-page dataset.

## When to use this

Our 205 pages give the model page-level structure (headings, bullets, diagrams) but limited equation variety, since equations appear mixed in with everything else on a board. **Trigger:** after fine-tuning on our own data and evaluating on the test split, if the equation exact-match rate or CER on equation spans is poor, add one or more of the datasets below and retrain, rather than trying to fix it by relabeling our own pages.

This is not a guess. **Uni-MuMER** (NeurIPS 2025 Spotlight) fine-tunes Qwen2.5-VL-3B for handwritten equation recognition on exactly this kind of mix — CROHME, HME100K, MathWriting, and Im2LaTeX — and reports that each dataset added on top of the others improved accuracy further. Same base model family as ours, same idea: use public equation data to boost equation recognition without touching the model architecture.

## Candidate datasets

| Dataset | Size | Raw label format | Images ready? | Licence | Priority |
|---|---|---|---|---|---|
| [MathWriting](https://github.com/google-research/google-research/blob/master/mathwriting/README.md) | 230K human-written + 400K synthetic | InkML (pen strokes) + LaTeX | No — must render strokes to an image | CC BY-NC-SA 4.0 (non-commercial; fine for coursework) | 1st |
| [CROHME 2019](https://tc11.cvc.uab.es/datasets/ICDAR2019-CROHME-TDF_1) | ~8.8K train / 1.2K test | InkML + LaTeX/MathML | No — must render | Research use | 2nd (also the standard benchmark, useful for reporting comparable numbers) |
| HME100K | 74,502 train / 24,607 test | Pre-rendered image + LaTeX | Yes | Research use | 3rd |
| [Im2LaTeX-100K-Handwritten](https://im2markup.yuntiandeng.com/data/) | ~100K | Pre-rendered image + LaTeX | Yes | Open | 4th, if more volume is needed |
| [Aida Calculus](https://www.kaggle.com/datasets/aidapearson/ocr-data) | 100K synthetic | Pre-rendered image + LaTeX (+ char boxes) | Yes | Open | Optional, lowest priority — synthetic and visually too clean |
| Tex80M (2026, TexTeller) | 80M+ | Mostly printed/typeset formulas | Yes | Not yet checked | Not recommended — built for printed formulas at massive scale, far beyond what a course project needs or can afford to train on |

Recommendation: start with a 5,000–10,000 sample subset of MathWriting, add CROHME if more is needed. Don't pull the full multi-hundred-thousand-sample sets — Kaggle's free GPU hours and storage don't support that, and Uni-MuMER's own result curve shows most of the gain comes from the first dataset added, not from maximum volume.

## How we'd actually use one (integration steps)

1. **Download** the chosen dataset (MathWriting first).
2. **Get an image per sample.**
   - InkML datasets (MathWriting, CROHME): the raw data is pen-stroke coordinates, not an image. Write a converter script that plots the strokes (matplotlib) and saves a PNG — this is a well-known step, commonly done with a script like Harold Mouchère's `convertInkmlToImg.py` used for CROHME, which we'd adapt.
   - Pre-rendered datasets (HME100K, Im2LaTeX, Aida): already images, no conversion needed.
3. **Extract the LaTeX label** from the InkML `<annotation type="truth">` tag or the dataset's accompanying label file.
4. **Wrap into our JSONL schema**, but with a *different, equation-only prompt* — not our page-level prompt, since these are single cropped equations, not full lecture pages:
   ```json
   {"messages": [
     {"role": "user", "content": [
       {"type": "image", "image": "external/mathwriting/sample_00123.png"},
       {"type": "text", "text": "Convert this handwritten mathematical expression to LaTeX."}
     ]},
     {"role": "assistant", "content": "$$\\frac{\\partial e}{\\partial w} = \\nabla_w E$$"}
   ]}
   ```
5. **Combine with our own data as a second training task, not a replacement.** Train on both our 205-page dataset (page-level prompt) and the external equation crops (equation-only prompt) together, in the same fine-tuning run — this is what Uni-MuMER calls multi-task fine-tuning, and it's why the two prompts need to stay distinct: the model learns "when asked for the whole page, do structure + equations; when asked for a single equation, just transcribe it," rather than getting confused about what a training example should look like.
6. **Keep external data a minority of the mix.** Cap it, e.g. external samples ≤ our own page count, so the model doesn't drift toward treating every input as an isolated equation crop and lose the page-structure skill.
7. Build this as `00_dataset/build_external_dataset.py`, separate from `00_dataset/build_dataset.py`, so the external data is always an explicit opt-in and never silently mixed into our core 205-page dataset. The report should describe our data and any external data as two clearly separate sources.

## Caveats

- **Domain mismatch.** These datasets are clean, isolated equation images (synthetic or scanned symbol-by-symbol), not equations embedded in a messy lecture-board photo. They help the model's LaTeX vocabulary and symbol recognition, but won't teach it anything about reading equations *in context* on a real board — that only comes from our own data.
- **Licensing.** MathWriting is non-commercial (fine here); cite datasets used, in the report's references.
- **Compute cost.** Even a small InkML-to-image conversion pass and extra fine-tuning epochs cost Kaggle GPU time, which is limited per week — factor this into the schedule if the trigger condition is hit close to a deadline.

## Decision so far

Not triggered. Do the baseline and fine-tuning on our own 205 pages first (see `PIPELINE.md`, phases B–C); come back to this file only if equation metrics on the test split are weak.
