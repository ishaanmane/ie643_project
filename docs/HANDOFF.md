# START HERE — IE643 project handoff

Updated 2026-10-25, Asia/Kolkata, after the 12:15 GPU memory check and automatic-upload PDF review. Submission was due **today** according to the user. Current implementation commit: `540208d`; this documentation snapshot is subsequent to it. No secrets or application tokens are recorded here.

## 1. Read order and exact stopping point

1. This document: current state, constraints and next actions.
2. [Complete work log](WORK_LOG_2026-10-25.md): chronology, failures, decisions and results through the last review.
3. [Operations runbook](OPERATIONS.md): environments, launch, tmux, tunnel, diagnostics and recovery.
4. [Submission readiness](SUBMISSION_READINESS.md): outstanding deliverables and honest claims.
5. [Earlier handoff, preserved in full](history/HANDOFF_BEFORE_FINAL_UI_REVIEW_2026-10-25.md): earlier setup, historical commands, gotchas and detailed dataset/training history. Its superseded current-status paragraphs are historical, not instructions to repeat completed work.
6. Stage `findings/`, `docs/GENERATION_RUN_REVIEW.md`, `docs/PREDICTION_COMPARISON_REVIEW.md`, `docs/PIPELINE_RESEARCH_REVIEW.md` for detailed evidence.

**Stopping point:** automatic upload → preprocessing → tested Surya v2 → clean Qwen adapter → crop/render/PDF works on the GPU. GPU returned to **42 MiB** with only gnome-shell after two reported completed runs. Latest archived evidence is lecture 14: 10 input pages, 94.12 seconds, 16 matched descriptions, 47 preserved blocks, one math syntax fallback, 13 output PDF pages. This verifies execution, not OCR/diagram accuracy. Visual review found incorrect caption associations, partial crops and an appendix heading appearing before the last reconstructed figure.

**Proposed next renderer changes are NOT implemented:** neutral captions with source-page references; explicit heuristic uncertainty flags; conservative spatial merging instead of count-driven merging; `\clearpage` before the source appendix. User asked whether these need new models: answer no, they are renderer/matching changes. Then user requested comprehensive documentation and saving all work. Do not imply those proposals are already shipped.

## 2. Project and ownership

Team InTra, IE643: convert handwritten lecture photos/scans into clean, searchable, structured PDFs. Official requirements: [PROJECT_STATEMENT.md](PROJECT_STATEMENT.md). Five stages/deliverables: preprocessing; trained recognition; structure/layout; reconstruction; PDF generation/evaluation. Submission also requires trained models, code/setup documentation, a user interface, metrics and stage-wise report.

Akshat owns dataset, preprocessing, reconstruction/PDF/evaluation; Ishaan Mane owns the repository and contributed the original Sauvola preprocessing work. Do not infer that all official deliverables are satisfied: structure is pretrained Surya, optional outlining is zero-shot Qwen, rendering is deterministic. Clarify actual contributions in the report, particularly if instructions demand distinct trained models for those stages.

## 3. Non-negotiable working rules

- **Push only when the user explicitly says “push”.** Local implementation/tests/commits are authorized. A new request to save/document is not push authorization.
- Single working branch everywhere: `akshat/dataset-and-preprocessing`. **Never switch the GPU checkout's branch.** A prior branch switch removed files that were not tracked on that branch.
- GPU outputs for repo review move through Git: GPU commit/push, Mac pull. The user has also supplied UI-downloaded bundles directly; archive these as provided. Do not invent direct SSH/scp access.
- User accesses GPU through Antigravity terminal. No usable Ports panel or SSH host address was available. Agent cannot run GPU commands itself; provide copy-paste commands, each with **Expect:**. Avoid repeated diagnostic requests after evidence is sufficient.
- Long tasks use tmux. Detach with Ctrl-b then d. **Never Ctrl-C a training pane.** Stop only the specifically identified service. Never `tmux kill-server` or broad process-killing commands.
- User wants concrete next actions, minimal unnecessary permission prompts and no retraining just to repair rendering/integration.
- Do not publish tokens, email PINs, keys or full token-bearing URLs. Tokens change when the UI restarts. Historical chat tokens must not be reused as documentation credentials.

