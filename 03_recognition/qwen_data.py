"""Data side of Qwen2.5-VL fine-tuning: pages -> chat examples -> masked training batches.

Used by finetune_qwen25vl.ipynb. Kept in a module so it can be tested without a GPU.

Variants (what the model sees; the target is always data/annotations/<page>.md):
  clean       preprocessed page                 + PAGE_PROMPT
  boxed       page with Surya boxes drawn on    + BOXED_PROMPT
  boxed_json  page with Surya boxes drawn on    + BOXED_PROMPT + the page's layout tags
              as JSON in Qwen2.5-VL's own grounding format
              ({"bbox_2d": [x1, y1, x2, y2], "label": ...}, pixels of the image as fed)
"""
import json
import math
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "00_dataset"))
from prompts import BOXED_PROMPT, PAGE_PROMPT  # noqa: E402

DATA = os.path.join(ROOT, "data")
IMAGE_DIRS = {"clean": "processed", "boxed": "processed_boxed", "boxed_json": "processed_boxed"}
LAYOUT_INTRO = ("\nLayout blocks detected on this page, in reading order "
                "(bbox_2d is [x1, y1, x2, y2] in pixels of this image):\n")
PATCH = 28  # Qwen2.5-VL: one visual token per 28x28 pixels


def page_ids(split):
    """Pages in a split, from data/splits.json (the ?? pages are already left out)."""
    return json.load(open(os.path.join(DATA, "splits.json")))["splits"][split]


def load_page_image(path, max_pixels):
    """RGB image whose sides are multiples of 28 and whose area is <= max_pixels.

    Doing the resize here (instead of leaving it to the processor) means we know the
    exact size the model sees, so the layout boxes can be given in its pixels.
    """
    im = Image.open(path).convert("RGB")
    w, h = im.size
    s = min(1.0, math.sqrt(max_pixels / (w * h)))
    nw = max(PATCH, int(w * s) // PATCH * PATCH)
    nh = max(PATCH, int(h * s) // PATCH * PATCH)
    return im.resize((nw, nh), Image.LANCZOS) if (nw, nh) != (w, h) else im


def layout_blocks(tags, width, height):
    """Tags (boxes 0-1000) -> Qwen grounding format in pixels of the resized image."""
    out = []
    for b in sorted(tags["blocks"], key=lambda b: b["order"]):
        if b["type"] == "blank":
            continue
        x0, y0, x1, y1 = b["bbox"]
        out.append({"bbox_2d": [round(x0 * width / 1000), round(y0 * height / 1000),
                                round(x1 * width / 1000), round(y1 * height / 1000)],
                    "label": b["type"]})
    return out


def build_example(page, variant, max_pixels, with_answer=True):
    image = load_page_image(os.path.join(DATA, IMAGE_DIRS[variant], page + ".jpg"), max_pixels)
    if variant == "clean":
        prompt = PAGE_PROMPT
    else:
        prompt = BOXED_PROMPT
    if variant == "boxed_json":
        tags = json.load(open(os.path.join(DATA, "tags", page + ".json")))
        blocks = layout_blocks(tags, *image.size)
        prompt += LAYOUT_INTRO + json.dumps(blocks, separators=(",", ":"))
    messages = [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": prompt}]}]
    if with_answer:
        answer = open(os.path.join(DATA, "annotations", page + ".md")).read().strip()
        messages.append({"role": "assistant", "content": [{"type": "text", "text": answer}]})
    return {"id": page, "images": [image], "messages": messages}


def check_inputs(variant, splits=("train", "val", "test")):
    """List of problems that would break or corrupt training for this variant."""
    problems = []
    for split in splits:
        for p in page_ids(split):
            img = os.path.join(DATA, IMAGE_DIRS[variant], p + ".jpg")
            if not os.path.exists(img):
                problems.append(f"{p}: no image {img}")
            if not os.path.exists(os.path.join(DATA, "annotations", p + ".md")):
                problems.append(f"{p}: no annotation")
            if variant == "boxed_json":
                tp = os.path.join(DATA, "tags", p + ".json")
                if not os.path.exists(tp):
                    problems.append(f"{p}: no tags")
                elif os.path.exists(img):
                    size = list(Image.open(os.path.join(DATA, "processed", p + ".jpg")).size)
                    if json.load(open(tp))["image_size"] != size:
                        problems.append(f"{p}: tags were made for a different version of the image")
    return problems


def find_last(seq, sub):
    for i in range(len(seq) - len(sub), -1, -1):
        if seq[i:i + len(sub)] == sub:
            return i
    return -1


def make_collate_fn(processor):
    """Batch builder that trains only on the answer.

    Everything up to and including '<|im_start|>assistant\\n' (system prompt, image
    tokens, instruction, layout JSON) gets label -100, as does padding. The answer and
    its closing <|im_end|> are learned, so the model also learns where to stop.
    """
    start = processor.tokenizer.encode("<|im_start|>assistant\n", add_special_tokens=False)
    pad_id = processor.tokenizer.pad_token_id

    def collate(examples):
        texts = [processor.apply_chat_template(e["messages"], tokenize=False) for e in examples]
        batch = processor(text=texts, images=[e["images"] for e in examples],
                          return_tensors="pt", padding=True)
        labels = batch["input_ids"].clone()
        labels[labels == pad_id] = -100
        for i, ids in enumerate(batch["input_ids"].tolist()):
            pos = find_last(ids, start)
            if pos < 0:
                raise ValueError(f"assistant marker not found in example {examples[i]['id']}")
            labels[i, :pos + len(start)] = -100
        batch["labels"] = labels
        return batch

    return collate
