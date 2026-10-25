# 06 · Infrastructure and lessons

## Kaggle (Surya, preprocessing)

| Problem | Cause | Fix |
|---|---|---|
| `numba` failed to build | Kaggle's Python 3.13 | Separate Python 3.11 environments made with `uv` |
| `vllm==0.1.2` (2023) got installed and failed to compile | Installing `vllm` and `surya-ocr` together made the resolver backtrack | Two environments: one for vLLM, one for Surya |
| vLLM ran out of memory at start-up on the T4 | It reserves memory for video inputs | `--limit-mm-per-prompt '{"video": 0}' --max-num-batched-tokens 8192 --enforce-eager --dtype half` |
| `pkill -f 'vllm serve'` killed its own shell | The pattern matched the command itself | Identify the owned service before stopping it; managed UI terminates only its own private process group |
| Session restarts wipe `/kaggle/working` | Updating a dataset input or idling restarts the session | Keep only small outputs; rebuild images from code |
| New zip still contained old files | `zip` adds to an existing archive | `rm -f` the zip first |
| Re-run used old code | `git clone` fails silently when the folder exists | Inspect the existing checkout, pull on its working branch, and compare `git log -1`; do not delete the live checkout |
| Notebook read the old dataset | Kaggle pins the dataset version first attached | Check a known count (55 warped pages) before continuing |
| Large output files would not download | Browser download of a 295 MB output | Rebuild images on the target machine instead |

## Local GPU (fine-tuning)

| Item | Detail |
|---|---|
| Machine | Ubuntu, RTX 5060 Ti 16 GB (Blackwell, compute 12.0), dual-boot |
| Storage | 171 GB workspace partition for repo and model cache (`HF_HOME`); system disk had 35 GB free |
| Setup | venv `.qwen`, PyTorch from the CUDA 12.8 index, installs with `uv pip` |
| Ollama | Holds GPU memory while a model is loaded: `ollama stop` before training |
| Long runs | Inside `tmux`; Ctrl-C in the training pane stops (and once hung) the run; detach with Ctrl-b d |
| Model download | 16 GB; progress bar only moves per 4 GB file, so it looks frozen for minutes |

## General lessons

1. Summary numbers can look perfect while images are wrong: three preprocessing bugs reported "0 failures". Always view samples.
2. Put a guard on every hand-off: counts (410, 55 warped), sizes (tags vs image), versions (`git log`). The guards caught the old-dataset problem twice.
3. Different machines give different bytes for the same image; compare sizes and pixels, not hashes.
4. Test the data path without a GPU first (real processor, masking, token counts): the GPU run then only had to confirm memory and speed.

## Upload UI and remote access lessons (2026-10-25)

| Problem | Evidence / fix |
|---|---|
|Mac localhost could not reach GPU|Antigravity had no forwarding panel/SSH address; outbound Cloudflare tunnel provided temporary HTTPS access|
|QUIC timed out|HTTP/2 connectivity passed; force `--protocol http2`|
|Repeated email login and lost token fragment|Added application-token field/hashchange handling; user authorized temporary tunnel without email layer, while API token authentication remains|
|Empty JSON response hid HTTP failure|Read text/status first, report empty/non-JSON/redirect responses; health preflight before upload|
|Missing fitz|Installed PyMuPDF in the UI Python environment; no wholesale model-stack reinstall|
|Wrong Surya version assumption|Live UI used 0.7.0, but recorded reviewed setup was 0.22.1; installed pinned client/server in separate environments|
|Port 8000 occupied|Unrelated Python service did not return model JSON; left it alone and used localhost:8001|
|Managed Surya startup failed|UI held 7,398 MiB, leaving 8.08 GiB vs 13.93 GiB required; isolated Qwen worker fixed retention|
|Session names caused confusion|`notes-tunnel` ended up running Python UI, `web-tunnel` cloudflared; inspect live commands and listeners, not names|

Current execution verified memory returning to 42 MiB after two completed runs. Restarting the UI changes its application token; restarting a Quick Tunnel changes its URL. Never record tokens in Git. A temporary URL is not permanent hosting, and traffic passes through Cloudflare. Current environments and commands: [operations runbook](../docs/OPERATIONS.md).
