"""Consistency checks for the dataset, from raw scans to the training files.

Usage (from the repo root): python3 00_dataset/check_dataset.py
Read-only. Prints PASS / WARN / FAIL per check.

Checks:
  1. every raw scan has an annotation (and vice versa); processed images present
  2. splits: every page in exactly one split, no unit split across splits
  3. the JSONL files match splits.json, the current annotations and the prompt
  4. near-duplicate leakage: val/test pages whose text is very similar to a train page
  5. label format: uncertain readings (??), math delimiters, length
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_dataset import HELD_OUT, split_of  # noqa: E402
from prompts import PAGE_PROMPT  # noqa: E402

RAW, ANN, PROC = "data/raw_scans", "data/annotations", "data/processed"
results = []


def report(status, name, detail=""):
    results.append(status)
    print(f"[{status}] {name}" + (f": {detail}" if detail else ""))


def stems(folder, ext):
    if not os.path.isdir(folder):
        return set()
    return {os.path.splitext(f)[0] for f in os.listdir(folder) if f.endswith(ext) and "_debug" not in f}


def unit_of(stem):
    return re.match(r"[a-z0-9]+_([a-z0-9]+)_page\d+$", stem).group(1)


def shingles(text, k=5):
    t = re.sub(r"\s+", " ", text.lower())
    return {t[i:i + k] for i in range(max(0, len(t) - k + 1))}


def main():
    raw, ann, proc = stems(RAW, ".jpg"), stems(ANN, ".md"), stems(PROC, ".jpg")
    text = {s: open(os.path.join(ANN, s + ".md")).read().strip() for s in ann}

    # 1. pairing
    if raw == ann:
        report("PASS", "raw scans and annotations pair up", f"{len(raw)} pages")
    else:
        report("FAIL", "raw/annotation mismatch",
               f"no annotation: {sorted(raw - ann)[:5]}, no image: {sorted(ann - raw)[:5]}")
    if not proc:
        report("WARN", "data/processed/ is missing", "run 01_preprocessing/batch_preprocess.py")
    elif proc != raw:
        report("FAIL", "processed images do not match raw scans", f"missing {sorted(raw - proc)[:5]}")
    else:
        report("PASS", "processed images present", f"{len(proc)}")

    # 2. splits
    sp = json.load(open("data/splits.json"))["splits"]
    seen = Counter(s for v in sp.values() for s in v)
    dup = [s for s, c in seen.items() if c > 1]
    report("FAIL" if dup else "PASS", "each page in at most one split", f"duplicates: {dup[:5]}" if dup else "")
    wrong = [(s, k) for k, v in sp.items() for s in v if split_of(s) != k]
    report("FAIL" if wrong else "PASS", "splits.json agrees with HELD_OUT", str(wrong[:5]) if wrong else "")
    unit_splits = defaultdict(set)
    for k, v in sp.items():
        for s in v:
            unit_splits[unit_of(s)].add(k)
    leak = {u: ks for u, ks in unit_splits.items() if len(ks) > 1}
    report("FAIL" if leak else "PASS", "no unit (lecture/week) spread over two splits", str(leak) if leak else "")
    missing = sorted(raw - set(seen))
    report("WARN" if missing else "PASS", "every page is in a split",
           f"{len(missing)} not in any split (e.g. excluded as flagged): {missing[:6]}" if missing else "")
    comp = {k: dict(Counter(s.split("_")[0] for s in v)) for k, v in sp.items()}
    report("INFO", "split sizes by source", json.dumps(comp))
    for k in ("val", "test"):
        if not any(s.startswith(("ie802", "hlcs")) for s in sp[k]):
            report("WARN", f"{k} has no notebook-photo pages (ie802/hlcs)", "that medium is never measured")

    # 3. JSONL vs splits / annotations / prompt
    for k in ("train", "val", "test"):
        lines = [json.loads(l) for l in open(f"data/{k}.jsonl")]
        ids, stale, bad_prompt, bad_path = [], [], 0, 0
        for d in lines:
            user, asst = d["messages"]
            img = next(c["image"] for c in user["content"] if c["type"] == "image")
            prm = next(c["text"] for c in user["content"] if c["type"] == "text")
            sid = os.path.splitext(os.path.basename(img))[0]
            ids.append(sid)
            bad_prompt += prm != PAGE_PROMPT
            bad_path += img != f"{PROC}/{sid}.jpg"
            if text.get(sid) != asst["content"]:
                stale.append(sid)
        same = sorted(ids) == sorted(sp[k])
        report("PASS" if same else "FAIL", f"{k}.jsonl matches splits.json", f"{len(ids)} records")
        report("FAIL" if stale else "PASS", f"{k}.jsonl answers match current annotations",
               f"{len(stale)} stale, rebuild with 00_dataset/build_dataset.py: {stale[:4]}" if stale else "")
        if bad_prompt or bad_path:
            report("FAIL", f"{k}.jsonl prompt/path", f"{bad_prompt} wrong prompts, {bad_path} wrong paths")

    # 3b. boxed variant, if built: same pages per split, images present, boxes present
    if os.path.isdir("data/boxed"):
        no_tags = 0
        for k in ("train", "val", "test"):
            lines = [json.loads(l) for l in open(f"data/boxed/{k}.jsonl")]
            imgs = [next(c["image"] for c in d["messages"][0]["content"] if c["type"] == "image") for d in lines]
            ids = sorted(os.path.splitext(os.path.basename(i))[0] for i in imgs)
            if not os.path.isdir("data/processed_boxed"):
                report("PASS" if ids == sorted(sp[k]) else "FAIL", f"boxed/{k}.jsonl: same pages as {k}")
                report("WARN", f"boxed/{k}.jsonl: images not generated yet", "run 02_layout/draw_boxes.py")
                continue
            absent = [i for i in imgs if not os.path.exists(i)]
            ok = ids == sorted(sp[k]) and not absent
            report("PASS" if ok else "FAIL", f"boxed/{k}.jsonl: same pages as {k}, images exist",
                   "" if ok else f"{len(absent)} images missing; ids match: {ids == sorted(sp[k])}")
            no_tags += sum(not os.path.exists(f"data/tags_draft/{i}.json") for i in ids)
        report("WARN" if no_tags else "PASS", "boxed variant: every page has Surya boxes",
               f"{no_tags} pages without boxes (Surya not run on them)" if no_tags else "")

    # 4. near-duplicate leakage
    train_sh = {s: shingles(text[s]) for s in sp["train"]}
    for k in ("val", "test"):
        hits, top = [], (0.0, "")
        for s in sp[k]:
            sh = shingles(text[s])
            if len(sh) < 50:
                continue  # blank or tiny pages say nothing
            best, bt = 0.0, None
            for t, tsh in train_sh.items():
                j = len(sh & tsh) / len(sh | tsh)
                if j > best:
                    best, bt = j, t
            if best > top[0]:
                top = (best, f"{s}~{bt}")
            if best >= 0.5:
                hits.append(f"{s}~{bt} ({best:.2f})")
        report("WARN" if hits else "PASS", f"{k}: no near-duplicate of a train page (5-gram Jaccard >= 0.5)",
               "; ".join(hits[:6]) + (f" (+{len(hits) - 6} more)" if len(hits) > 6 else "") if hits
               else f"highest {top[0]:.2f} ({top[1]})")

    # 5. label format
    flagged = sorted(s for s in text if "??" in text[s])
    by_split = Counter(split_of(s) for s in flagged)
    report("WARN" if flagged else "PASS", "annotations with uncertain readings (??)",
           f"{len(flagged)} pages, by split {dict(by_split)}")
    styles = Counter()
    for s, t in text.items():
        if "$$" in t: styles["$$...$$"] += 1
        if re.search(r"(?<!\$)\$[^$\n]+\$(?!\$)", t): styles["inline $...$"] += 1
        if "\\(" in t or "\\[" in t: styles["\\( \\) or \\[ \\]"] += 1
        if "\\begin{align" in t: styles["align env"] += 1
    report("INFO", "math styles (pages using each)", dict(styles).__repr__())
    lens = sorted((len(t), s) for s, t in text.items())
    report("INFO", "answer length in characters", f"median {lens[len(lens) // 2][0]}, max {lens[-1][0]} ({lens[-1][1]}), "
           f"about {lens[-1][0] // 3} tokens at most")

    n_fail = results.count("FAIL")
    print(f"\n{n_fail} FAIL, {results.count('WARN')} WARN")
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
