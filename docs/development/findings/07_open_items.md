# 07 · Open items and completed decisions

Updated 2026-10-25. Full submission checklist: [SUBMISSION_READINESS.md](../docs/SUBMISSION_READINESS.md).

## Completed since the original checklist

- Chosen recognition variant: **clean**; weights/config verified on GPU,181.6 MiB adapter.
- Markdown/crop reconstruction and PDF generation implemented and reviewed.
- 42-unit annotation reconstruction, two-unit prediction outline comparison and reviewed rendering fixes completed.
- Fresh-upload CLI/UI with automatic tested Surya v2 and trained recognition implemented.
- Remote browser access works through temporary HTTP/2 tunnel.
- Model isolation fixed retained GPU memory; two observed completed runs returned to 42 MiB.
- Current handoff, work history, service runbook and latest automatic bundle saved.

## Next implementation priority

Neutral source-page captions, heuristic uncertainty records, conservative figure merging and appendix page break are **proposed, not implemented**. Rebuild saved PDFs without model inference and visually compare. See [latest review](08_upload_interface_and_reconstruction.md). No new training needed for these changes.

## Submission blockers

1. Package the clean adapter with configs/processor, dependency versions, base-model identifier and checksums; verify submission-accessible backup outside the GPU machine. Existing local backup notes are not external delivery evidence.
2. Write the consolidated academic report and collect demo screenshots. Engineering handoff documentation is not the final report.
3. Include reproducible start instructions and limitations; temporary tunnel URL depends on live services and is not permanent hosting.
4. Audit remaining historical stage documentation before using claims in the report.

## Evaluation and dataset work

- Verify test labels before reporting test accuracy;55-page test split remains unscored. Any earlier provisional scoring must be labelled against unverified references.
- Fix 12 uncertain `??` pages; do not silently change the established split or reported metrics.
- Decide whether a future experiment should hold out notebook photos. Current val/test have none; adding a proper holdout changes training/evaluation and may require retraining. Not a quick renderer fix.
- Hand-check layout tags on a held-out sample and implement IoU/reading-order metrics. Match counts are not substitutes.
- Improve formula transcription only through separately evaluated work; an extra epoch is a possible experiment, not a current requirement or demonstrated improvement.

## Housekeeping

- Revoke the Gemini key disclosed earlier; do not reproduce it.
- Preserve working branch and push-only-on-explicit-request rule.
- Preserve raw predictions and separate curated fixes from model outputs.
