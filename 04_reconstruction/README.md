# Step 4 - Reconstruction and PDF

## Step 1 (built): deterministic renderer, `render_document.py`

Per-page Markdown (the labels, or the fine-tuned model's predictions) + Surya figure crops → one document per unit (lecture, week, notebook) → PDF via Pandoc + xelatex (HTML when no LaTeX is installed).

No model is involved, so nothing can be invented: every sentence and equation is copied from the per-page Markdown.

| Part | How |
|---|---|
| Pages | In order; each page's Markdown split into blocks (a `$$...$$` display is never split) |
| Figures | Each `[Diagram: ...]` matched to a Surya figure by position on the page (both in reading order; order-preserving alignment allows unequal counts). The crop goes in, the description becomes its caption. |
| Over-split figures | When Surya has more figure boxes than the page has descriptions, the closest boxes on the same row/column are merged until the counts match (one drawing boxed as three icons becomes one crop) |
| Unmatched | A description without a crop stays as italic text; a Surya drawing without a description is added only if it covers at least 3% of the page |
| Crop cleaning | Chalkboard crops: grayscale, inverted to dark-on-white; others: contrast stretch |
| Equations | Checked with xelatex when installed (exact), else pandoc's math parser (approximate). A failing equation is shown verbatim with a ⚠ marker, never changed. |

All 42 units, labels as input (Mac, HTML output): 410 pages, 243 diagram descriptions, 227 matched to a crop (93%), 16 kept as text, 38 extra drawings, 2,739 equations with 1 parser failure (`\hphantom`, which LaTeX itself accepts).

```bash
python3 04_reconstruction/render_document.py --unit ie643_lec07                                  # labels -> PDF
python3 04_reconstruction/render_document.py --unit ie643_lec07 --pages-md preds/lora_clean_val  # model output -> PDF
python3 04_reconstruction/render_document.py --all
```
Output: `out/documents/<unit>/<unit>.pdf`, `<unit>.md`, `figures/`, `report.json` (per page: descriptions, Surya figures, matched, extra; failed equations).

Needs on Ubuntu: `sudo apt-get install -y pandoc texlive-xetex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended lmodern fonts-dejavu`.

## Next steps

2. Outline generator: an LLM proposes section structure as block IDs only; the renderer still copies all text (no new content possible), with coverage checks.
3. Cross-check the extractor against Surya's own OCR to flag pages that may contain hallucinated text.
