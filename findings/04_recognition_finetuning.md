# 04 · Recognition: fine-tuning Qwen2.5-VL-7B

Code: `03_recognition/finetune_qwen25vl.py` (command line) and `finetune_qwen25vl.ipynb` (same steps); data logic in `qwen_data.py`.

## Design

| Item | Choice |
|---|---|
| Base model | `Qwen/Qwen2.5-VL-7B-Instruct` (Hugging Face weights; the Ollama copy is a GGUF file for inference and cannot be trained) |
| Input (variant `boxed_json`) | Preprocessed page with Surya boxes drawn + instruction + the page's layout tags as JSON in Qwen's grounding format (`{"bbox_2d":[x1,y1,x2,y2],"label":...}`, pixels of the image as fed, reading order) |
| Target | The page's Markdown label |
| Loss | Answer only: system prompt, image, instruction and JSON masked; the closing `<|im_end|>` is learned so the model knows where to stop |
| Image size | At most 1,000,000 pixels, sides multiples of 28: about 1,215-1,260 image tokens; the processor does no further resize (verified) |
| Sequence length | Max 3,450 tokens (`boxed_json`), 2,246 (`clean`); longest answer 942 |
| Method | 4-bit NF4 QLoRA (double quantisation), bf16, LoRA rank 16 / alpha 32 / dropout 0.05 on q, k, v, o, gate, up, down: 47.6M trainable parameters (0.57%) |
| Training | 318 pages, batch 1 x 8 accumulation, 3 epochs = 120 steps, lr 1e-4 cosine, 3% warmup, paged AdamW 8-bit, gradient checkpointing; best epoch by validation loss |
| Hardware | RTX 5060 Ti 16 GB (Blackwell), PyTorch for CUDA 12.8, transformers 4.57.6, peft 0.21.2, bitsandbytes 0.50.2 |

Two corrections before the GPU run: `prepare_model_for_kbit_training` was removed (it upcasts embeddings and output layer to fp32, about 2 GB of VRAM for nothing in bf16), and generation forces `use_cache=True` (gradient checkpointing had switched the cache off).

## Pilot and run

| | Pilot (5 steps) | Full run (120 steps) |
|---|---|---|
| Model in VRAM | 5.5 GB | 5.5 GB |
| Peak VRAM | 11.4 GB | 13.2 GB |
| Speed | 31 s/step (8 pages) | about 62 min total |

Validation loss: epoch 1 0.484 → epoch 2 0.429 → epoch 3 0.418 (kept). Still improving, gains shrinking; no overfitting.

## Results (25 validation pages, `boxed_json`)

| | CER | WER | text-only CER | equation exact match |
|---|---|---|---|---|
| Baseline (zero-shot) | 0.712 | 0.927 | 0.892 | 0.061 |
| **Fine-tuned** | **0.287** | **0.469** | **0.258** | **0.273** |

| Source | Baseline CER → fine-tuned | Equation match |
|---|---|---|
| Chalkboard (19 pages) | 0.745 → 0.290 | 0.083 → 0.344 |
| Digital ink (6 pages) | 0.607 → 0.277 | 0.000 → 0.083 |

Generation takes 1-11 s per page.

## Error analysis

- **Output completeness:** 17 of 25 pages are 0.88-1.22 times the label length. The baseline's long outputs (for example 1,218 characters for a 398-character label) were verbose; the fine-tuned model learned the label style.
- **Near-perfect pages:** `lec07_page001` (CER 0.01), `005` (0.03), `015` (0.02), `019` (0.00). Similarity to the closest train page 0.08, 0.33, 0.15, 0.39: mostly genuine reading, with some topic overlap on two of them.
- **Main weakness: side notes dropped.** `lec07_page011` keeps both equations, the algorithm and the stopping rule, but misses "N: very large → overload", "w⁰" and the step-length aside. Pages `011` and `012` are about 0.65 of the label length. Untested hypothesis: the model may skip content Surya did not box; the clean run will show.
- **Diagram descriptions** are free text, so correct descriptions in other words still count as errors (for example `lec07_page004`, CER 0.47, structure correct). Text-only CER is the fairer number.
- **Blank page** (`lec07_page020`): short note instead of the label's longer note; harmless.

## In progress

Comparison run `--variant clean` (no boxes, no JSON), same pages and settings, to see whether layout input helps, especially on side notes.

## Caveats

Validation only (25 pages, two units, no notebook photos); test split not scored until its labels are checked. Labels themselves are unverified.
