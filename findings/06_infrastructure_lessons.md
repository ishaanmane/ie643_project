# 06 · Infrastructure and lessons

## Kaggle (Surya, preprocessing)

| Problem | Cause | Fix |
|---|---|---|
| `numba` failed to build | Kaggle's Python 3.13 | Separate Python 3.11 environments made with `uv` |
| `vllm==0.1.2` (2023) got installed and failed to compile | Installing `vllm` and `surya-ocr` together made the resolver backtrack | Two environments: one for vLLM, one for Surya |
| vLLM ran out of memory at start-up on the T4 | It reserves memory for video inputs | `--limit-mm-per-prompt '{"video": 0}' --max-num-batched-tokens 8192 --enforce-eager --dtype half` |
| `pkill -f 'vllm serve'` killed its own shell | The pattern matched the command itself | Kill by GPU process id from `nvidia-smi` |
| Session restarts wipe `/kaggle/working` | Updating a dataset input or idling restarts the session | Keep only small outputs; rebuild images from code |
| New zip still contained old files | `zip` adds to an existing archive | `rm -f` the zip first |
| Re-run used old code | `git clone` fails silently when the folder exists | `rm -rf` before cloning; print `git log -1` and compare |
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
