"""Score predicted Markdown against the ground truth.

Usage (from the repo root):
    python 05_evaluation/evaluate.py --pred preds/base_val --split data/val.jsonl [--csv out.csv]
    python 05_evaluation/evaluate.py --pred preds/final_clean_test --split data/test.jsonl --full
    python 05_evaluation/evaluate.py --pred preds/A --compare preds/B --split data/test.jsonl
--full adds the metrics in metrics.py (corpus CER, NED, token P/R/F1, BLEU-4, normalised
equation P/R/F1 and edit score, diagram counts, headings, 95% bootstrap intervals);
--compare runs a paired bootstrap of NED, A vs B, on the same pages.

Metrics, per page and averaged by source (prefix of the page id):
  CER / WER   character and word error rate on the whole page (lower is better)
  text CER    same, after removing math and [Diagram: ...] lines, so equations
              do not dominate the number
  eq match    share of ground-truth $$...$$ equations that appear verbatim
              (whitespace-normalised) in the prediction (higher is better)
Per-page CER/WER is capped at 1.0 so one runaway page cannot dominate the mean, and
text CER is skipped when the reference has under 20 characters of plain text (the
ratio is meaningless there). Pages with no prediction file are counted as missing.
References are read from data/annotations/<id>.md (the current, possibly corrected
labels), not from the copy inside the JSONL; the split file only says which pages.
"""
import argparse
import csv
import json
import os
import re
import statistics as st
import sys

import jiwer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import metrics as M  # noqa: E402


def load_records(jsonl_path):
    """One dict per page of a split file: id, image_path, answer (JSONL copy of the label)."""
    recs = []
    with open(jsonl_path) as fh:
        for line in fh:
            user, assistant = json.loads(line)["messages"]
            image_path = next(c["image"] for c in user["content"] if c["type"] == "image")
            answer = assistant["content"]
            if not isinstance(answer, str):
                answer = "".join(c.get("text", "") for c in answer)
            recs.append({"id": os.path.splitext(os.path.basename(image_path))[0],
                         "image_path": image_path, "answer": answer})
    return recs


MATH = re.compile(r"\$\$(.+?)\$\$", re.S)


def norm(t):
    return re.sub(r"\s+", " ", t).strip()


def strip_math(t):
    t = MATH.sub(" ", t)
    t = re.sub(r"\$[^$\n]+\$", " ", t)
    t = re.sub(r"^\s*\[Diagram:.*$", " ", t, flags=re.M)
    return norm(t)


def equations(t):
    return [re.sub(r"\s+", "", m) for m in MATH.findall(t)]


def capped(x):
    return min(x, 1.0)


def score(ref, pred):
    row = {"cer": capped(jiwer.cer(norm(ref), norm(pred))),
           "wer": capped(jiwer.wer(norm(ref), norm(pred)))}
    rt, pt = strip_math(ref), strip_math(pred)
    row["text_cer"] = capped(jiwer.cer(rt, pt)) if len(rt) >= 20 else None
    eq = equations(ref)
    row["eq_match"] = (sum(e in set(equations(pred)) for e in eq) / len(eq)) if eq else None
    return row


def mean(vals):
    vals = [v for v in vals if v is not None]
    return f"{st.mean(vals):.3f}" if vals else "  -  "


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--pred", required=True)
    p.add_argument("--split", required=True)
    p.add_argument("--csv", default="")
    p.add_argument("--full", action="store_true", help="also the extended metrics")
    p.add_argument("--compare", default="", help="second prediction folder for a paired comparison")
    a = p.parse_args()

    rows, missing, refs = [], [], {}
    for r in load_records(a.split):
        path = os.path.join(a.pred, r["id"] + ".md")
        if not os.path.exists(path):
            missing.append(r["id"])
            continue
        if not norm(r["answer"]):
            continue  # nothing to compare against
        ref_path = os.path.join("data/annotations", r["id"] + ".md")
        ref = open(ref_path).read() if os.path.exists(ref_path) else r["answer"]
        if not norm(ref):
            continue
        pred = open(path).read()
        row = score(ref, pred)
        row.update(id=r["id"], source=r["id"].split("_")[0])
        if a.full or a.compare:
            row["full"] = M.page_metrics(ref, pred)
        refs[r["id"]] = ref
        rows.append(row)

    print(f"scored {len(rows)} pages, {len(missing)} missing predictions")
    print(f"{'source':8s} {'n':>3s} {'CER':>6s} {'WER':>6s} {'textCER':>8s} {'eqMatch':>8s}")
    for src in sorted({r["source"] for r in rows}) + ["ALL"]:
        sub = [r for r in rows if src == "ALL" or r["source"] == src]
        print(f"{src:8s} {len(sub):3d} {mean([r['cer'] for r in sub]):>6s} "
              f"{mean([r['wer'] for r in sub]):>6s} {mean([r['text_cer'] for r in sub]):>8s} "
              f"{mean([r['eq_match'] for r in sub]):>8s}")
    if a.full:
        full_report(rows)
    if a.compare:
        compare(rows, refs, a.compare)
    if a.csv:
        with open(a.csv, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["id", "source", "cer", "wer", "text_cer", "eq_match"])
            w.writeheader()
            w.writerows(rows)


def fmt(v):
    return "  -  " if v is None else f"{v:.3f}"


def full_report(rows):
    cols = [("corpCER", "corpus_cer"), ("NED", "ned"), ("tokP", "tok_p"), ("tokR", "tok_r"), ("tokF1", "tok_f1"),
            ("BLEU4", "bleu4"), ("len", "len_ratio"), ("eqP", "eq_p"), ("eqR", "eq_r"), ("eqF1", "eq_f1"),
            ("eqEdit", "eq_edit"), ("diagEx", "diag_exact"), ("diagP", "diag_p"), ("diagR", "diag_r"), ("headR", "heading_r")]
    print("\nextended metrics (higher is better except corpCER, NED; len = prediction/reference length)")
    print(f"{'source':8s} {'n':>3s} " + " ".join(f"{c:>7s}" for c, _ in cols))
    for src in sorted({r["source"] for r in rows}) + ["ALL"]:
        sub = [r["full"] for r in rows if src == "ALL" or r["source"] == src]
        s = M.summarise(sub)
        print(f"{src:8s} {len(sub):3d} " + " ".join(f"{fmt(s[k]):>7s}" for _, k in cols))
    for name, key in (("CER (capped, page mean)", None), ("NED", "ned"), ("token F1", "tok_f1"), ("eq edit score", "eq_edit")):
        vals = [r["cer"] for r in rows] if key is None else [r["full"][key] for r in rows]
        ci = M.bootstrap_ci(vals)
        if ci:
            print(f"95% CI {name}: {ci[0]:.3f} - {ci[1]:.3f}")


def compare(rows, refs, other_dir):
    a, b = [], []
    for r in rows:
        path = os.path.join(other_dir, r["id"] + ".md")
        if os.path.exists(path):
            a.append(r["full"]["ned"])
            b.append(M.page_metrics(refs[r["id"]], open(path).read())["ned"])
    diff, ci, p_better = M.paired_bootstrap(a, b)
    wins = sum(y < x for x, y in zip(a, b))
    print(f"\npaired comparison on {len(a)} pages, NED (lower is better): B - A = {diff:+.3f} "
          f"(95% CI {ci[0]:+.3f} to {ci[1]:+.3f}); B better on {wins} pages, worse on "
          f"{sum(y > x for x, y in zip(a, b))}; B better in {100 * p_better:.0f}% of resamples")


if __name__ == "__main__":
    main()
