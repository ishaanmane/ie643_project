# Step 2 - Layout detection

Detects text blocks, equations, diagrams and tables on a page, with reading order. Tried so far: Surya v2, zero-shot. Results and verdict: [SURYA_FINDINGS.md](SURYA_FINDINGS.md). Raw output: `surya_raw_results.json`. Design: [../docs/PIPELINE.md](../docs/PIPELINE.md).

## Running Surya on Kaggle (T4)

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

Planned: `layout.py` (wrapper that returns normalised 0-1000 boxes, labels and order).
