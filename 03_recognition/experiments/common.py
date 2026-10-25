"""Shared helpers: read our chat-format JSONL and prepare images for Qwen2.5-VL."""
import json
import math
import os

from PIL import Image


def load_records(jsonl_path, limit=0):
    """One dict per line: id, image_path, prompt, answer (the ground-truth Markdown)."""
    recs = []
    with open(jsonl_path) as fh:
        for line in fh:
            user, assistant = json.loads(line)["messages"]
            image_path = next(c["image"] for c in user["content"] if c["type"] == "image")
            prompt = next(c["text"] for c in user["content"] if c["type"] == "text")
            answer = assistant["content"]
            if not isinstance(answer, str):
                answer = "".join(c.get("text", "") for c in answer)
            recs.append({"id": os.path.splitext(os.path.basename(image_path))[0],
                         "image_path": image_path, "prompt": prompt, "answer": answer})
            if limit and len(recs) >= limit:
                break
    return recs


def load_image(path, max_pixels):
    """Open as RGB and shrink (keeping aspect ratio) so w*h <= max_pixels.

    Qwen2.5-VL spends one visual token per 28x28 pixels, so this is the knob that
    controls memory. Never upscales.
    """
    im = Image.open(path).convert("RGB")
    w, h = im.size
    if w * h > max_pixels:
        s = math.sqrt(max_pixels / (w * h))
        im = im.resize((max(28, int(w * s)), max(28, int(h * s))), Image.LANCZOS)
    return im


def train_example(rec, max_pixels):
    """Chat example in the format the Unsloth vision collator expects."""
    return {"messages": [
        {"role": "user", "content": [
            {"type": "text", "text": rec["prompt"]},
            {"type": "image", "image": load_image(rec["image_path"], max_pixels)}]},
        {"role": "assistant", "content": [{"type": "text", "text": rec["answer"]}]},
    ]}
