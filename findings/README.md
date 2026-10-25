# Findings

What we built, measured and learned, stage by stage. Historical and current measurements are distinguished; diagnostic counts are not automatically accuracy scores. Detailed run instructions live next to the code; these files record results and decisions.

| File | Covers |
|---|---|
| [01_dataset.md](01_dataset.md) | Sources, labels, splits, leakage checks, fixes, known gaps |
| [02_preprocessing.md](02_preprocessing.md) | Pipeline, five bugs found and fixed, final numbers |
| [03_layout_surya.md](03_layout_surya.md) | Surya v2 on raw vs preprocessed pages, full run, tags and crops |
| [04_recognition_finetuning.md](04_recognition_finetuning.md) | Qwen2.5-VL-7B QLoRA: design, pilot, results, error analysis |
| [05_evaluation.md](05_evaluation.md) | Metrics, how to read them, their limits |
| [06_infrastructure_lessons.md](06_infrastructure_lessons.md) | Kaggle, local GPU, setup problems and their fixes |
| [07_open_items.md](07_open_items.md) | Completed decisions, remaining submission and quality work |
| [08_upload_interface_and_reconstruction.md](08_upload_interface_and_reconstruction.md) | Automatic uploads, tested Surya, GPU memory fix and visual PDF review |

## Summary

1. **Dataset:** 410 handwritten pages from 4 sources with Markdown labels, split by lecture or week (train 318, val 25, test 55; 12 uncertain pages held back). Unit-level splitting reduces leakage; highest measured similarity was 0.49, with topical overlap remaining. Gap: val and test contain no notebook-photo pages.
2. **Preprocessing:** page crop/warp, resize, illumination flattening, contrast, denoise. Inspection found five bugs, all fixed; the worst rotated about 80% of straight pages and another cut off parts of 7 notebook pages. Final version: 410 pages, 0 failures, reproducible across Kaggle, Mac and the GPU machine.
3. **Layout:** Surya v2 zero-shot gives usable boxes and reading order; preprocessing helped it (margin notes found, neighbouring-page bleed removed). Full run: 410 pages, 4,283 blocks, 0 errors.
4. **Recognition:** Qwen2.5-VL-7B fine-tuned with 4-bit QLoRA, two variants on 25 validation pages. With boxes + layout JSON: CER 0.712 → 0.287, equation match 0.061 → 0.273. On the plain page (`clean`): CER 0.776 → 0.277, text-only CER 0.222, equation match 0.244.
5. **Decision:** `clean` for extraction. The boxed variant dropped side notes Surya had not boxed (about 65% of the label length on those pages, against 97-98% for `clean`), and clean recognition does not require layout inputs. This comparison changes both boxes and JSON/prompt, so it is not a causal ablation of boxes alone. Surya stays for figure crops and reading order in the PDF stage.

Branch: `akshat/dataset-and-preprocessing` of `ishaanmane/ie643_project`.

## Latest verified state — 2026-10-25

The GPU upload pipeline now runs tested Surya 0.22.1/vLLM 0.32.0 followed by the trained clean adapter in a separate worker, then renders diagrams and PDFs. The latest archived 10-page run took 94.12 s;47 blocks retained,16 descriptions assigned,one math syntax fallback. GPU returned to 42 MiB after completion, also observed after the prior run.

Visual review found incorrect crop-caption associations, partial crops and an appendix ordering issue. Neutral source-page captions, uncertainty flags, conservative merging and appendix clearpage are proposed but not yet implemented. No retraining is needed for those renderer changes.

[Current handoff](../docs/HANDOFF.md) · [Full history](../docs/WORK_LOG_2026-10-25.md) · [Service runbook](../docs/OPERATIONS.md) · [Latest evidence](../results/upload_automated_review/README.md)
