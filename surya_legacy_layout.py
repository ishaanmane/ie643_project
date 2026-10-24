"""
Surya Legacy Layout Generator (surya-ocr < 0.8.0)
-------------------------------------------------
Generates layout JSON files compatible with content_extractor.py using 
the local, pure-PyTorch version of Surya OCR (no Docker required).

Usage Examples:
    # Process a single image
    python surya_legacy_layout.py --image binarized_page.png --out-dir layout_outputs
    
    # Process a whole folder
    python surya_legacy_layout.py --image ./binarized_sauvola --out-dir layout_outputs
"""

import argparse
import json
import time
from pathlib import Path
from PIL import Image

try:
    from surya.detection import batch_text_detection
    from surya.layout import batch_layout_detection
    from surya.model.detection.model import load_model as load_det_model, load_processor as load_det_processor
    from surya.model.layout.model import load_model as load_layout_model
    from surya.model.layout.processor import load_processor as load_layout_processor
except ImportError:
    raise SystemExit("Error: surya-ocr not found or incompatible version.\n"
                     "Please ensure you ran: uv pip install 'surya-ocr<0.8.0'")

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}

# Map Surya's internal labels to the schema expected by content_extractor.py
LABEL_MAP = {
    "Caption": "caption",
    "Footnote": "footer",
    "Formula": "equation",
    "List-item": "list_item",
    "Page-footer": "footer",
    "Page-header": "header",
    "Picture": "image",
    "Figure": "image",
    "Section-header": "heading",
    "Table": "table",
    "Text": "paragraph",
    "Title": "title"
}

def parse_args():
    p = argparse.ArgumentParser(description="Legacy Surya Layout Detection to JSON")
    p.add_argument("-i", "--image", required=True, help="Path to a single image or a directory of images.")
    p.add_argument("-o", "--out-dir", default="layout_outputs", help="Output directory to store JSON maps.")
    p.add_argument("--overwrite", action="store_true", help="Overwrite existing output files.")
    return p.parse_args()

def collect_images(image_arg):
    path = Path(image_arg)
    if not path.exists():
        raise SystemExit(f"Error: Path not found: {path.resolve()}")
    if path.is_file():
        return [path]
    elif path.is_dir():
        images = sorted(p for p in path.iterdir() if p.suffix.lower() in IMAGE_EXTS)
        if not images:
            print(f"Warning: No images found in {path.resolve()}")
        return images
    return []

def main():
    args = parse_args()
    
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    images = collect_images(args.image)
    
    if not images:
        return

    print("Loading Surya Models (this takes a moment)...")
    t_load = time.time()
    det_model = load_det_model()
    det_processor = load_det_processor()
    layout_model = load_layout_model()
    layout_processor = load_layout_processor()
    print(f"Models loaded in {time.time() - t_load:.1f}s")

    total = len(images)
    done, skipped = 0, 0

    print(f"\nStarting Layout Analysis for {total} images...")

    for i, img_path in enumerate(images, start=1):
        out_path = out_dir / f"{img_path.stem}.json"

        if out_path.exists() and not args.overwrite:
            print(f"[{i}/{total}] Skip (already exists): {out_path.name}")
            skipped += 1
            continue

        print(f"[{i}/{total}] Processing: {img_path.name}...")
        t0 = time.time()

        try:
            # 1. Open image
            image = Image.open(img_path).convert("RGB")
            
            # 2. Line detection is required first in legacy Surya
            line_predictions = batch_text_detection([image], det_model, det_processor)
            
            # 3. Layout detection based on lines
            layout_predictions = batch_layout_detection([image], layout_model, layout_processor, line_predictions)
            
            # 4. Extract bounding boxes
            # Surya returns a list of results (one per image). We only passed one.
            page_layout = []
            if layout_predictions and len(layout_predictions) > 0:
                # `bboxes` contains objects with .label and .bbox attributes
                for box_obj in layout_predictions[0].bboxes:
                    # Convert [x1, y1, x2, y2] floats/ints to a clean string
                    bbox_coords = [int(coord) for coord in box_obj.bbox]
                    surya_label = getattr(box_obj, "label", "Text")
                    
                    mapped_type = LABEL_MAP.get(surya_label, "other")
                    
                    page_layout.append({
                        "block_type": mapped_type,
                        # We pass the coordinates as content. Qwen will use this as a map.
                        "content": f"Location: {bbox_coords}"
                    })

            # 5. Format to exactly match what content_extractor.py expects
            result_dict = {
                "input_image": str(img_path),
                "model": "surya-legacy-layout",
                "data": {
                    "page_layout": page_layout
                }
            }

            out_path.write_text(json.dumps(result_dict, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"  -> Saved {len(page_layout)} blocks to {out_path.name} ({time.time() - t0:.1f}s)")
            done += 1

        except Exception as e:
            print(f"  -> Error processing {img_path.name}: {e}")

    print(f"\nFinished: {done} processed, {skipped} skipped.")

if __name__ == "__main__":
    main()