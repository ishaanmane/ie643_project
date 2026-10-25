"""Fine-tune Qwen2.5-VL-7B (4-bit QLoRA) on our pages: command-line version of
finetune_qwen25vl.ipynb, for running on a remote GPU machine inside tmux.

Run from the repo root:
    python3 03_recognition/finetune_qwen25vl.py --dry-run           # checks + examples only, no GPU
    python3 03_recognition/finetune_qwen25vl.py --pilot             # 5 training steps: memory and speed
    python3 03_recognition/finetune_qwen25vl.py --test              # real run: baseline, train, val + test scores

Each run is isolated by --run-name (default final_clean): adapter in runs/<run-name>/,
predictions in preds/<run-name>_{base_val,val,base_test,test}/. An existing final adapter is never
overwritten. Predictions are resumable, so a crashed run continues where it stopped.
Model choice uses val only (best epoch by validation loss); test is scored once, at the end.

Input: page image (with Surya boxes for boxed / boxed_json) + instruction (+ the page's
layout tags as JSON for boxed_json). Target: data/annotations/<page>.md. Only the
answer is in the loss. Outputs: runs/<run-name>/ (adapter), preds/<run-name>_*/ (predictions).
"""
import argparse
import csv
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import qwen_data as Q  # noqa: E402

D = os.path.join(ROOT, "data")
MODEL_ID = "Qwen/Qwen2.5-VL-7B-Instruct"


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def check_data(variant):
    rows = list(csv.DictReader(open(os.path.join(D, "processed", "preprocess_report.csv"))))
    whitened = sum(r.get("crop") == "whiten+brightness" for r in rows)
    log(f"preprocessed pages: {len(rows)}, desk-whitened: {whitened} (19 = current version)")
    if len(rows) != 410 or "bg_removed" not in rows[0]:
        sys.exit("STOP: data/processed is not the current version; rerun 01_preprocessing/batch_preprocess.py --force")
    problems = Q.check_inputs(variant)
    log(f"input problems for {variant}: {len(problems)}")
    if problems:
        for p in problems[:10]:
            print("   ", p)
        sys.exit("STOP: fix the problems above (missing images/tags, or tags from another image version)")
    for split in ("train", "val", "test"):
        log(f"{split}: {len(Q.page_ids(split))} pages")


def predict(model, processor, pages, out_dir, variant, max_pixels, max_new_tokens):
    import torch
    os.makedirs(out_dir, exist_ok=True)
    model.eval()
    for i, p in enumerate(pages, 1):
        path = os.path.join(out_dir, p + ".md")
        if os.path.exists(path):
            continue  # resumable
        ex = Q.build_example(p, variant, max_pixels, with_answer=False)
        text = processor.apply_chat_template(ex["messages"], tokenize=False, add_generation_prompt=True)
        inputs = processor(text=[text], images=[ex["images"]], return_tensors="pt").to(model.device)
        t = time.time()
        with torch.no_grad():
            out = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False,
                                 repetition_penalty=1.05, use_cache=True)
        pred = processor.batch_decode(out[:, inputs["input_ids"].shape[1]:], skip_special_tokens=True)[0]
        with open(path, "w") as fh:
            fh.write(pred)
        log(f"[{i}/{len(pages)}] {p}: {len(pred)} chars, {time.time() - t:.0f}s")


