# Step 2 - Layout detection

Surya v2 (`surya-ocr` 0.22.1, model `datalab-to/surya-ocr-2`, zero-shot, served by vLLM 0.32.0).
In the final pipeline it is used **only to find figures and tables** and crop them; all text
and its order come from the recognition model (stage 3).

## Run (GPU machine)

```bash
python3 02_layout/run_layout.py
```

Starts a private vLLM server, runs Surya on every image in `data/processed/`, stops the server,
and writes `data/tags_draft/<page>.json` (blocks, boxes normalised to 0-1000) and
`data/crops/<page>_bN.png` (one per figure/table). Previous tags and crops are moved to
`out/layout_backup_<time>/`. Uses the same code as the upload interface (`06_interface/layout.py`)
and the environments in `/home/intralab/workspace/ie643_layout_envs` (see `docs/OPERATIONS.md`).

**Re-run it whenever `data/processed/` is regenerated**: boxes are in the pixel space of the
processed image, so old tags give wrong crops.

| File | Purpose |
|---|---|
| `run_layout.py` | Batch run over `data/processed/` |
| `surya_to_tags.py` | Surya results.json -> tags + crops (used by `run_layout.py` and the interface) |
| `experiments/` | First 10-page test (`SURYA_FINDINGS.md`), the Kaggle all-page run, `draw_boxes.py` for the dropped boxed variant |

## Earlier: running Surya on Kaggle (T4)


Settings: Accelerator GPU T4 x2, Internet On. Surya v2 needs a vLLM server, and Kaggle has no Docker, so we start it ourselves. The two packages go in **separate** environments, because installing them together made `uv` fall back to a 2023 `vllm` that cannot build.

```python
# 1. clone + environments (about 10 min)
!git clone -q -b akshat/dataset-and-preprocessing https://github.com/ishaanmane/ie643_project.git
%cd /kaggle/working/ie643_project
!pip install -q uv
!uv venv --python 3.11 /kaggle/working/venv_vllm
!uv pip install --python /kaggle/working/venv_vllm/bin/python vllm --torch-backend=auto
!uv venv --python 3.11 /kaggle/working/venv_surya
!uv pip install --python /kaggle/working/venv_surya/bin/python surya-ocr
```

```python
# 2. start the model server (2-5 min; prints "server ready")
import subprocess, time, requests
srv = subprocess.Popen(
    ["/kaggle/working/venv_vllm/bin/vllm", "serve", "datalab-to/surya-ocr-2",
     "--dtype", "half", "--max-model-len", "8192", "--max-num-batched-tokens", "8192",
     "--limit-mm-per-prompt", '{"video": 0}', "--enforce-eager",
     "--gpu-memory-utilization", "0.90", "--port", "8000"],
    stdout=open("/kaggle/working/vllm.log", "w"), stderr=subprocess.STDOUT)
for _ in range(120):
    try:
        if requests.get("http://localhost:8000/v1/models").ok: print("server ready"); break
    except Exception: pass
    time.sleep(5)
else:
    print(open("/kaggle/working/vllm.log").read()[-3000:])
```

```python
# 3. layout on a folder of images; boxes + overlays go to surya_out/
import os
os.environ["SURYA_INFERENCE_BACKEND"] = "vllm"
os.environ["SURYA_INFERENCE_URL"] = "http://localhost:8000/v1"
!/kaggle/working/venv_surya/bin/surya_layout surya_in --images --output_dir surya_out
```

Why those server flags: `--dtype half` (the T4 has no bf16), `--limit-mm-per-prompt '{"video": 0}'` and a small `--max-num-batched-tokens` (otherwise vLLM's start-up memory check for video inputs runs the card out of memory), `--enforce-eager` (skips a memory-heavy optimisation). To stop a stuck server, kill by GPU process id (`nvidia-smi --query-compute-apps=pid --format=csv,noheader | xargs kill -9`); `pkill -f 'vllm serve'` also kills the shell running it.

Convert Surya output to our tags format and crop figures: `python3 02_layout/surya_to_tags.py --results <results.json> --images data/processed` (writes `data/tags_draft/` and `data/crops/`). Full runbook: [../docs/PIPELINE_TO_OCR.md](../docs/PIPELINE_TO_OCR.md).
