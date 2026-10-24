# Findings

What we built, measured and learned, stage by stage. Every number here was measured on our data unless marked as an estimate. Detailed run instructions live next to the code; these files record results and decisions.

| File | Covers |
|---|---|
| [01_dataset.md](01_dataset.md) | Sources, labels, splits, leakage checks, fixes, known gaps |
| [02_preprocessing.md](02_preprocessing.md) | Pipeline, five bugs found and fixed, final numbers |
| [03_layout_surya.md](03_layout_surya.md) | Surya v2 on raw vs preprocessed pages, full run, tags and crops |
| [04_recognition_finetuning.md](04_recognition_finetuning.md) | Qwen2.5-VL-7B QLoRA: design, pilot, results, error analysis |
| [05_evaluation.md](05_evaluation.md) | Metrics, how to read them, their limits |
| [06_infrastructure_lessons.md](06_infrastructure_lessons.md) | Kaggle, local GPU, setup problems and their fixes |
| [07_open_items.md](07_open_items.md) | What is not done yet, and decisions still open |

## Summary

1. **Dataset:** 410 handwritten pages from 4 sources with Markdown labels, split by lecture or week (train 318, val 25, test 55; 12 uncertain pages held back). No near-duplicate leakage (highest similarity 0.49). Gap: val and test contain no notebook-photo pages.
2. **Preprocessing:** page crop/warp, resize, illumination flattening, contrast, denoise. Inspection found five bugs, all fixed; the worst rotated about 80% of straight pages and another cut off parts of 7 notebook pages. Final version: 410 pages, 0 failures, reproducible across Kaggle, Mac and the GPU machine.
3. **Layout:** Surya v2 zero-shot gives usable boxes and reading order; preprocessing helped it (margin notes found, neighbouring-page bleed removed). Full run: 410 pages, 4,283 blocks, 0 errors.
4. **Recognition:** Qwen2.5-VL-7B fine-tuned with 4-bit QLoRA, two variants on 25 validation pages. With boxes + layout JSON: CER 0.712 → 0.287, equation match 0.061 → 0.273. On the plain page (`clean`): CER 0.776 → 0.277, text-only CER 0.222, equation match 0.244.
5. **Decision:** `clean` for extraction. The boxes made the model drop side notes Surya had not boxed (about 65% of the label length on those pages, against 97-98% for `clean`), and `clean` needs no Surya step before Qwen. Surya stays for figure crops and reading order in the PDF stage.

Branch: `akshat/dataset-and-preprocessing` of `ishaanmane/ie643_project`.