def score(pred_dir, title, split="val"):
    r = subprocess.run([sys.executable, os.path.join(ROOT, "05_evaluation", "evaluate.py"),
                        "--pred", pred_dir, "--split", os.path.join(D, split + ".jsonl")],
                       cwd=ROOT, capture_output=True, text=True)
    text = f"\n=== {title} ===\n{r.stdout or r.stderr}"
    print(text, flush=True)
    with open(os.path.join(pred_dir + "_score.txt"), "w") as fh:
        fh.write(text)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--variant", default="clean", choices=["clean", "boxed_json", "boxed"],
                   help="clean = final; boxed variants are the dropped experiment")
    p.add_argument("--run-name", default="final_clean")
    p.add_argument("--test", action="store_true", help="also baseline + fine-tuned scores on the test split")
    p.add_argument("--pilot", action="store_true", help="5 training steps to measure memory and speed")
    p.add_argument("--dry-run", action="store_true", help="checks and example building only, no model")
    p.add_argument("--max-pixels", type=int, default=1_000_000)
    p.add_argument("--epochs", type=float, default=3)
    p.add_argument("--lr", type=float, default=1e-4)
    p.add_argument("--grad-accum", type=int, default=8)
    p.add_argument("--lora-r", type=int, default=16)
    p.add_argument("--max-new-tokens", type=int, default=1280)
    p.add_argument("--eval-pages", type=int, default=0, help="val pages to score (0 = all)")
    p.add_argument("--skip-baseline", action="store_true")
    a = p.parse_args()

    out_dir = os.path.join(ROOT, "runs", a.run_name)
    if os.path.exists(os.path.join(out_dir, "final_adapter")) and not a.dry_run:
        sys.exit(f"STOP: {out_dir}/final_adapter exists; choose another --run-name")
    val_pages = Q.page_ids("val")[:a.eval_pages or None]
    test_pages = Q.page_ids("test")
    pred = lambda name: os.path.join(ROOT, "preds", f"{a.run_name}_{name}")
    base_pred, ft_pred = pred("base_val"), pred("val")

    # 1. data
    check_data(a.variant)

    # 2. processor + examples
    from transformers import AutoProcessor
    processor = AutoProcessor.from_pretrained(MODEL_ID, min_pixels=4 * 28 * 28, max_pixels=a.max_pixels)
    collate = Q.make_collate_fn(processor)
    train_ds = [Q.build_example(x, a.variant, a.max_pixels) for x in Q.page_ids("train")]
    val_ds = [Q.build_example(x, a.variant, a.max_pixels) for x in Q.page_ids("val")]
    lens = [(b["input_ids"].shape[1], int((b["labels"] != -100).sum())) for b in (collate([e]) for e in train_ds)]
    log(f"examples: {len(train_ds)} train, {len(val_ds)} val | tokens/example max {max(l[0] for l in lens)}"
        f" | answer tokens max {max(l[1] for l in lens)}")
    ex = train_ds[0]
    log(f"example {ex['id']}: image {ex['images'][0].size}, prompt starts: "
        f"{ex['messages'][0]['content'][1]['text'][:120]!r}")
    if a.dry_run:
        log("dry run: stopping before loading the model")
        return

    # 3. GPU + model
    import torch
    from transformers import BitsAndBytesConfig, Qwen2_5_VLForConditionalGeneration
    if not torch.cuda.is_available():
        sys.exit("STOP: no GPU visible to PyTorch")
    free, total = torch.cuda.mem_get_info()
    log(f"GPU {torch.cuda.get_device_name(0)}, bf16 {torch.cuda.is_bf16_supported()}, "
        f"free {free / 2**30:.1f}/{total / 2**30:.1f} GB")
    if free / total < 0.85:
        log("WARNING: another process holds GPU memory (Ollama?): run `ollama stop qwen2.5vl:7b`")
    bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
                             bnb_4bit_compute_dtype=torch.bfloat16)
    t = time.time()
    model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
        MODEL_ID, quantization_config=bnb, torch_dtype=torch.bfloat16, device_map={"": 0},
        attn_implementation="sdpa")
    log(f"model loaded in {time.time() - t:.0f}s, GPU memory {torch.cuda.memory_allocated() / 2**30:.1f} GB")

    # 4. zero-shot baseline (cached in preds/, so later runs skip it)
    if not a.skip_baseline:
        predict(model, processor, val_pages, base_pred, a.variant, a.max_pixels, a.max_new_tokens)
        score(base_pred, f"BASELINE zero-shot ({a.variant}, {len(val_pages)} val pages)")
        if a.test and not a.pilot:
            predict(model, processor, test_pages, pred("base_test"), a.variant, a.max_pixels, a.max_new_tokens)
            score(pred("base_test"), f"BASELINE zero-shot ({a.variant}, {len(test_pages)} test pages)", "test")

    # 5. LoRA training
    from peft import LoraConfig, get_peft_model
    from transformers import Trainer, TrainingArguments
    model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
    model.enable_input_require_grads()  # needed for checkpointing with a frozen base
    model.config.use_cache = False
    model = get_peft_model(model, LoraConfig(
        r=a.lora_r, lora_alpha=2 * a.lora_r, lora_dropout=0.05, bias="none", task_type="CAUSAL_LM",
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]))
    model.print_trainable_parameters()
    args = TrainingArguments(
        output_dir=out_dir, num_train_epochs=a.epochs, max_steps=5 if a.pilot else -1,
        per_device_train_batch_size=1, per_device_eval_batch_size=1, gradient_accumulation_steps=a.grad_accum,
        gradient_checkpointing=True, gradient_checkpointing_kwargs={"use_reentrant": False},
        learning_rate=a.lr, lr_scheduler_type="cosine", warmup_ratio=0.03, max_grad_norm=1.0,
        bf16=True, optim="paged_adamw_8bit", logging_steps=1 if a.pilot else 5,
        eval_strategy="no" if a.pilot else "epoch", save_strategy="no" if a.pilot else "epoch",
        save_total_limit=2, load_best_model_at_end=not a.pilot, metric_for_best_model="eval_loss",
        greater_is_better=False, remove_unused_columns=False, dataloader_num_workers=0, report_to="none")
    trainer = Trainer(model=model, args=args, train_dataset=train_ds, eval_dataset=val_ds, data_collator=collate)
    torch.cuda.reset_peak_memory_stats()
    t0 = time.time()
    result = trainer.train()
    secs = (time.time() - t0) / max(result.global_step, 1)
    log(f"{result.global_step} steps, {secs:.0f} s/step ({a.grad_accum} pages), "
        f"peak GPU {torch.cuda.max_memory_allocated() / 2**30:.1f} GB")
    if a.pilot:
        steps = -(-len(train_ds) // a.grad_accum) * int(a.epochs)
        log(f"PILOT DONE. Full run: {steps} steps -> about {steps * secs / 3600:.1f} h of training "
            f"(+ validation loss after each epoch). Next: rerun without --pilot.")
        return

    # 6. save + score the fine-tuned model
    adapter = os.path.join(out_dir, "final_adapter")
    trainer.save_model(adapter)
    processor.save_pretrained(adapter)
    log("adapter saved to", adapter)
    model.config.use_cache = True
    predict(trainer.model, processor, val_pages, ft_pred, a.variant, a.max_pixels, a.max_new_tokens)
    score(base_pred, f"BASELINE zero-shot ({a.variant}, val)")
    score(ft_pred, f"FINE-TUNED ({a.variant}, val)")
    if a.test:
        predict(trainer.model, processor, test_pages, pred("test"), a.variant, a.max_pixels, a.max_new_tokens)
        score(pred("base_test"), f"BASELINE zero-shot ({a.variant}, test)", "test")
        score(pred("test"), f"FINE-TUNED ({a.variant}, test)", "test")


if __name__ == "__main__":
    main()