## 4. Machines and dependencies

| Item | Value / qualification |
|---|---|
| Mac checkout | `/Users/akshatmac/Desktop/IE643/ie643_project` |
| GPU checkout | `/home/intralab/workspace/ie643_project` |
| Repo | `https://github.com/ishaanmane/ie643_project.git` |
| GPU setup | `source /home/intralab/workspace/ie643_env.sh` activates environment, sets cache and changes directory |
| GPU | RTX 5060 Ti, 16 GB; observed driver 595.91.07, driver CUDA capability 13.2 |
| Qwen environment | `/home/intralab/ie643/.qwen`; latest running-process evidence is Python **3.11.17**, overriding older notes saying 3.13 |
| Qwen runtime | torch 2.11.0+cu128, transformers 4.57.6; earlier recorded peft 0.21.2, bitsandbytes 0.50.2 |
| Adapter | `runs/qwen25vl_clean/final_adapter`; config verified, base identifier correct, `adapter_model.safetensors` 181.6 MiB |
| Tested Surya client | `/home/intralab/workspace/ie643_layout_envs/surya0221`, Python 3.11, `surya-ocr==0.22.1` |
| Tested model server | sibling `vllm0320`, `vllm==0.32.0`; checkpoint `datalab-to/surya-ocr-2` |
| Old Surya | 0.7.0 in `.qwen` is NOT the reviewed model; do not use it as a substitute |
| HF cache | `/home/intralab/workspace/hf_cache` |
| PDF stack | GPU Pandoc/XeLaTeX/DejaVu/pdftotext; PyMuPDF installed after initial missing-fitz error |
| Interface | Python stdlib HTTP server, no Gradio/Streamlit required |
| Tunnel | `$HOME/.local/bin/cloudflared`, observed 2026.10.3; HTTP/2 required on this network |
| Mac validation | `/usr/bin/python3` has PIL/cv2/fitz/numpy, no GPU torch; use `PYTHONPYCACHEPREFIX=/tmp/ie643-pycache` |

Do not confuse driver CUDA version with the torch build version. Older runtime notes remain useful history but observed process output is the current evidence.

## 5. Pipeline and why both models exist

### Batch dataset path

Raw images → corrected preprocessing → precomputed Surya tags → clean-adapter Markdown → optional base-Qwen text outline → deterministic renderer → Pandoc/TeX → PDF and reports.

### Current uploaded-document path

`06_interface/server.py` accepts PDF/images, one job at a time (20 pages / 25 MiB browser limit). Each job lives in `out/upload_jobs/<id>/output`:

1. Save originals and SHA-256; rasterize PDF/TIFF/images in supplied order.
2. Run existing preprocessing into job-local processed images.
3. `layout.py` checks exact package versions, starts its own vLLM server at localhost:8001, runs Surya on processed pages, shuts down its private server/worker process group, validates coverage and coordinate bounds, writes normalized tags/crops.
4. `recognition_worker.py` loads the trained clean adapter in a **short-lived process**, writes predictions, and exits. Process exit releases CUDA/model allocations. UI itself stays lightweight.
5. Renderer preserves transcription blocks, matches description positions to Surya figure boxes, merges boxes, inserts crops, checks math and builds PDF. Original scans remain appended.
6. Download PDF, Markdown/bundle and inference report. Bundle includes tags, Surya results/logs and `diagram_review.json`.

Surya supplies spatial regions/types/reading order; Qwen supplies text/LaTeX and descriptions. Optional outline Qwen supplies semantic headings, not bounding boxes. These are different functions. Clean recognition does not take boxed images or Surya JSON. Using Surya for crops does not change the trained weights or CER.

