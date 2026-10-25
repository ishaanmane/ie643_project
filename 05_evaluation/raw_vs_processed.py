"""Ablation: does preprocessing help? The trained clean adapter reads the RAW scans
(data/raw_scans/, only resized to the same pixel budget) instead of data/processed/.

    python3 05_evaluation/raw_vs_processed.py            # GPU; resumable
Writes preds/final_clean_raw_{val,test}/ and their scores, then compares with
preds/final_clean_{val,test} (same model, preprocessed input) using a paired bootstrap.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "06_interface"))
sys.path.insert(0, os.path.join(ROOT, "03_recognition"))


def main():
    from pipeline import CleanRecognizer
    import json
    model = CleanRecognizer(os.path.join(ROOT, "runs/final_clean/final_adapter"), max_new_tokens=1280)
    splits = json.load(open(os.path.join(ROOT, "data/splits.json")))["splits"]
    for split in ("val", "test"):
        out = os.path.join(ROOT, "preds", f"final_clean_raw_{split}")
        os.makedirs(out, exist_ok=True)
        for i, page in enumerate(splits[split], 1):
            target = os.path.join(out, page + ".md")
            if os.path.exists(target):
                continue
            text, _ = model.predict(os.path.join(ROOT, "data/raw_scans", page + ".jpg"))
            open(target, "w").write(text)
            print(f"[{split} {i}/{len(splits[split])}] {page}", flush=True)
        for args in (["--pred", out], ["--pred", out.replace("_raw", ""), "--compare", out]):
            r = subprocess.run([sys.executable, os.path.join(ROOT, "05_evaluation/evaluate.py"), *args,
                                "--split", os.path.join(ROOT, f"data/{split}.jsonl"), "--full"],
                               cwd=ROOT, capture_output=True, text=True)
            print(r.stdout or r.stderr, flush=True)
            if "--compare" not in args:
                open(out + "_score.txt", "w").write(r.stdout)


if __name__ == "__main__":
    main()
