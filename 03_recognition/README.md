# Step 3 - Recognition (Qwen2.5-VL-7B, 4-bit QLoRA, Markdown output)

Final model: **`clean` variant** — preprocessed page + `PAGE_PROMPT` -> Markdown with `$...$`,
`$$...$$` and `[Diagram: ...]`. Target is `data/annotations/<page>.md`; only the answer is in the loss.
Plain `transformers` + `peft`, bf16, on the local GPU machine (RTX 5060 Ti 16 GB).

## Run (GPU machine, in tmux)

```bash
python3 03_recognition/finetune_qwen25vl.py --dry-run     # data checks, no model
python3 03_recognition/finetune_qwen25vl.py --pilot       # 5 steps: memory + speed
python3 03_recognition/finetune_qwen25vl.py --test        # full run
```

The full run: zero-shot baseline on val and test -> 3 epochs on train (303 pages), best epoch
by validation loss -> fine-tuned predictions on val and test -> scores. Everything is under one
`--run-name` (default `final_clean`): adapter `runs/final_clean/final_adapter/`, predictions
`preds/final_clean_{base_val,val,base_test,test}/`, scores next to them as `*_score.txt`.
An existing adapter is never overwritten; predictions resume after a crash.

| File | Purpose |
|---|---|
| `finetune_qwen25vl.py` | The run above |
| `qwen_data.py` | Image resize to multiples of 28, chat examples, answer-only label masking |
| `requirements-train.txt` | Training stack (install PyTorch for CUDA 12.8+ first) |
| `experiments/` | Notebook version, earlier Unsloth/Kaggle scripts (`common.py`, `train_qwen_vl.py`, `infer_qwen_vl.py`) |

Earlier result (old split, 25 val pages): clean CER 0.277, text CER 0.222; `boxed_json` was worse
and dropped (see `findings/04_recognition_finetuning.md`). These are superseded by the `final_clean` run.

## Memory knob: image size

Qwen2.5-VL uses one visual token per 28x28 pixels. Our processed pages are about 2.6 million pixels (about 3300 tokens), which is probably too much for a 16 GB T4. `--max-pixels` shrinks the page (aspect ratio kept):

| `--max-pixels` | Example page | Visual tokens |
|---|---|---|
| 500,000 | 612x816 | about 640 |
| 1,000,000 | 865x1155 | about 1270 |
| 1,500,000 | 1060x1414 | about 1910 |

Smaller is cheaper but chalkboard handwriting gets harder to read. The pilot picks the value.

