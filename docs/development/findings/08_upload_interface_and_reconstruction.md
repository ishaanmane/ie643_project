# 08 · Upload interface and reconstruction findings

Updated 2026-10-25. Implementation through `540208d`; evidence archive added at `c039535`. See [handoff](../docs/HANDOFF.md), [work history](../docs/WORK_LOG_2026-10-25.md) and [operations](../docs/OPERATIONS.md) for context and exact launch instructions.

## What now works

A user uploads PDF/images through the browser; the GPU preprocesses pages, runs tested Surya v2 layout, runs the existing clean Qwen adapter, crops detected figures, checks math syntax, and builds searchable PDF/Markdown plus a downloadable evidence bundle. No new recognition training was done for this integration. Source scans are retained in an appendix.

The UI is a Python stdlib server on localhost:7860 with a per-start application token and one active job. Browser limits:20 pages,25 MiB total. Job data stays under `out/upload_jobs/<id>/output`; `out/` is ignored by Git. Remote access uses a temporary Cloudflare HTTP/2 tunnel; traffic passes through Cloudflare. No Gradio or Streamlit dependency is required.

## Roles and execution order

- **Surya:** `surya-ocr==0.22.1`, checkpoint `datalab-to/surya-ocr-2`, vLLM 0.32.0. These match the earlier reviewed Kaggle setup. The old Surya 0.7.0 installed in `.qwen` is not used.
- **Recognition:** Qwen2.5-VL-7B-Instruct plus clean trained adapter; plain processed image input. Surya boxes are used for reconstruction, not fed into this clean recognition model.
- **Rendering:** deterministic matching/cropping and Pandoc/XeLaTeX. Optional semantic outlines remain off for upload runs.
- **Lifecycle:** preprocess → owned Surya server/client → stop its process group → isolated Qwen worker → worker exits → PDF. Package versions, result coverage, image dimensions and coordinate bounds are checked. Layout failures abort rather than silently claiming successful cropping.

## GPU memory failure and verified correction

The first managed implementation deleted model references and emptied the CUDA cache in the UI process. It still retained 7,398 MiB. Surya failed: 8.08 GiB free vs 13.93 GiB requested at 90% utilization. `nvidia-smi` identified the UI Python process, not an unrelated service.

Commit `540208d` moved recognition into a short-lived subprocess. Its exit releases model/CUDA allocations; no-op cleanup no longer imports torch into an unused parent. Two post-run user checks showed **42 MiB total GPU use**, only gnome-shell, with no model processes. This verifies the observed jobs, not indefinite stress testing. Twelve interface tests and thirteen renderer tests pass; CPU tests are separate from GPU execution evidence.

## Measured runs

| Run | Input | Result |
|---|---|---|
| Initial adapter CLI smoke | Existing MLT page003 |19.11s; actual trained recognition and PDF; initial appendix-only mode |
| Lecture12 initial upload |20 source pages |151.08s;119 blocks;11 diagram descriptions, zero crops because fresh layout was not integrated |
| Lecture12 manual Surya rebuild | Saved predictions and processed pages |9 matched descriptions +3 extra figures;2 unmatched;119 blocks retained;one math fallback;21 PDF pages;zero outside words |
| Lecture14 automatic upload |10 source pages |94.12s;16/16 descriptions assigned;47/47 blocks retained;23 equation snippets, one syntax fallback;13 PDF pages;zero outside words |

No predictions reached their token limit in the archived lecture14 run. ZIP integrity passed; its PDF hash equals the separately downloaded PDF. These dataset lecture uploads demonstrate integration, not an independently established held-out accuracy result.

Evidence: [manual review artifacts](../results/upload_surya_review/), [automatic run archive and manifest](../results/upload_automated_review/README.md). The complete 66-member automatic bundle preserves original upload, predictions, PDF, figure crops, source scans, tags, raw layout, overlays, logs and reports.

## Visual findings: assignment is not correctness

Lecture12: true diagrams on source pages 17 and 19 were classified as text/equations and therefore not cropped. The first generated caption reversed layer dimensions. Some crops include neighbouring writing; one caption equation falls back to raw text.

Lecture14 PDF pages 1–8 inspected:

- Figures 7/8 have descriptions that do not accurately identify their crop content.
- Figure 15 shows only part of the network described in its caption.
- Several crops include neighbouring text or omit diagram context.
- Source page 7 had 12 detected regions merged to one assigned figure. Matching counts alone do not validate this union.
- The appendix heading appears on PDF page7, before the last reconstructed figure on page8.
- PDF page2 exposes malformed caption LaTeX: `\{0,1,\dots255\} \to \[0,1\]`.

Thus16/16 assigned descriptions is **not 16/16 correct diagrams**. All blocks retained does not prove OCR completeness against the scan. Successful compilation or zero out-of-page words does not establish mathematical meaning, correct captions or no overlap.

## Recommended changes — not implemented

1. Use neutral captions with source-page references; preserve original model descriptions separately instead of presenting them as verified claims.
2. Record heuristic review flags for merged boxes, ambiguous associations and count disagreement; do not call these calibrated confidence scores.
3. Merge more conservatively based on spatial evidence, rather than simply reaching the number of descriptions. Preserve separate regions where association is uncertain.
4. Insert `\clearpage` before the appendix to flush pending figures and start a new page.
5. Rebuild both saved runs from existing predictions/layout, preserving before/after evidence; no model rerun or retraining is needed for these renderer changes.

Neutral captions reduce misleading claims but do not repair incomplete boxes. Source-reviewed overrides must be labelled manual assistance, not model accuracy gains.
