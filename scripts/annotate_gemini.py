"""Bootstrap ground-truth annotations for processed pages using Gemini 2.0 Flash.

This is the AI-bootstrap half of the annotation strategy from
FINAL_IMPLEMENTATION_PLAN.md section 5.2: auto-transcribe every page, then a
human manually verifies/corrects (required for the full test set, spot-check
for train). This script only does the auto-transcribe half.

Requires a free API key from https://aistudio.google.com/apikey, passed via
the GEMINI_API_KEY environment variable (never hardcode it into this file).

Usage:
    export GEMINI_API_KEY="your-key-here"
    python3 scripts/annotate_gemini.py [--limit N]

Resumable: skips any page that already has a .md file in data/annotations/.
"""
import argparse
import os
import sys
import time

from google import genai
from google.genai import types

PROCESSED_DIR = "data/processed"
ANNOTATIONS_DIR = "data/annotations"
MODEL = "gemini-3.6-flash"

PROMPT = (
    "Convert this handwritten lecture note page into clean, structured Markdown.\n"
    "Rules:\n"
    "- Use # for main headings, ## for subheadings, ### for sub-subheadings\n"
    "- Use LaTeX wrapped in $$ for display equations, $ for inline math\n"
    "- Use - for bullet points, 1. 2. 3. for numbered lists\n"
    "- Use Markdown tables for any tabular content\n"
    "- Use > for important notes or definitions\n"
    "- Describe any diagrams in [Diagram: description] format\n"
    "- Preserve ALL content faithfully — do not summarize or skip anything\n"
)


def annotate_all(limit=None, sleep_s=4.5):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: set GEMINI_API_KEY environment variable first.", file=sys.stderr)
        print("Get a free key at https://aistudio.google.com/apikey", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    os.makedirs(ANNOTATIONS_DIR, exist_ok=True)

    files = sorted(
        f for f in os.listdir(PROCESSED_DIR)
        if f.lower().endswith((".jpg", ".jpeg", ".png")) and "_debug" not in f
    )
    todo = []
    for f in files:
        stem = os.path.splitext(f)[0]
        if not os.path.exists(os.path.join(ANNOTATIONS_DIR, stem + ".md")):
            todo.append(f)

    if limit:
        todo = todo[:limit]

    print(f"{len(files)} processed pages total, {len(todo)} need annotation this run.")

    ok, failed = 0, []
    for i, fname in enumerate(todo, 1):
        stem = os.path.splitext(fname)[0]
        img_path = os.path.join(PROCESSED_DIR, fname)
        try:
            with open(img_path, "rb") as f:
                img_bytes = f.read()
            response = client.models.generate_content(
                model=MODEL,
                contents=[
                    types.Part.from_bytes(data=img_bytes, mime_type="image/jpeg"),
                    PROMPT,
                ],
            )
            text = response.text.strip()
            with open(os.path.join(ANNOTATIONS_DIR, stem + ".md"), "w") as f:
                f.write(text)
            ok += 1
            print(f"[{i}/{len(todo)}] {fname} -> {len(text)} chars")
        except Exception as e:
            failed.append((fname, str(e)))
            print(f"[{i}/{len(todo)}] {fname} FAILED: {e}")
        time.sleep(sleep_s)  # free-tier rate limit headroom

    print(f"\nDone. {ok} succeeded, {len(failed)} failed.")
    if failed:
        print("Failed files (re-run the script to retry — it's resumable):")
        for fname, err in failed:
            print(f"  {fname}: {err}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None, help="only annotate the first N pending pages")
    args = parser.parse_args()
    annotate_all(limit=args.limit)
