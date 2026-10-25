# GPU/UI operations runbook

Current as of 2026-10-25. Read [HANDOFF.md](HANDOFF.md) first. User runs GPU commands through Antigravity; Mac agent cannot SSH to GPU. Commands below are for the GPU unless marked Mac. No new installation is required for the already-working setup.

## Inventory first

```bash
tmux list-panes -a -F 'Session: #S | Command: #{pane_current_command} | PID: #{pane_pid}'
ss -ltnp '( sport = :7860 or sport = :8001 )'
nvidia-smi
pgrep -a cloudflared
```

**Expect:** UI on7860, cloudflared, and no Surya listener on8001 while idle. GPU idle baseline observed42MiB, only gnome-shell. Session labels are not proof of contents. Last known Python UI is in `notes-tunnel`, tunnel in `web-tunnel`. Do not terminate arbitrary PIDs based on old numbers.

## Start/restart UI after an authorized push

Switch to the actual Python UI pane (`tmux switch-client -t notes-tunnel` from inside tmux; `tmux attach -t notes-tunnel` from outside). Once no conversion is running, Ctrl-C **only that UI pane**. No training-pane Ctrl-C. Keep tunnel running.

```bash
source /home/intralab/workspace/ie643_env.sh
git pull --rebase origin akshat/dataset-and-preprocessing &&
python3 06_interface/server.py
```

**Expect:** localhost7860 URL with a fresh random token. Never switch branch. Python changes require server restart; HTML-only changes are read on each request and need browser refresh only. Paste value after `#token=` into browser form, not the Cloudflare email PIN. Copying a localhost URL to the Mac does not access the GPU.

Retrieve token locally when necessary (private output):

```bash
tmux capture-pane -p -J -S -2000 -t notes-tunnel |
grep -oE '#token=[A-Za-z0-9_-]+' | tail -1 | sed 's/^#token=//'
```

**Expect:** latest token from the pane actually running the UI. If session roles change, adjust target. Do not paste token into chat or commit it.

## Tunnel

No accessible SSH address or forwarding panel was available. Cloudflare uses outbound connections; same Wi-Fi is unnecessary. QUIC timed out; HTTP/2 worked. Current user-approved temporary mode has no email-login layer; API remains app-token protected. Do not casually change this into public unauthenticated inference.

If no cloudflared process is running and `web-tunnel` does not exist:

```bash
tmux new-session -d -s web-tunnel \
  "$HOME/.local/bin/cloudflared tunnel --protocol http2 --url http://127.0.0.1:7860"
```

**Expect:** background process; no terminal output required. If session already exists, attach/switch and inspect it rather than repeatedly creating duplicates.

```bash
tmux capture-pane -p -J -S -200 -t web-tunnel |
grep -E 'https://[^ ]*trycloudflare\.com|Registered tunnel connection|ERR'
```

**Expect:** temporary HTTPS URL and registered HTTP/2 connection. Use newest URL, not older history lines. If it stops, old URL will no longer work. Link plus services is temporary demo access, not permanent hosting. Keep token private.

## Automated model lifecycle

Do not manually launch vLLM while UI managed mode is in use. `layout.py` checks Surya0.22.1/vLLM0.32.0, starts checkpoint `datalab-to/surya-ocr-2`, localhost8001, half precision,8192 context/batched tokens, video0,enforce-eager,GPU utilization.90. It refuses occupied8001 and stops only its own process group. UI starts isolated Qwen worker only after layout terminates. Worker exits before PDF rendering. Failed model stages leave logs, not silent successful fallback.

Environment overrides: `IE643_LAYOUT_ENVS` (default `/home/intralab/workspace/ie643_layout_envs`), `IE643_LAYOUT_PORT` (8001). HF_HOME `/home/intralab/workspace/hf_cache`. Explicit `--layout none` skips layout; do not use it while claiming diagrams are automatically cropped.

For CLI integration testing:

```bash
source /home/intralab/workspace/ie643_env.sh
python3 06_interface/pipeline.py data/raw_scans/mlt_week06_page003.jpg \
  --out "out/new_input_smoke_$(date +%Y%m%d_%H%M%S)"
```

**Expect:** managed Surya, then isolated Qwen, then output paths. Do not run simultaneously with a UI conversion on this single GPU. Existing output directories cannot be overwritten. This known validation image is a smoke test, not new held-out accuracy evidence.

## Tests and failure diagnostics

```bash
python3 -m unittest discover -s 06_interface/tests -v
python3 -m unittest discover -s 04_reconstruction/tests -v
```

**Expect:**12 interface tests and13 renderer tests (at540208d). CPU tests do not prove GPU lifecycle; two completed GPU jobs plus idle42MiB observations supply additional evidence. HTTP tests bind localhost.

For latest Surya startup failure:

```bash
python3 - <<'PY'
from pathlib import Path
logs=list(Path('out/upload_jobs').glob('*/output/surya_layout/server.log'))
if not logs: raise SystemExit('No server logs found')
p=max(logs,key=lambda x:x.stat().st_mtime)
print(p); print('\n'.join(p.read_text(errors='replace').splitlines()[-100:]))
PY
```

**Expect:**actual exception. Client failures: same job `surya_layout/client.log`; recognition failures:`recognition.log`; rendering:`documents/upload_notes/report.json`; browser job status:`out/upload_jobs/<id>/status.json`. Do not blindly retry an upload after an HTTP error: it may already have started. Check job status first.

## Installation provenance, not routine commands

Qwen environment must not be overwritten to install layout. Tested isolated environments were created with `uv venv --python 3.11`; installed client `surya-ocr==0.22.1` and server `vllm==0.32.0 --torch-backend=auto` separately. Earlier combined installation resolved obsolete vLLM. Existing Surya0.7.0 in Qwen env is irrelevant to current layout. Missing fitz was resolved with `uv pip install --python "$(command -v python3)" PyMuPDF` after sourcing env. Gradio/Streamlit absent and unnecessary.

## Git and evidence

```bash
git status --short
git log -1 --oneline
```

**Expect:** inspect local changes before pull/commit. GPU-generated outputs must be explicitly copied into `results/` because `out/` is ignored. Commit selected evidence, then wait for user “push”. Authorized transfer:

```bash
git pull --rebase origin akshat/dataset-and-preprocessing &&
git push origin HEAD:refs/heads/akshat/dataset-and-preprocessing
```

**Expect:**successful push; Mac then pulls same branch. Do not commit adapters/base weights into ordinary Git by accident. Adapter delivery needs a separately agreed submission location.
