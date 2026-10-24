# Handoff: full project context for a new session

Read this first. It records what the project is, how the machines and repo are set up, what is built (with measured results), every non-obvious problem we hit and how it was solved, what is in progress, and what comes next. Detailed results per stage are in `findings/`; run instructions are next to the code (`*/README.md`).

---

## 1. The project

IE643 course project (Team InTra): **turn photos/scans of handwritten lecture notes into clean, structured, searchable PDFs.** Official statement: `docs/PROJECT_STATEMENT.md`. Five deliverables: (1) preprocessing, (2) recognition with a fine-tuned vision-language model, (3) structure/layout understanding, (4) digital reconstruction, (5) PDF generation + quality evaluation. Final submission also needs trained models + code docs, a user interface, metrics, and a stage-wise report.

The user (Akshat) owns preprocessing, dataset, reconstruction, PDF and evaluation; a teammate (Ishaan Mane, repo owner) did the original Sauvola binarisation work.

## 2. Repo, branches, machines

| Item | Value |
|---|---|
| GitHub repo | `ishaanmane/ie643_project` |
| Working branch (everything) | `akshat/dataset-and-preprocessing` (one branch only; `main` is Ishaan's original; a temporary `preds-sync` branch was deleted) |
| Commit identity | `git -c user.name="Akshat" -c user.email="aksh10.at@gmail.com" commit ...` (no global git identity is set on the Mac) |
| Commit trailer | `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` |
| Mac (laptop) | repo at `/Users/akshatmac/Desktop/IE643/ie643_project`; the Claude session's working directory is `/Users/akshatmac/Desktop/IE643/Project643` (older pre-repo folder with the original dataset build; `Project643/rendered_pdfs/` holds PDFs shown to the user) |
| GPU machine | Ubuntu, RTX 5060 Ti 16 GB (Blackwell, compute 12.0), dual-boot with Windows. User has **terminal access only** (no GUI, laptop cannot reach it over the network). Repo at `/home/intralab/workspace/ie643_project` (171 GB workspace partition). An old unused clone at `~/ie643_project` holds a backup adapter copy; do not delete it blindly |
| GPU env | venv `/home/intralab/ie643/.qwen` (Python 3.13, installs with `uv pip`), HF cache `HF_HOME=/home/intralab/workspace/hf_cache`. Session setup: `source /home/intralab/workspace/ie643_env.sh` (deactivates conda base, activates venv, sets HF_HOME, cd to repo) |
| GPU software | torch cu128, transformers 4.57.6, peft 0.21.2, bitsandbytes 0.50.2, pandoc 3.7, TeX Live 2025 (xelatex), DejaVu fonts, gh CLI logged in as `aksh10-at` (can push) |
| Mac software | Python 3.9 system (no torch); Homebrew; `tectonic` (small LaTeX) and `poppler` installed; a scratch venv with transformers 4.57.6 + CPU torch + pypandoc_binary (pandoc 3.9) lives in an old session scratchpad: `/private/tmp/claude-501/-Users-akshatmac-Desktop-IE643-Project643/7f585ea5-d684-4630-8ef2-6f1e5f84f24d/scratchpad/` (`tenv/` venv, `bin/pandoc` symlink). It may be cleaned by the OS; recreate if missing. Mac disk is tight (~10 GB free) |

### Working rules (agreed with the user)

- **Push only when the user says "push".** Commit locally, then say "say push".
- **The GPU folder never switches branch.** Always `git pull` before starting and before pushing (`git pull -q --rebase && git push -q`). Switching branches once deleted untracked-on-this-branch files (`preds/`).
- **Moving files GPU → Mac goes through git**: GPU commits outputs (`preds/`, `logs/`, `results/pdfs/`) and pushes; the Mac pulls and shows them (Read tool for PDFs, SendUserFile to display). No network path between laptop and GPU (scp/http/ssh failed: hostname does not resolve, not on the same network).
- Give the user copy-paste commands with an **Expect:** line after each, and ask for the output; one step at a time when they are doing setup.
- Long GPU runs inside **tmux** (`tmux new -s qwen` / `tmux attach -t qwen`, detach Ctrl-b d). **Ctrl-C in the training pane kills (and once hung) the run.** Short runs (outline, render) do not need tmux.
- The user dislikes doing things twice and prefers building on the GPU and pulling the result.

## 3. Pipeline as built

```
raw scans ──► 01 preprocessing ──► data/processed/ (410 pages)
                                      │
                    02 Surya layout ◄─┤  (all 410 pages, results committed)
                    tags + figure crops
                                      │
                    03 Qwen2.5-VL-7B + LoRA (clean variant) ──► per-page Markdown (preds/)
                                      │
                    04 outline LLM (sections only) + deterministic renderer ──► Markdown ──► pandoc/xelatex ──► PDF
                                      │
                    05 evaluate.py (CER/WER/equations), evaluate_generation.py (blocks kept, sections, ...)
```

## 4. What is done (with numbers)

### 4.1 Dataset (`00_dataset/`, `data/`) — details: `findings/01_dataset.md`
- 410 pages, 4 sources: IE643 chalkboard (205; lecture 2 is low-res 2044x1228, rest 7168x4320), MLT digital ink (129), IE802 notebook (56), HumynLabs CS notes (20). Markdown labels in `data/annotations/<page>.md` (LaTeX `$...$` inline, `$$...$$` display, `[Diagram: ...]` for figures). Labels are AI-written (11 via Gemini, 399 by direct transcription) and **not human-verified**.
- Split **by unit** (lecture/week) to avoid near-duplicate leakage: train 318, val 25 (`lec07`, `week06`), test 55 (`lec03`, `lec09`, `week03`, `week09`); 12 pages with `??` are left out of every split until fixed. `build_dataset.py` (lists from `data/raw_scans/`, so it works on a fresh clone), `check_dataset.py` (0 FAIL, 4 known WARN).
- Leakage: highest 5-gram similarity val/test vs train 0.49 (lecture 08 re-derives backprop equations of 07/09).
- Variants built from the same split: `clean` (`data/*.jsonl`), `boxed` (`data/boxed/*.jsonl`, images `data/processed_boxed/` drawn by `02_layout/draw_boxes.py`).
- **Known gap (open decision):** val and test contain **no notebook-photo pages**.

### 4.2 Preprocessing (`01_preprocessing/`) — details: `findings/02_preprocessing.md`
- Page crop/warp → resize 2000 px → illumination flattening → CLAHE → denoise; deskew off by default.
- Five bugs found **only by looking at images** (summary always said 0 failures): skew estimator rotated ~80% of straight pages; page warp cut off chalkboards (skip if mean brightness < 100); tilted photos (aspect < 0.6 rejected); warps covering only 53-72% of the page (minimum area now 0.8); edge clipping (rectangle grown 2%).
- Final: 55 warped (20 HumynLabs + 35 IE802), 355 content-cropped, 0 failures. **The check number for "corrected images" is 55 warped** (old versions had 80 or 62).
- Reproducible on Kaggle, Mac, GPU (same sizes; pixels differ ≤0.5/255; bytes differ, so never compare hashes across machines).

### 4.3 Layout, Surya v2 (`02_layout/`) — details: `findings/03_layout_surya.md`
- Ran on Kaggle T4 (vLLM server). All 410 corrected pages: 4,283 blocks, 0 errors. Raw output `02_layout/surya_results_all.json`; per-page tags `data/tags_draft/` (boxes normalised 0-1000, reading order, type).
- Surya on preprocessed pages beats raw scans (found margin notes, removed neighbouring-page bleed).

### 4.4 Recognition, fine-tuning (`03_recognition/`) — details: `findings/04_recognition_finetuning.md`
- Qwen2.5-VL-7B-Instruct, 4-bit NF4 QLoRA, bf16, LoRA r16/α32 on q,k,v,o,gate,up,down (47.6M params), 318 pages, 3 epochs (120 steps, batch 1×8), lr 1e-4, answer-only loss (masking tested with the real processor). Script `finetune_qwen25vl.py` (also a notebook); data logic `qwen_data.py`.
- Peak VRAM 13.2 GB, ~62 min per run, 31 s/step.
- Validation (25 pages):

| Fine-tuned | CER | WER | text-only CER | equation exact |
|---|---|---|---|---|
| zero-shot baseline (boxed_json) | 0.712 | 0.927 | 0.892 | 0.061 |
| `boxed_json` (boxes + layout JSON) | 0.287 | 0.469 | 0.258 | 0.273 |
| **`clean` (chosen)** | **0.277** | 0.485 | **0.222** | 0.244 |

- **Decision: `clean`.** The boxed model dropped side notes Surya had not boxed (65% of label length vs 97-98% for clean on those pages), and clean needs no Surya before Qwen.
- Adapters on the GPU machine: `runs/qwen25vl_clean/final_adapter` (+ backups `/home/intralab/workspace/adapter_clean_<date>/`, `~/ie643_project/adapter_clean_<date>/`), same for `boxed_json`. Predictions committed in `preds/` (`base_*_val`, `lora_*_val`), logs in `logs/`.
- Test split **not scored yet** (labels must be checked first).

### 4.5 Reconstruction + PDF (`04_reconstruction/`)
- **`render_document.py` (deterministic, no model):** per unit, pages in order, blocks copied verbatim; each `[Diagram: ...]` matched to a Surya figure by order-preserving position alignment; over-split Surya figures merged (closest pair first, stop when counts match); unmatched descriptions stay as text; extra drawings added if ≥3% of page; chalkboard crops grayscale-inverted; figures numbered, centred, ≤55% width / 30% height, pinned with `float` `[H]` (otherwise LaTeX moves them); equations checked exactly with xelatex (or tectonic on the Mac) and failing ones shown verbatim with a plain-text warning (never altered); long verbatim lines wrap (fvextra); DejaVu font if present; **reports blocks kept (must be N/N)**.
  - All 42 units with labels: 227/243 diagrams matched (93%), 2,739 equations.
- **`outline.py` (LLM structure only):** Qwen2.5-VL-7B text-only, zero-shot, greedy. Model sees `id | type | first words`, returns section starts/levels. Validation in code: ids exist and increase; levels 1-2; **if a section starts on a heading, the notes' exact heading text is used**; otherwise title words must occur in the notes, else the section break is dropped; repeated consecutive titles merged; outline rejected if more invalid than valid sections (page order then). Parser accepts `{"sections": [...]}` or a bare list, with or without ```json fences; strips `#` from titles; model loaded once.
- Results on val units with model predictions (GPU): lecture 7 15 sections, **91/91 blocks kept**; week 6 5 sections, 37/37; PDFs in `results/pdfs/*_model_outline.pdf`.

### 4.6 Evaluation (`05_evaluation/evaluate.py`)
- CER, WER, text-only CER (math and diagram lines removed), equation exact match; per-page capped at 1.0; references read from `data/annotations/`.

### 4.7 Documentation
- `findings/` (one file per stage + open items), `docs/PIPELINE.md`, `docs/PIPELINE_TO_OCR.md`, `docs/DATASET_AUDIT.md`, stage READMEs.

## 5. Intricacies discovered (read before changing anything)

**Data and preprocessing**
- Look at images, not only summary counts; three preprocessing bugs passed "0 failures".
- Tags must match the exact image Surya saw: `surya_to_tags.py` and `draw_boxes.py` refuse when sizes differ. Check `preprocess_report.csv`: 55 warped = corrected version.
- `data/processed/`, `data/processed_boxed/`, `data/crops/`, `out/` are gitignored and rebuilt per machine (`batch_preprocess.py --workers 8 --force` ~5-8 min, then `draw_boxes.py`).

**Kaggle / Surya**
- Python 3.13 on Kaggle broke `numba`; use uv venvs with Python 3.11. Installing vllm + surya together made the resolver pick vllm 0.1.2: use two venvs. vLLM OOM at start on T4: `--dtype half --limit-mm-per-prompt '{"video": 0}' --max-num-batched-tokens 8192 --enforce-eager`. `pkill -f 'vllm serve'` kills its own shell; kill by GPU pid. `zip` appends to existing archives (`rm -f` first). `git clone` into an existing folder fails silently (old code). Kaggle pins dataset versions. Updating a dataset input restarts the session.

**Fine-tuning**
- The Ollama copy of Qwen cannot be trained; use HF weights.
- `prepare_model_for_kbit_training` wastes ~2 GB VRAM (fp32 upcast); use gradient checkpointing + `enable_input_require_grads`. Generation after training needs `use_cache=True`.
- Pre-resize images to multiples of 28 within the pixel budget so the processor does not resize again (box coordinates then line up).
- Free GPU from Ollama: `ollama stop qwen2.5vl:7b`.

**Rendering / outline**
- Relative `--out` broke pandoc (it runs inside the output folder); fixed with abspath.
- The approximate math check (pandoc parser) misses LaTeX errors (model wrote `&` inside `\text{}`); exact check needs xelatex/tectonic.
- Tectonic stops at the first error; the checker removes the failing equation and retries.
- Inverting a green chalkboard in colour gives pink; grayscale first.
- The model ignores format instructions sometimes (bare list, `#` in titles, a section per page); never trust its output, validate it.
- Model titles differing only in case from the notes' heading lost content (89/91); headings now keep the notes' wording.

**Workflow**
- Laptop cannot reach the GPU machine; transfer via git only. `gh auth login --web` with device code worked for the GPU machine.

## 6. In progress right now

Step 1 of "improve generation": **measure the generator on all 42 units** (labels as input, so it measures the generator, not extraction).
- `04_reconstruction/evaluate_generation.py`: **written, not yet tested, not committed.** Summarises render reports + outlines: blocks kept, sections, outlines used/rejected, titles dropped, repeats merged, equations failed, figures matched, PDFs built.
- `04_reconstruction/outline.py`: an `--all` option was added (**uncommitted, untested**).
- Next action: test locally with `--mock` (`outline.py --all --mock --out <dir>`, render `--all --outlines <dir> --format md`, then `evaluate_generation.py`), commit, push on request, then on the GPU:
  ```bash
  python3 04_reconstruction/outline.py --all --out out/outlines_all
  python3 04_reconstruction/render_document.py --all --outlines out/outlines_all --out out/documents_all
  python3 04_reconstruction/evaluate_generation.py --docs out/documents_all --outlines out/outlines_all --md results/generation_eval.md
  ```
  then commit `results/generation_eval.md` (+ a few PDFs) and push. Watch the IE802 unit (56 pages, ~700 blocks: long prompt; max_new_tokens 1536 may be tight).

## 7. Next steps (agreed order)

1. Generation measurement (above), then record in `findings/`.
2. Flag uncertain extraction: compare the model's text with Surya's own OCR per block/page (needs a Surya OCR run on Kaggle or the GPU machine); mark disagreeing blocks in the PDF.
3. Cosmetic: attach short label lines next to a figure into its caption ("NP-hard", "local minimum" appear as stray lines); merge sentences split across pages; mark repeated recap content.
4. Later: inference path for new uploads (preprocess → Qwen clean adapter → Surya for figures → outline → render), user interface, layout metric (hand-checked tags on ~20 pages), test-split scoring after label checks, report.

## 8. Open decisions / user tasks
- Hold out notebook-photo pages for val/test (needs code change: IE802 is one unit) or keep the split and note it.
- Fix the 12 `??` pages; check the 55 test labels by hand (`data/VERIFICATION.md`).
- Revoke the Gemini API key pasted in chat early in the project.
