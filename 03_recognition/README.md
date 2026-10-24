# Step 3 - Recognition (Qwen2.5-VL fine-tuning, Markdown output)

**Main route (local GPU, e.g. RTX 5060 Ti 16 GB): [finetune_qwen25vl.ipynb](finetune_qwen25vl.ipynb).** Plain `transformers` + `peft` QLoRA, bf16. Variants: `boxed_json` (page with Surya boxes + the page's layout tags as JSON in Qwen's `bbox_2d` format), `boxed`, `clean`; target is always `data/annotations/<page>.md`, and only the answer is in the loss. Data logic is in `qwen_data.py` and was tested with Qwen's real processor (no hidden resize, correct label masking, max 3250 tokens per example). Training itself has not been run yet. Install: `requirements-train.txt` (after PyTorch for CUDA 12.8+).

The Unsloth scripts below were the earlier Kaggle-T4 route and are kept for reference.

Fine-tune Qwen2.5-VL-7B with 4-bit LoRA to turn a page image into structured Markdown (LaTeX for equations), using `data/train.jsonl` (324 pages). Design: [../docs/PIPELINE.md](../docs/PIPELINE.md).

**Status: scripts written, not yet run on a GPU.** The data loader and `05_evaluation/evaluate.py` were tested here without a GPU; the Unsloth/TRL calls follow Unsloth's published vision notebooks and may need a small fix on the first run.

| File | Purpose |
|---|---|
| `common.py` | Read the JSONL, shrink pages to a pixel budget (`--max-pixels`), build chat examples |
| `train_qwen_vl.py` | LoRA fine-tune; `--max-steps 20` runs a short pilot that reports peak GPU memory and seconds per step |
| `infer_qwen_vl.py` | Run the base model or base + adapter over a split, write one `.md` per page (resumable) |
| `../05_evaluation/evaluate.py` | CER, WER, text-only CER and equation exact-match, by source |

## Memory knob: image size

Qwen2.5-VL uses one visual token per 28x28 pixels. Our processed pages are about 2.6 million pixels (about 3300 tokens), which is probably too much for a 16 GB T4. `--max-pixels` shrinks the page (aspect ratio kept):

| `--max-pixels` | Example page | Visual tokens |
|---|---|---|
| 500,000 | 612x816 | about 640 |
| 1,000,000 | 865x1155 | about 1270 |
| 1,500,000 | 1060x1414 | about 1910 |

Smaller is cheaper but chalkboard handwriting gets harder to read. The pilot picks the value.

## Steps

0. **Before anything:** `data/processed/` must exist and be the fixed version (`git pull`, then `python3 01_preprocessing/batch_preprocess.py --workers 4 --force`). The JSONL files point at it.
1. **Kaggle setup** (GPU T4, Internet On): clone the repo, create a Python 3.11 environment, install Unsloth, TRL and jiwer. Kaggle's default Python is 3.13, which Unsloth may not support.
2. **Pilot** at 500k, 1M and 1.5M pixels, 20 steps each, with `--grad-accum 1` (so seconds per step is seconds per page; training time is that times 324 times the epochs). Pick the largest size that fits with headroom; note the seconds per step and compute the real training time.
3. **Zero-shot baseline:** `infer_qwen_vl.py` with no adapter on the 26 validation pages, then `evaluate.py`. This is the number the fine-tuned model must beat.
4. **Fine-tune:** 3 epochs on the 324 training pages. Adapters are saved after every epoch to `/kaggle/working/qwen_lora`. Download or upload them before the session ends, because Kaggle wipes the disk.
5. **Evaluate the adapter** on validation with the same two commands, and compare with step 3.
6. **Test split** only once the test labels have been checked by hand (`data/VERIFICATION.md`).
7. **Optional:** repeat steps 4 and 5 on binarized images (`01_preprocessing/sauvola.py`) and compare.

Defaults: LoRA rank 16, learning rate 2e-4, batch 1 with gradient accumulation 8, fp16 (the T4 has no bf16), loss on the answer only, no evaluation inside the training loop.
