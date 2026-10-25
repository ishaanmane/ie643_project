# Submission readiness audit — 2026-10-25

Audited the official project statement, tracked code, stage READMEs, findings,
metrics and GPU outputs through `d8beb66`. This audit cannot verify private GPU
checkpoint files or submission files stored outside this repository.

## Required work, in priority order

1. **New-input inference and upload interface.** At the initial audit no app/upload implementation was found. A local MVP is now implemented in `06_interface/`; seven CPU tests and simulated-recognition PDF integration pass. Real GPU inference and a genuinely new upload remain to be tested. Fresh Surya is not connected; originals are appended. The following describes the initial gap: The tested renderer enumerates units through existing annotations;
   it is not yet a standalone uploaded-document pipeline. The separate inference
   script uses the earlier Unsloth route, while successful training used Transformers
   + PEFT. Extract an inference-only path for the existing clean adapter; accept
   images/PDFs, preprocess, recognize, optionally obtain fresh layout, render, then
   provide Markdown/PDF downloads and visible warnings. Test one genuinely new input.
   An interface that only selects cached outputs does not demonstrate new-input support.
   Confirm an accessible way to open it from the user's terminal-only GPU setup.

2. **Model submission and reproducible setup.** Verify the final adapter config and
   nonempty weights, processor/tokenizer, base-model identifier, inference settings,
   tested dependency versions, and a submission-accessible backup. Existing backup
   notes do not prove a copy outside the same GPU machine. `runs/` is gitignored;
   GitHub code alone does not deliver the weights. Avoid uploading large weights to
   ordinary Git history. Record the chosen approved delivery location and checksums.

3. **Consolidated stage-wise report.** Extensive stage notes exist, but no consolidated
   submission report was found. Cover dataset/AI labels/splits, preprocessing fixes,
   both training variants, baseline and fine-tuned results, Surya, outlining ablation,
   renderer, reviewed repairs, interface, and limitations. State that recognition is
   fine-tuned, Surya pretrained, outlining zero-shot, and PDF rendering deterministic.
   The wording of deliverables 3/4 includes model development/fine-tuning; explain
   the actual contribution and verify instructor expectations if clarification is needed.

4. **Evaluation evidence and definitions.** Validation is 25 pages from two units;
   no notebook photos and no completed test-set scoring found. Current CER is capped
   per-page macro CER, not corpus CER. Equation matching is a reference-recall-like
   exact-string score: duplicates and extras are not fully penalized. Missing
   predictions are printed but excluded from the average. Label metrics accurately,
   include coverage, and do not replace old scores silently if the scorer is improved.
   Keep annotation-input reconstruction separate from prediction-input results.
   Reviewed K-fold mapping and exact syntax repair are curated assistance, not learned
   model accuracy gains. A small hand-audited formula/page set is useful; avoid using
   those same corrected examples as an independent improvement claim. Test scores
   against unverified references, if produced, must be explicitly provisional.

5. **Documentation cleanup.** Main README still says training/reconstruction are to do
   and uses old 324/26/60 split counts; current counts are 318/25/55 plus 12 excluded.
   Recognition README still says training has not run. Evaluation README says not
   started. Findings/open-items also contain superseded pending items. Replace these
   statuses and give one verified demo command and a clear output/model location.

## Remaining quality work after the blockers

- Source-check erroneous formulas (e.g. Ridge expression); syntactic validity is not
  mathematical correctness. Preserve raw predictions and separately record corrections.
- Notebook: three syntax fallbacks and missing-glyph warnings remain. Fix fonts without
  replacing mathematical symbols with guessed content. Some crops remain incomplete.
- Scale reviewed diagram grounding beyond one example only with additional held-out
  checks. No trained layout metric is currently substantiated by manual box labels.
- Retain page-order baseline; current outline is optional and has no demonstrated
  fidelity gain on the two compared units. A new structure model or recognition
  training run is not the first deadline priority.

## Already evidenced

Clean QLoRA training and adapter-based validation; 410 processed pages and Surya tags;
42 annotation-based PDFs; four plain/outlined prediction PDFs; tested rendering fixes;
13 regression tests; GPU XeLaTeX validation PDFs with 128/128 intermediate blocks,
10/10 matched descriptions after one reviewed link, one reviewed syntax repair;
notebook clipping fixed; all three latest PDFs have zero out-of-page words.
None of these implies perfect OCR, semantic equation correctness, or complete submission.

## Immediate next action

Verify GPU adapter files and inference/UI dependencies (read-only), then build/test
an inference-only entry point and upload interface. Do not retrain or reinstall the
working GPU stack merely to begin this task. Keep pushing subject to the user's
explicit `push` instruction and keep the GPU on the existing working branch.

## Update after implementation

User confirmed the clean adapter config, base identifier and 181.6 MiB weights on GPU, with torch/transformers/peft present. External checkpoint delivery remains unverified. Main README now reflects current split and stage status; older stage documents still need review. Antigravity terminal access is available; port forwarding is not yet confirmed. No physical access is required for CLI inference. Next: authorized push, GPU pull, one-page inference smoke test from `06_interface/README.md`, then a genuinely new upload.
