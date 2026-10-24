# 07 · Open items

## Decisions

| Decision | Options | Effect |
|---|---|---|
| Notebook pages in val/test | Hold out a block of IE802 pages and some HumynLabs notes, or keep the split | Holding out means a small code change (IE802 is one unit), about 30 fewer training pages, and re-running fine-tuning for final numbers |
| Which variant to keep | `boxed_json` vs `clean` (and `boxed`) | Decided by the comparison run now in progress; `boxed_json` needs Surya at inference |

## Dataset

1. Fix the 12 `??` pages so they rejoin the splits.
2. Check all test labels by hand before reporting test scores (`data/VERIFICATION.md`).
3. Hand-check layout tags on about 20 test pages and move them to `data/tags/`.

## Model

1. Finish the clean comparison run and compare with `boxed_json`.
2. Score the chosen model on the test split (after step 2 above).
3. Address dropped side notes (more examples with margin notes, or a variant without boxes if the comparison points that way).
4. Optional: a 4th epoch (validation loss was still falling slightly).

## Pipeline

1. Layout metric script (box overlap, reading order).
2. Stage 4: rebuild a document from the Markdown plus figure crops, then generate the PDF.
3. Inference path for a new page: preprocessing → Surya → tags → boxes → Qwen with the adapter.
4. User interface.
5. Report.

## Housekeeping

- Revoke the Gemini API key that was pasted in chat early in the project.
- Back up `runs/qwen25vl_*/final_adapter` off the GPU machine.
