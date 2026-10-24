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
| Figure layout | Numbered, centred figures with the description as caption; aspect ratio preserved; at most 55% text width / 30% text height on letter paper with 2 cm margins; pinned in place (no LaTeX floating), so order matches the notes |
| Equations | Syntax checked with xelatex or Tectonic, else pandoc's approximate parser. Diagnosed failures are shown verbatim with a warning. Compiler errors/timeouts are reported separately; syntax success does not mean mathematical correctness. |

All 42 units, labels as input (Mac, HTML output): 410 pages, 243 diagram descriptions, 227 matched to a crop (93%), 16 kept as text, 38 extra drawings, 2,739 equations with 1 parser failure (`\hphantom`, which LaTeX itself accepts).

```bash
python3 04_reconstruction/render_document.py --unit ie643_lec07                                  # labels -> PDF
python3 04_reconstruction/render_document.py --unit ie643_lec07 --pages-md preds/lora_clean_val  # model output -> PDF
python3 04_reconstruction/render_document.py --all
```
Output: `out/documents/<unit>/<unit>.pdf`, `<unit>.md`, `figures/`, `report.json` (per page: descriptions, Surya figures, matched, extra; failed equations).

PDF engine: xelatex if installed, else Tectonic (small; `brew install tectonic` on a Mac). Both xelatex and Tectonic perform compilation checks.

Needs on Ubuntu: `sudo apt-get install -y pandoc texlive-xetex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended lmodern fonts-dejavu`.

## Step 2 (built): outline generator, `outline.py`

The LLM proposes **structure only**: where sections start (block ids like `p4.3`), a short title, and a level (1 main topic, 2 sub-topic). It never writes content. Sections are contiguous runs of blocks in reading order, and the renderer copies every block verbatim, so nothing can be dropped, duplicated or reordered.

Checks in code: valid JSON; start ids exist and increase; levels 1-2; every content word of a title must occur in the notes, otherwise the section break is dropped; an outline with more invalid than valid sections is rejected (page order is used). Model: Qwen2.5-VL-7B used text-only (already downloaded for extraction), zero-shot, greedy decoding. `--mock` builds the outline from existing headings, for testing without a model.

Every render now also reports **blocks kept** (ordered text occurrences in intermediate Markdown before math fallback); it should be N/N, but this does not establish final PDF fidelity.

Tested (Mac, mock outline, model predictions as input): lecture 7 91/91 blocks kept, 9 sections; week 6 37/37, 5 sections. Validation tested against non-JSON, unknown ids, out-of-order starts, invented titles (section dropped) and invalid levels.

```bash
python3 04_reconstruction/outline.py --unit ie643_lec07 --pages-md preds/lora_clean_val             # LLM on the GPU
python3 04_reconstruction/render_document.py --unit ie643_lec07 --pages-md preds/lora_clean_val --outlines out/outlines
```

## Measure generation across all units

Use labels as input to measure reconstruction separately from recognition. For a local
smoke check without loading the model:

```bash
python3 04_reconstruction/outline.py --all --mock --out out/mock_outlines
python3 04_reconstruction/render_document.py --all --outlines out/mock_outlines --out out/mock_documents --format md
python3 04_reconstruction/evaluate_generation.py --docs out/mock_documents --outlines out/mock_outlines --md out/mock_generation_eval.md
```

Expect: 42 outlines and render reports, a per-unit table and totals, and zero PDFs
because this check requests Markdown. Mock outlines test the pipeline using existing
headings; they do not measure LLM outline quality.

On the GPU, omit `--mock`, render PDFs, and save the measured summary:

```bash
python3 04_reconstruction/outline.py --all --out out/outlines_all
python3 04_reconstruction/render_document.py --all --outlines out/outlines_all --out out/documents_all
python3 04_reconstruction/evaluate_generation.py --docs out/documents_all --outlines out/outlines_all --md results/generation_eval.md
```

Expect: 42 unit rows with block preservation, outline acceptance, section counts,
validation problems, equation check method and failures, diagram matching and PDF counts.
Use fresh output folders when changing input sets so old reports do not enter the totals.

## Next steps

3. Mark repeated content (recaps) using the leakage-check similarity.
4. Cross-check the extractor against Surya's own OCR to flag pages that may contain hallucinated text.

## Targeted retries and trustworthy reports (2026-10-25)

The first all-unit LLM run saved 42 files: 36 accepted, six rejected. The six raw
responses ended mid-JSON, consistent with the 1,536-token generation limit.
The updated prompt asks for compact JSON and at most 24 topic sections; this is a
practical budget limit, not a measured optimum. Retry only rejected files:

```bash
python3 04_reconstruction/outline.py --all --retry-rejected --max-new-tokens 4096 --out out/outlines_all
```

Expect: the 36 accepted files stay unchanged; only the six rejected units run.
Their original JSON files are backed up under `out/outlines_all/retry_backups/`.
Acceptance and section quality still need checking after this run.

**Keep inputs consistent:** `out/outlines_all` uses annotation Markdown. Render it
with the default annotation input. For actual recognition quality, generate separate
outlines using `--pages-md preds/lora_clean_val`, then render with that same folder.
Block IDs from annotations and predictions are not interchangeable.

The renderer saves a `run.json` manifest and per-report run IDs. The evaluator ignores
stale/unselected reports, counts missing reports and missing input pages, checks PDF
files exist, and takes section usage from the renderer. Legacy math reports have
unknown check status, rather than assumed success. A completed check can still have
diagnosed bad equations; `error` and `unchecked` never establish success.

All-42-unit mock/Markdown smoke check: 410 pages, 2,579/2,579 blocks retained;
math intentionally unchecked in that smoke run, no PDFs requested.

Local validation: eight regression tests and two PDFs from the 25 available clean
validation predictions, with no LLM outline. All 128 intermediate blocks retained,
128 unique equation snippets counted per unit, one diagnosed invalid equation,
both checks completed, 9/10 descriptions matched, both PDFs compiled. All nine
embedded images retain their source aspect ratio (relative difference <0.1%).
Lecture 7 page010 has no prediction: it is one of the excluded uncertain-label
pages in `data/VERIFICATION.md`; all 25 validation predictions are present.
See `results/generation_eval_fixes_val.md`. Tests used Tectonic on the Mac;
XeLaTeX behavior has regression coverage but needs the GPU integration run.

```bash
python3 -m unittest discover -s 04_reconstruction/tests -v
```

Expect: eight passing tests covering rendering dimensions, ordered/repeated text,
checker failures/timeouts, incomplete checks, report coverage and targeted retries.

Remaining: crop completeness/table inclusion, source transcription errors, figure
matching quality, semantic equation correctness, and a real-model outline comparison.
These changes do not fix or establish improvement in recognition CER.
