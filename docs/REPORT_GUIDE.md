# Where to find the material for each report section

Report template sections (IE643 instructions) -> files on branch `final`
(https://github.com/ishaanmane/ie643_project/tree/final). Write the report in your own words:
the instructions warn of a plagiarism check and zero marks for copied or AI-generated text.
These files are source material and numbers, not report text.

| Report section | Look here | What you will find |
|---|---|---|
| Title, problem | `docs/PROJECT_STATEMENT.md` | Official task and the five required deliverables |
| **Abstract** | `findings/03_recognition.md`, `findings/04_reconstruction.md`, `results/recognition_experiments.md` | Headline numbers: test corpus CER 0.915 -> 0.332, NED 0.596 -> 0.311, token F1 0.855; 529/529 blocks kept; 9/9 test PDFs |
| **Introduction** | `docs/PROJECT_STATEMENT.md`, `docs/development/PIPELINE.md` (sections 1-2) | Motivation, goal, deliverables |
| **Workflow** (bullets + diagram) | `README.md` (pipeline table), `docs/development/WORK_LOG_2026-10-25.md`, `docs/development/HANDOFF.md` | Stage order 0-6 and what was done when; the diagram can follow the pipeline table |
| **Literature survey** | `05_evaluation/README.md` (Nougat, OmniDocBench, CDM), `docs/development/PIPELINE_RESEARCH_REVIEW.md`, `findings/02_layout.md` (Surya) | Papers already used, with why they matter; reference list below |
| **Methods, before prep review** | `docs/development/planning/` (implementation plans, discussion), `docs/development/PIPELINE.md` (dated 2026-09-22), `docs/development/findings/01-03` | Original plan, first dataset and preprocessing, first Surya test |
| **Methods, after prep review** | `findings/00-06` (final branch) and `docs/development/findings/04-08` | Fine-tuning, boxed vs clean, deterministic renderer, outline LLM, evaluation, interface |
| Architecture / loss / optimiser | `findings/03_recognition.md`, `03_recognition/README.md`, `03_recognition/finetune_qwen25vl.py`, `03_recognition/qwen_data.py` | Qwen2.5-VL-7B, 4-bit NF4 QLoRA, LoRA r=16/alpha 32 on q,k,v,o,gate,up,down (47.6M params, 0.57%), answer-only cross-entropy, paged AdamW 8-bit, lr 1e-4 cosine, 3% warmup, 3 epochs, batch 1x8 |
| Reconstruction method | `findings/04_reconstruction.md`, `04_reconstruction/README.md` | Block splitting, figure matching, LaTeX checks, outline validation, PDF style |
| **Data** | `findings/00_dataset.md`, `data/README.md`, `data/TEST_LABEL_AUDIT.md`, `data/TEST_LABEL_CHECK.md`, `docs/development/DATASET_AUDIT.md`, `docs/development/findings/01_dataset.md` | 410 pages, 4 sources, label format, split 303/31/76 by unit, label audit, limitations |
| Data preprocessing | `findings/01_preprocessing.md`, `01_preprocessing/README.md`, `results/preprocessing/preprocess_report.csv`, `docs/development/findings/02_preprocessing.md` | Steps, the 5 earlier bugs and the desk-whitening fix, counts |
| **Experiments** (settings, hardware) | `findings/03_recognition.md`, `logs/final_clean.txt`, `logs/final_boxed_json.txt`, `docs/development/findings/06_infrastructure_lessons.md`, `docs/development/OPERATIONS.md` | RTX 5060 Ti 16 GB, PyTorch CUDA 12.8, transformers 4.57, peft 0.21, bitsandbytes 0.50; time 53/61 min, peak 10.8/13.1 GB; Kaggle T4 for early Surya runs |
| Negative / dropped experiments | `findings/03_recognition.md` (boxed_json no gain), `01_preprocessing/experiments/` (Sauvola), `02_layout/experiments/`, `03_recognition/experiments/` (Unsloth/Kaggle route), `04_reconstruction/experiments/` (hand fixes) | Include them: the instructions ask for all experiments |
| **Results: recognition** | `results/recognition_experiments.md`, `preds/*_score.txt` | Zero-shot vs clean vs boxed_json, val and test, 12 metrics, bootstrap CIs, paired test |
| Results: layout | `results/layout/count_metrics.md`, `results/layout/block_counts.txt`, `results/layout/examples/` | Surya recall 0.93 / precision 0.73; overlay images for qualitative figures |
| Results: reconstruction | `results/reconstruction/{val,test}_{plain,outlined}.md`, `results/reconstruction/pdfs_{val,test}/`, `results/reconstruction/outlines_*` | Generation tables, real PDFs for qualitative figures, outline examples |
| Results: preprocessing ablation | `preds/final_clean_raw_{val,test}_score.txt`, `logs/raw_vs_processed.txt`, `findings/01_preprocessing.md` | Raw vs preprocessed input, same model |
| Results: figure crops (hand-graded) | `results/crop_review/summary.md`, `*_grades.json` | correct / partial / wrong / not a drawing rates |
| Qualitative figures | `results/reconstruction/pdfs_test/*.pdf`, `results/style/sample_lec07.pdf`, `results/layout/examples/*.jpg`, `data/raw_scans/` (originals) | Before/after page pairs, outline vs plain |
| Interface (demo section) | `findings/06_interface.md`, `06_interface/README.md` | Notes2PDF features, warm models, limits |
| Limitations / extreme cases | `docs/REPORT_NOTES.md` | Everything the report must state honestly |
| **Novelty plan** | `docs/development/findings/07_open_items.md`, "Not used"/"future" notes in `05_evaluation/README.md`, `findings/02_layout.md` | Ideas: Qwen grounding for figure boxes (removes the matching problem), CDM formula metric, notebook-writer generalisation, cross-page sentence joining |
| **Conclusion** | `findings/README.md` + the headline numbers above | |
| GitHub link (required) | https://github.com/ishaanmane/ie643_project/tree/final | |

## References already used (check details before citing; follow the template format)

- Shuai Bai et al. Qwen2.5-VL Technical Report, arXiv, 2025. https://arxiv.org/abs/2502.13923
- Edward J. Hu et al. LoRA: Low-Rank Adaptation of Large Language Models, ICLR, 2022. https://arxiv.org/abs/2106.09685
- Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer. QLoRA: Efficient Finetuning of Quantized LLMs, NeurIPS, 2023. https://arxiv.org/abs/2305.14314
- Lukas Blecher, Guillem Cucurull, Thomas Scialom, Robert Stojnic. Nougat: Neural Optical Understanding for Academic Documents, arXiv, 2023. https://arxiv.org/abs/2308.13418
- Linke Ouyang et al. OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations, CVPR, 2025. https://arxiv.org/abs/2412.07626
- Bin Wang et al. CDM: A Reliable Metric for Fair and Accurate Formula Recognition Evaluation (Image over Text), CVPR, 2025. https://arxiv.org/abs/2409.03643
- Woosuk Kwon et al. Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM), SOSP, 2023. https://arxiv.org/abs/2309.06180
- Karel Zuiderveld. Contrast Limited Adaptive Histogram Equalization, Graphics Gems IV, 1994 (CLAHE).
- Antoni Buades, Bartomeu Coll, Jean-Michel Morel. A non-local algorithm for image denoising, CVPR, 2005.
- Jaakko Sauvola, Matti Pietikäinen. Adaptive document image binarization, Pattern Recognition, 2000.
- Datalab (Vik Paruchuri et al.). Surya OCR. https://github.com/datalab-to/surya (accessed date)
- John MacFarlane. Pandoc. https://pandoc.org (accessed date)
- Sorkin Type. Merriweather font. https://github.com/SorkinType/Merriweather (accessed date)
- Data: IE643 class scribes, MLT notes, IE802 notebook, HumynLabs notes: sources in `data/README.md`.

## Before and after the prep-presentation review

Git history only starts on 2026-10-23, so use the documents: `docs/development/planning/`
and `docs/development/PIPELINE.md` (2026-09-22) describe the plan and the state at the prep
review; everything in `findings/` on this branch is the final, re-run work after it.
