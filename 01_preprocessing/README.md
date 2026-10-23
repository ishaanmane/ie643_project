# Step 1 - Preprocessing

| File | Purpose |
|---|---|
| `preprocess.py` | `NotesPreprocessor`: page-boundary detection and perspective warp (fallback: brightness crop), deskew, CLAHE contrast, non-local-means denoise, resize to 2000 px. Output stays grayscale/colour on purpose, because the vision-language model can use shading. |
| `batch_preprocess.py` | Runs it over `data/raw_scans/` into `data/processed/`. Resumable; `--force` regenerates everything. |
| `sauvola.py` | Alternative: Sauvola adaptive binarization (inverts dark-background pages first). Outputs go to `binarized_sauvola/`, with `compare/` side-by-sides. |

```bash
python3 01_preprocessing/batch_preprocess.py --force
python3 01_preprocessing/sauvola.py --step 10 --compare
```

Open question for the report: binarized input (Sauvola) versus the grayscale output of `preprocess.py`, compared on recognition accuracy.
