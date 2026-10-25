"""LoRA fine-tune Qwen2.5-VL-7B (4-bit) on data/train.jsonl with Unsloth.

Run from the repo root on a GPU machine (Kaggle T4). NOT yet run: the Unsloth/TRL API
calls follow Unsloth's published vision notebooks and may need a small adjustment.

Pilot (find the largest image size that fits, and the seconds per step):
    python 03_recognition/experiments/train_qwen_vl.py --max-steps 20 --limit 40 --grad-accum 1 --max-pixels 1000000
(with --grad-accum 1, sec/step is seconds per page: full training time = sec/step x 324 x epochs)
Real run:
    python 03_recognition/experiments/train_qwen_vl.py --epochs 3 --max-pixels 1000000
Saves the LoRA adapter (a few hundred MB) to --out.
"""
import argparse
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load_records, train_example  # noqa: E402


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--train", default="data/train.jsonl")
    p.add_argument("--model", default="unsloth/Qwen2.5-VL-7B-Instruct-bnb-4bit")
    p.add_argument("--max-pixels", type=int, default=1_000_000,
                   help="pixel budget per page; 1,000,000 is about 1300 visual tokens")
    p.add_argument("--epochs", type=float, default=3)
    p.add_argument("--max-steps", type=int, default=0, help="pilot: stop after N optimizer steps")
    p.add_argument("--limit", type=int, default=0, help="use only the first N training pages")
    p.add_argument("--lr", type=float, default=2e-4)
    p.add_argument("--grad-accum", type=int, default=8)
    p.add_argument("--rank", type=int, default=16)
    p.add_argument("--out", default="/kaggle/working/qwen_lora")
    p.add_argument("--no-response-only", action="store_true",
                   help="also compute loss on the prompt tokens (fallback if masking errors)")
    a = p.parse_args()

    from unsloth import FastVisionModel, is_bf16_supported  # import unsloth first
    from unsloth.trainer import UnslothVisionDataCollator
    from trl import SFTConfig, SFTTrainer
    import torch

    recs = load_records(a.train, a.limit)
    print(f"{len(recs)} training pages, max_pixels={a.max_pixels}")
    data = [train_example(r, a.max_pixels) for r in recs]

    model, tokenizer = FastVisionModel.from_pretrained(
        a.model, load_in_4bit=True, use_gradient_checkpointing="unsloth")
    model = FastVisionModel.get_peft_model(
        model, finetune_vision_layers=True, finetune_language_layers=True,
        finetune_attention_modules=True, finetune_mlp_modules=True,
        r=a.rank, lora_alpha=a.rank, lora_dropout=0, bias="none", random_state=3407)
    FastVisionModel.for_training(model)

    collator_kwargs = {}
    if not a.no_response_only:
        collator_kwargs = dict(train_on_responses_only=True,
                               instruction_part="<|im_start|>user\n",
                               response_part="<|im_start|>assistant\n")
    collator = UnslothVisionDataCollator(model, tokenizer, **collator_kwargs)

    # Sanity check: how many visual tokens does the first page really become?
    batch = collator([data[0]])
    print("input_ids", tuple(batch["input_ids"].shape),
          "image_grid_thw", batch.get("image_grid_thw"),
          "(visual tokens = t*h*w / 4)")

    trainer = SFTTrainer(
        model=model, tokenizer=tokenizer, data_collator=collator, train_dataset=data,
        args=SFTConfig(
            per_device_train_batch_size=1, gradient_accumulation_steps=a.grad_accum,
            warmup_steps=5, num_train_epochs=a.epochs,
            max_steps=a.max_steps if a.max_steps else -1,
            learning_rate=a.lr, fp16=not is_bf16_supported(), bf16=is_bf16_supported(),
            logging_steps=1, optim="adamw_8bit", weight_decay=0.01,
            lr_scheduler_type="linear", seed=3407, output_dir=a.out, report_to="none",
            save_strategy="no" if a.max_steps else "epoch",
            remove_unused_columns=False, dataset_text_field="",
            dataset_kwargs={"skip_prepare_dataset": True},
            max_length=8192))  # long enough that image tokens are never truncated

    t0 = time.time()
    result = trainer.train()
    secs = time.time() - t0
    steps = result.global_step
    peak = torch.cuda.max_memory_allocated() / 2**30
    print(f"SUMMARY max_pixels={a.max_pixels} steps={steps} "
          f"sec/step={secs / max(steps, 1):.1f} peak_gpu_gb={peak:.1f} "
          f"final_loss={result.training_loss:.3f}")
    if not a.max_steps:
        model.save_pretrained(a.out)
        tokenizer.save_pretrained(a.out)
        print("adapter saved to", a.out)


if __name__ == "__main__":
    main()
