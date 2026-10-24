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
| Figure layout | Numbered, centred figures with the description as caption; at most 55% page width / 30% page height; pinned in place (no LaTeX floating), so order matches the notes |
| Equations | Checked with xelatex when installed (exact), else pandoc's math parser (approximate). A failing equation is shown verbatim with a ⚠ marker, never changed. |

All 42 units, labels as input (Mac, HTML output): 410 pages, 243 diagram descriptions, 227 matched to a crop (93%), 16 kept as text, 38 extra drawings, 2,739 equations with 1 parser failure (`\hphantom`, which LaTeX itself accepts).

```bash
python3 04_reconstruction/render_document.py --unit ie643_lec07                                  # labels -> PDF
python3 04_reconstruction/render_document.py --unit ie643_lec07 --pages-md preds/lora_clean_val  # model output -> PDF
python3 04_reconstruction/render_document.py --all
```
Output: `out/documents/<unit>/<unit>.pdf`, `<unit>.md`, `figures/`, `report.json` (per page: descriptions, Surya figures, matched, extra; failed equations).

PDF engine: xelatex if installed, else Tectonic (small; `brew install tectonic` on a Mac). The exact equation check needs xelatex; with Tectonic the approximate check is used.

Needs on Ubuntu: `sudo apt-get install -y pandoc texlive-xetex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended lmodern fonts-dejavu`.

## Step 2 (built): outline generator, `outline.py`

The LLM proposes **structure only**: where sections start (block ids like `p4.3`), a short title, and a level (1 main topic, 2 sub-topic). It never writes content. Sections are contiguous runs of blocks in reading order, and the renderer copies every block verbatim, so nothing can be dropped, duplicated or reordered.

Checks in code: valid JSON; start ids exist and increase; levels 1-2; every content word of a title must occur in the notes, otherwise the title is replaced by the notes' own text at that point; an outline with more invalid than valid sections is rejected (page order is used). Model: Qwen2.5-VL-7B used text-only (already downloaded for extraction), zero-shot, greedy decoding. `--mock` builds the outline from existing headings, for testing without a model.

Every render now also reports **blocks kept** (each source block's text found in the output); it must be N/N.

Tested (Mac, mock outline, model predictions as input): lecture 7 91/91 blocks kept, 9 sections; week 6 37/37, 5 sections. Validation tested against non-JSON, unknown ids, out-of-order starts, invented titles (replaced) and invalid levels.

```bash
python3 04_reconstruction/outline.py --unit ie643_lec07 --pages-md preds/lora_clean_val             # LLM on the GPU
python3 04_reconstruction/render_document.py --unit ie643_lec07 --pages-md preds/lora_clean_val --outlines out/outlines
```

## Next steps

3. Mark repeated content (recaps) using the leakage-check similarity.
4. Cross-check the extractor against Surya's own OCR to flag pages that may contain hallucinated text.
