# Submission readiness — current 2026-10-25

This supersedes the initial pre-interface audit. See [handoff](HANDOFF.md), [work history](WORK_LOG_2026-10-25.md) and [runbook](OPERATIONS.md).

## Completed and evidenced

- Dataset, corrected preprocessing, full Surya layout run and clean/boxed recognition training.
- Validation scores and retained predictions; clean adapter chosen.
- Annotation reconstruction across42-units, plain/outline prediction comparison, audited rendering fixes.
- Real upload UI with token authentication, PDF/image input, trained recognition, tested Surya v2 layout, crops and PDF/bundle/report downloads.
- Remote access through temporary outbound HTTP/2 tunnel. Browser flow works without same Wi-Fi.
- Sequential model processes; two post-run observations at42 MiB, no model GPU processes. Latest automatic10-page run archived with94.12 s runtime.
- Twelve interface tests and 13 renderer tests pass at 540208d; GPU execution separately evidenced.
- Comprehensive engineering handoff/runbook/history and archived latest bundle with checksums.

## Remaining submission work

1. **Model package/delivery.** Config and 181.6 MiBadapter verified on GPU, but external submission-accessible backup not verified. Package adapter, processor/tokenizer, exact base identifier, inference settings, dependency versions and checksums; choose delivery location. `runs/` is ignored; source GitHub does not deliver weights. Do not accidentally commit base weights into ordinary Git.
2. **Consolidated academic report.** Findings and engineering documentation exist; this is not yet a polished stage-wise submission report. Include goals/ownership, label provenance/splits, preprocessing fixes, baseline/trained metrics, layout role, outline ablation, deterministic renderer, manual fixes, UI/screenshots, limitations and reproducibility. Explain pretrained vs fine-tuned vs zero-shot components honestly; do not claim independently trained structure/generation models.
3. **Renderer quality pass.** Neutral source-page captions, matching uncertainty flags, conservative merging and appendix clearpage are proposed, unimplemented. Rebuild saved outputs without model reruns, preserve originals andcompare visually. Review source17/19 missed diagrams and partial crops. Syntax fallback/glyph/semanticerrors remain.
4. **Evaluation scope.** Existing25-page validation / two units, no notebook holdout, no scored test set. AI labels unverified. CurrentCER capped macro; equation exact score reference-recall-like; missing predictions excluded. Distinguish preservation, syntax, assignment count and actual accuracy.16/16 assigned figures had visible misassociations. New upload execution is not independent generalization evidence.
5. **Submission launch/demo.** Provide trained weights separately, current runbook, screenshots and representative outputs. Temporary tunnel requires both services; no guaranteed stable URL. Confirm cold start from documented setup if time permits. Include remaining quality limitations rather than hide warnings.
6. **Legacy docs audit.** Current handoff/main README/interface README point to current state. Older stage findings/READMEs contain historical claims; review before quoting, particularly old split counts, training pending and causal claims about boxes. Historical handoff retained unchanged for traceability.

## What not to do

Do not retrain solely to fix caption/layout code. Do not install Surya 0.7as substitute for tested 0.22.1. Do not overwrite .qwen with vLLM dependencies. Do not leave manual Surya running beside managed UI. Do not remove token auth or expose GPU services on 0.0.0.0 casually. Do not claim tests prove OCR correctness. Push only on user instruction.
