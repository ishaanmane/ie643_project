# Upload interface — current status

**Verified on GPU 2026-10-25:** automatic tested Surya v2 → isolated Qwen adapter worker → PDF completed a 10-page lecture in 94.12 seconds. Memory returned to 42 MiB after completion, also observed after the preceding run. Twelve interface tests and thirteen renderer tests pass. See [current operations](../docs/OPERATIONS.md), [handoff](../docs/HANDOFF.md), and [archived evidence](../results/upload_automated_review/README.md).

Quality limitations: crop-caption associations can be wrong even when every description is assigned; some crops are partial; one caption formula fell back to text. Neutral captions, conservative merging and appendix clearpage are **proposed, not implemented**. The historical implementation notes below describe earlier checkpoints; their pending-validation statements are superseded by this paragraph.

## GPU memory correction

The first managed run failed: the UI process retained 7,398 MiB and Surya could not reserve 90% of VRAM. Recognition now runs in a short-lived `recognition_worker.py` subprocess, exits before rendering, and leaves the UI process without model weights. Surya still runs first in its own managed process group. No-op release no longer imports torch or initializes CUDA. Recognition failures retain `recognition.log` and raw predictions; incomplete worker output is rejected. Twelve CPU interface tests pass; repeated GPU uploads must still be tested.

After pulling this fix, stop and restart the existing UI process once to release its old memory. Current session naming: `notes-tunnel` contains the Python UI; `web-tunnel` contains cloudflared. Keep `web-tunnel` running. Check GPU memory after stopping the UI; then source the Qwen environment and restart `python3 06_interface/server.py`. Use its new application token.

## Current managed layout update

The CLI and server now default to `--layout surya`. Uses the verified Surya 0.22.1 client and vLLM 0.32.0 in `/home/intralab/workspace/ie643_layout_envs/`, checkpoint `datalab-to/surya-ocr-2`. Set `IE643_LAYOUT_ENVS` to override that directory and `IE643_LAYOUT_PORT` to override port 8001. Versions are checked before starting. There is no fallback to Surya 0.7.0.

Before launching the updated UI, stop the manually started server in the **surya-server pane only**. The managed runner refuses an occupied port; it never kills an unrelated server. Restart the old UI to load the Python changes. Keep the tunnel running. Then `source /home/intralab/workspace/ie643_env.sh` and `python3 06_interface/server.py`. A restart generates a new application token.

For each job: preprocess → release any previous Qwen instance → start isolated Surya server → detect layout → terminate its private server/worker process group → convert validated boxes → load Qwen adapter → recognize → crop/render. Loading models each job adds latency but avoids running both on the 16 GB GPU simultaneously. Failed layout aborts the job with logs in `surya_layout/`; it does not silently fall back. `--layout none` explicitly retains the earlier appendix-only mode.

The ZIP now includes layout tags/results/logs and `diagram_review.json` listing unmatched pages. Source scans remain appended. Matching and captions still need human review; no inferred correction of unmatched boxes is performed.

Validation: CPU schema, image-size/coverage checks, process-group cleanup and pipeline ordering tested. The manually operated identical Surya/client setup succeeded on GPU (9 matches, 3 extras, 2 unmatched). **The new managed lifecycle still requires a GPU upload test.**

---
The following documents the original interface and its initial validation:

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

If the email login redirect drops the URL fragment, paste the application token directly into the form after login. This is the value after `#token=` in the notes-ui terminal, not the email PIN. Fragment changes are also handled without requiring reload. The static HTML is read per request, so pulling this UI fix requires only refreshing the browser, not restarting the GPU server.
