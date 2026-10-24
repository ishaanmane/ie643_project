# 07 · Open items

## Decisions

| Decision | Options | Effect |
|---|---|---|
| Notebook pages in val/test | Hold out a block of IE802 pages and some HumynLabs notes, or keep the split | Holding out means a small code change (IE802 is one unit), about 30 fewer training pages, and re-running fine-tuning for final numbers |
| Which variant to keep | **Decided: `clean`** | Keeps side notes, better text accuracy, no Surya before Qwen; confirm on the test split |

## Dataset

1. Fix the 12 `??` pages so they rejoin the splits.
2. Check all test labels by hand before reporting test scores (`data/VERIFICATION.md`).
3. Hand-check layout tags on about 20 test pages and move them to `data/tags/`.

## Model

1. Score the `clean` model on the test split (after the test labels are checked).
2. Back up `runs/qwen25vl_clean/final_adapter` (the chosen model).
3. Improve equation exact match (0.244); possible: more epochs, equation-heavy examples.
4. Optional: a 4th epoch (validation loss was still falling slightly).

## Pipeline

1. Layout metric script (box overlap, reading order).
2. Stage 4: rebuild a document from the Markdown plus figure crops, then generate the PDF.
3. Inference path for a new page: preprocessing → Qwen with the `clean` adapter for the Markdown; Surya alongside for figure crops and reading order.
4. User interface.
5. Report.

## Housekeeping

- Revoke the Gemini API key that was pasted in chat early in the project.
- Back up `runs/qwen25vl_*/final_adapter` off the GPU machine.
