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
- **Main weakness of `boxed_json`: side notes dropped.** `lec07_page011` keeps both equations, the algorithm and the stopping rule, but misses "N: very large → overload", "w⁰" and the step-length aside. Pages `011` and `012` are about 0.65 of the label length. The clean run below retained more of those notes. This comparison does not isolate boxes from the accompanying layout JSON and prompt changes.
- **Diagram descriptions** are free text, so correct descriptions in other words still count as errors (for example `lec07_page004`, CER 0.47, structure correct). Text-only CER is the fairer number.
- **Blank page** (`lec07_page020`): short note instead of the label's longer note; harmless.

## Comparison: layout input vs clean page

Same 25 validation pages, same settings; `clean` = plain preprocessed page, no boxes, no JSON.

| Fine-tuned | CER | WER | text-only CER | equation exact match |
|---|---|---|---|---|
| `boxed_json` | 0.287 | 0.469 | 0.258 | 0.273 |
| `clean` | **0.277** | 0.485 | **0.222** | 0.244 |

| By source | `boxed_json` | `clean` |
|---|---|---|
| Chalkboard: CER / text-only CER / eq. match | 0.290 / 0.286 / 0.344 | 0.286 / 0.238 / 0.292 |
| Digital ink: CER / text-only CER / eq. match | 0.277 / 0.168 / 0.083 | 0.249 / 0.171 / 0.117 |

Zero-shot baselines: `boxed_json` CER 0.712, `clean` 0.776; layout hints help the untrained model on chalkboards but fine-tuning removes the gap.

**Observed association: the boxed variant drops more side notes.** Output length on the pages with side notes:

| Page | Label | `boxed_json` | `clean` |
|---|---|---|---|
| `lec07_page011` | 557 | 361 (65%) | 545 (98%) |
| `lec07_page012` | 558 | 375 (67%) | 542 (97%) |
| `lec07_page004` | 398 | 309 (78%) | 328 (82%) |

The inspected boxed outputs omit content outside Surya boxes that the clean model retains. Attention to boxed regions is a plausible explanation, not a controlled causal conclusion.

**Decision: `clean` for extraction.** Equal or better on text, keeps side notes, and needs no Surya step before Qwen at inference. Surya is still used for figure crops and reading order in the PDF stage. Overall differences are single runs on 25 pages, so small gaps (0.01-0.04) have not been validated across repeated training runs; to be confirmed on the test split.

## Caveats

Validation only (25 pages, two units, no notebook photos); test split not scored until its labels are checked. Labels themselves are unverified.

## Upload integration status

The same clean adapter is now used in the working upload interface; no retraining was needed. Tested Surya v2 runs separately for crop coordinates, then a short-lived Qwen worker performs recognition and exits to release GPU memory. See [upload findings](08_upload_interface_and_reconstruction.md). GPU uploads and PDF reviews are integration evidence, not additional CER or generalization measurements.