Defaults: CLI/server `--layout surya`; explicit `--layout none` uses appendix-only mode. Layout failure aborts rather than silently pretending crops succeeded. No annotations or cached dataset predictions are read for fresh upload inference. Dataset lectures uploaded during tests are integration tests, not established held-out or novel-data accuracy evaluations.

## 6. Dataset, preprocessing, training and metrics

- 410 pages: 205 IE643 chalkboard, 129 MLT digital ink, 56 IE802 notebook, 20 HumynLabs CS.
- Unit-level split: **318 train / 25 val / 55 test / 12 excluded uncertain**. Val: 19 lecture-7 pages plus 6 week-6 pages. No notebook photos in validation/test. Labels are AI-generated and unverified; test split not scored.
- Preprocessing fixes: turn deskew off; avoid chalkboard warp when dark; reject implausible aspect ratio; require ≥80% warp area; expand corners 2%. Final **55 warped / 355 cropped**, zero reported failures. This count identifies corrected image generation. Surya boxes must match the exact processed image, not a different preprocessing/rasterization.
- Surya v2 on all corrected pages: 4,283 blocks, 410 pages, zero errors; 333 figure and 14 table blocks among types. Tags are unverified drafts. Review history includes missing margins, merged text/equations, overlapping boxes, background bleed and misclassified diagrams.
- Qwen2.5-VL-7B clean/boxed_json variants: 4-bit NF4 double quantization, bf16, r16/alpha32/dropout .05, q/k/v/o/gate/up/down adapters (47.6M parameters), 318 pages, 3 epochs/120 steps, batch1×8, LR1e-4. About 62 minutes/run, 13.2 GB peak VRAM.
- Image limit 1,000,000 pixels, dimensions multiples of 28; answer-only loss masking; use_cache enabled for generation. Removing prepare_model_for_kbit_training avoided ~2GB fp32 upcast overhead.

| Variant | CER | WER | Text CER | Equation exact score |
|---|---:|---:|---:|---:|
| Base boxed_json | .712 | .927 | .892 | .061 |
| Trained boxed_json | .287 | .469 | .258 | .273 |
| Trained clean (chosen) | .277 | .485 | .222 | .244 |

Base clean CER .776. Clean retained side notes better in inspected examples. Boxed and clean change both image and prompt input, so do not claim a controlled causal proof that boxes alone caused the difference. Single runs / 25 validation pages constrain conclusions. CER is capped per-page macro CER; equation metric is reference-recall-like exact strings, not semantic correctness; missing predictions excluded from existing aggregate scorer. Correctly label metrics rather than silently relabel old results.

## 7. Reconstruction evidence

| Run | Evidence |
|---|---|
| 42-unit annotation reconstruction | 410 input pages, 42 PDFs; 2,579/2,579 Markdown blocks; 41 outlines/384 sections; 227/243 diagram descriptions matched; 2,739 math snippets, 6 diagnosed failures; all checks XeLaTeX |
| Two-unit actual prediction comparison | 128/128 blocks in plain and outlined variants; 9/10 diagram descriptions, one math failure. Outline increased lecture PDF 8→9 pages, duplicated/misplaced headings and added Blank Page section; MLT mainly promoted heading level |
| Reviewed renderer fixes | Validation: 10/10 matches after one manually reviewed table link; one exact syntax repair → zero remaining. Notebook: 622 blocks, 58/62 matches +6 extras, three remaining syntax failures. Bounds checks zero outside words |
| Initial new-input smoke | Existing MLT page003, trained adapter, 19.11s; no fresh layout in initial version |
| Uploaded lecture12 before layout | 20 source pages, 151.08s, 119 blocks, 11 descriptions and zero crops; source appendix only |
| Lecture12 manual tested Surya | 9 matches +3 extras, 2 unmatched (source17/19 mislabeled text/equation); 119 blocks; one caption math failure; 21 PDF pages, zero outside words |
| Lecture14 automatic current UI | 10 source pages, 94.12s, 16/16 descriptions assigned, 47 blocks, 23 equation snippets/one failure, 13 PDF pages, zero outside words; correct Surya/vLLM versions; archive integrity checked |

