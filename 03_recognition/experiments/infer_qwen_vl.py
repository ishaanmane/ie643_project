"""Run Qwen2.5-VL (base, or base + our LoRA adapter) over a split and save Markdown.

Run from the repo root on a GPU machine. NOT yet run on a GPU.

Zero-shot baseline on validation pages:
    python 03_recognition/experiments/infer_qwen_vl.py --split data/val.jsonl --out preds/base_val
With the fine-tuned adapter:
    python 03_recognition/experiments/infer_qwen_vl.py --split data/val.jsonl --adapter /kaggle/working/qwen_lora --out preds/lora_val
Resumable: pages that already have a .md in --out are skipped.
Score with: python 05_evaluation/evaluate.py --pred preds/base_val --split data/val.jsonl
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load_image, load_records  # noqa: E402


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--split", default="data/val.jsonl")
    p.add_argument("--adapter", default="", help="folder saved by train_qwen_vl.py")
    p.add_argument("--model", default="unsloth/Qwen2.5-VL-7B-Instruct-bnb-4bit")
    p.add_argument("--out", required=True)
    p.add_argument("--max-pixels", type=int, default=1_000_000)
    p.add_argument("--max-new-tokens", type=int, default=2048)
    p.add_argument("--limit", type=int, default=0)
    a = p.parse_args()

    from unsloth import FastVisionModel  # import unsloth first

    model, tokenizer = FastVisionModel.from_pretrained(a.adapter or a.model, load_in_4bit=True)
    FastVisionModel.for_inference(model)
    os.makedirs(a.out, exist_ok=True)

    recs = load_records(a.split, a.limit)
    for i, r in enumerate(recs, 1):
        dst = os.path.join(a.out, r["id"] + ".md")
        if os.path.exists(dst):
            continue
        image = load_image(r["image_path"], a.max_pixels)
        messages = [{"role": "user", "content": [
            {"type": "image"}, {"type": "text", "text": r["prompt"]}]}]
        text = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
        inputs = tokenizer(image, text, add_special_tokens=False,
                           return_tensors="pt").to("cuda")
        out = model.generate(**inputs, max_new_tokens=a.max_new_tokens,
                             use_cache=True, do_sample=False)
        pred = tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
        with open(dst, "w") as fh:
            fh.write(pred)
        print(f"[{i}/{len(recs)}] {r['id']} ({len(pred)} chars)")


if __name__ == "__main__":
    main()
