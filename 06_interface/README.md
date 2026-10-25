# New-input inference and local upload interface

Uses the existing clean Qwen2.5-VL adapter with Transformers + PEFT, in 4-bit inference mode. No training, annotation lookup, or cached prediction lookup. Accepts PDF/image inputs, preprocesses each page, recognizes Markdown, checks equations, and builds a searchable PDF plus an editable ZIP bundle.

Fresh Surya inference is not connected in this version. Original scans are appended to preserve diagrams for review; this is not automatic figure reconstruction. Outlining and curated fixes for known dataset pages are not applied to new inputs.

## GPU terminal smoke test

After the authorized push and pull, run from the repository root, in a free tmux pane:

```bash
source /home/intralab/workspace/ie643_env.sh
python3 06_interface/pipeline.py data/raw_scans/mlt_week06_page003.jpg \
  --out "out/new_input_smoke_$(date +%Y%m%d_%H%M%S)"
```

**Expect:** preprocessing, adapter loading, one-page recognition, equation checks, then JSON containing PDF, Markdown, bundle and report paths. This existing validation image checks integration; subsequently test a genuinely new scan. Outputs must use a new or empty directory. The default adapter is `runs/qwen25vl_clean/final_adapter`; override with `--adapter` if needed. First inference may take longer while weights load. Keep other GPU model processes stopped before this run.

Dependencies reuse the working GPU environment: torch, transformers, peft, bitsandbytes, Pillow, OpenCV, NumPy, PyMuPDF, Pandoc, XeLaTeX and installed fonts. Gradio and Streamlit are not needed. Do not reinstall the working model stack blindly on a missing-dependency error.

## Upload UI

```bash
python3 06_interface/server.py
```

**Expect:** a localhost URL containing an access token. Keep this tmux pane running. Open the full URL in a browser on the GPU machine, or forward remote port 7860 through the terminal application's port-forwarding feature and use the forwarded address with the same URL fragment. Ordinary terminal access alone does not establish a tunnel. Physical access is not required when forwarding is available. Server binds only to 127.0.0.1; do not expose it publicly.

Choose up to 20 pages / 25 MiB total. Check the displayed file order. Jobs run one at a time and persist under `out/upload_jobs/<id>/`; downloads include PDF, editable bundle and report. Original uploads, predictions, preprocessing diagnostics and rendering diagnostics are retained. A restart changes the token and clears in-memory job tracking; existing files remain on disk. Outputs are gitignored; deliberately copy selected review artifacts into `results/` for Git transfer.

## Validation status

Seven CPU tests pass, including HTTP authentication, upload validation, concurrent-job rejection, download handling, page limits and isolated output data. Existing thirteen renderer tests also pass. A real CPU preprocessing/Pandoc/Tectonic run produced a two-page PDF and ZIP using explicitly simulated recognition; the source appendix image was inspected. The browser form was visually inspected. **Real adapter inference through this entry point and browser upload-to-PDF on the GPU are pending.**

```bash
python3 -m unittest discover -s 06_interface/tests -v
python3 -m unittest discover -s 04_reconstruction/tests -v
```

**Expect:** 7 interface tests and 13 renderer tests pass. Interface tests require localhost binding but no model download or GPU.