Counts measure preservation/assignment/syntax, **not fidelity**. Latest review: captions for Figures7/8 do not describe crops accurately; Figure15 is partial; some neighbouring writing included; appendix title appears before Figure16; caption formula `\\{0,1,\\dots255\\} \\to \\[0,1\\]` falls back to raw text. All sixteen being assigned is not proof of correct matching. Diagram merged_from12 on one page warrants review of count-driven merging.

## 8. Saved evidence and repository map

- `results/upload_surya_review/`: committed lecture12 manual Surya PDF, Markdown, figures/source scans, tags/results/report (`0b89236`).
- `results/upload_automated_review/`: latest 66-entry download bundle, inference report, Markdown, diagram review and SHA-256 manifest. Bundle includes the PDF, original upload, predictions, crops, original-page images, tags, raw layout, overlays and logs. Downloaded PDF byte hash verified identical to bundled PDF. Stored once inside ZIP to avoid duplicating the large images/PDF.
- Source downloads remain `/Users/akshatmac/Downloads/inference (1).json`, `document_bundle (1).zip`, `upload_notes (4).pdf`.
- GPU lecture12 job: `out/upload_jobs/b5a76ebb273243929bd98d59169a3ef8/output`; rebuilt directory `documents_surya_20261025_110929/upload_notes`.
- GPU lecture14 job: `out/upload_jobs/67c6855a11a8412c93da63f309f9a137/output`.
- Failed managed-memory job: `out/upload_jobs/e18b9dec190d4f1e9032da29fdca1711/output`.
- `results/predictions_review/`, `results/render_fixes_review/`, `results/generation_eval*.md` retain earlier evidence.
- Adapter weights exist on GPU, not in Git. Submission-accessible external backup/checksum package still pending.

## 9. Last known services and access

Session names drifted: **notes-tunnel runs Python UI**, **web-tunnel runs cloudflared**. `notes-ui`, `qwen`, `surya-server`, `surya-setup` last showed idle bash. Verify live state before stopping anything. No separate manual Surya server should be running while automatic mode is used.

UI localhost7860, managed layout localhost8001 (port8000 belongs to an unrelated Python server; leave it alone). Temporary public URL last reported: `https://batteries-phase-township-switching.trycloudflare.com/`. It expires/changes when tunnel restarts. It is not a permanent submission deployment. Mac localhost cannot access GPU localhost directly.

Email-protected Quick Tunnel caused repeated login/fragment-loss problems. User authorized temporary simpler access without that layer. Current app still requires random application token for API/jobs/downloads. Form is public. HTTPS traffic passes through Cloudflare; do not describe it as never leaving the GPU. Never put token values into docs or Git. Full token URLs in earlier chat are not stable credentials.

## 10. Next steps, in order

1. Preserve this documentation/evidence locally, commit, push only if requested.
2. Implement proposed renderer fixes (neutral source-page captions, uncertainty records, conservative merging, clearpage appendix). Preserve raw predictions and descriptions; no ungrounded semantic repair. Add focused regression checks and visually compare before/after using saved results, without rerunning models.
3. Test and record updated PDFs; do not inflate match count by arbitrary reassignment. The two source17/19 diagrams need reviewed regions or explicit fallback, not fabricated confidence.
4. Package final adapter with configs/processor/checksums and accessible delivery location. Verify outside-machine backup.
5. Write consolidated submission report and capture UI screenshots, metrics definitions, setup/demo instructions and limitations. These engineering docs are not a completed academic report.
6. Audit remaining stale stage READMEs/findings; optionally provisional test scoring only with clearly stated unverified labels and no notebook coverage. No new training recommended solely for renderer defects.
