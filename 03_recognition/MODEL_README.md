# Notes2PDF recognition model (IE643 course project)

LoRA adapter for **Qwen/Qwen2.5-VL-7B-Instruct** that turns a preprocessed page of handwritten
lecture notes into Markdown (`$...$` / `$$...$$` LaTeX, `[Diagram: ...]` for drawings).
Code: https://github.com/ishaanmane/ie643_project/tree/final (`03_recognition/`, run name `final_clean`).

## Training
- Data: 303 training pages (IE643 chalkboard, MLT digital ink, IE802 and HumynLabs notebook photos),
  split by lecture/week/notebook; best epoch chosen on 31 validation pages.
- 4-bit NF4 QLoRA (double quantisation), bf16 compute; LoRA rank 16, alpha 32, dropout 0.05 on
  q, k, v, o, gate, up, down projections (47.6M trainable parameters).
- Loss on the answer tokens only; paged AdamW 8-bit, lr 1e-4 cosine, 3% warm-up, 3 epochs,
  batch 1 x 8 gradient accumulation; images resized to at most 1M pixels (sides multiples of 28).
- Hardware: NVIDIA RTX 5060 Ti 16 GB, 53 min, peak 10.8 GB.

## Test results (76 pages)
Corpus CER 0.332, NED 0.311, token F1 0.855, normalised equation F1 0.338 (zero-shot base:
0.915 / 0.596 / 0.623 / 0.143). Details: `results/recognition_experiments.md`.

## Use
```python
from transformers import AutoProcessor, BitsAndBytesConfig, Qwen2_5_VLForConditionalGeneration
from peft import PeftModel
import torch
bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
                         bnb_4bit_compute_dtype=torch.bfloat16)
base = Qwen2_5_VLForConditionalGeneration.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct",
        quantization_config=bnb, device_map={"": 0})
model = PeftModel.from_pretrained(base, "final_adapter")
processor = AutoProcessor.from_pretrained("final_adapter", max_pixels=1_000_000)
```
Prompt: `PAGE_PROMPT` in `00_dataset/prompts.py`; greedy decoding, repetition penalty 1.05.
Or run the whole pipeline: `python3 06_interface/pipeline.py page.jpg --out out/x --adapter final_adapter`.

Versions used: PyTorch (CUDA 12.8), transformers 4.57.6, peft 0.21.2, bitsandbytes 0.50.2.
The base model weights are not included (download from Hugging Face; Qwen licence applies).
`SHA256SUMS` lists checksums of the adapter files.

## Download
GitHub release: https://github.com/ishaanmane/ie643_project/releases/tag/model-final-clean
(`notes2pdf_final_clean_adapter.zip`, 172 MB, SHA-256
`bf8a4c5f1ae3adc633ace079094e8d3df2dea42a62a0ca91c7119c7a30a3bf7a`).
