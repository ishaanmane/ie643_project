# 02 · Layout (Surya v2, zero-shot)

- `surya-ocr` 0.22.1, model `datalab-to/surya-ocr-2`, served by vLLM 0.32.0 on the GPU machine.
  Used **only to find figures and tables** and crop them; text and reading order come from Qwen.
- Re-run on the final preprocessed images (boxes are tied to the exact image): **410 pages in
  279 s**, 348 figure/table crops. Blocks found: text 2123, equation 1314, figure 334, heading 165,
  page footer 165, list 53, page header 37, table 14 (`results/layout/`).
- Tags live in `data/tags/` (Surya boxes used as-is, not hand-checked). Example overlays:
  `results/layout/examples/`.
- **Not trained:** no box annotations exist, Surya v2 has no simple fine-tuning path, and the main
  figure problem seen in development was matching crops to descriptions, not detection.
- Known weaknesses (development test): missed margin notes on busy notebook pages, boxes mixing
  text and equations, some partial or missed figures. Weights: research-use licence.
- Planned metrics: figure count vs `[Diagram]` count per page; a hand-graded sample of crops.
