"""Layout check without hand boxes: Surya figure/table boxes vs the label's [Diagram: ...] count.

For every page the label says how many drawings there are; Surya's tags (data/tags/) say how
many figure/table regions it found. Per split and source: exact-count accuracy, and count-level
precision / recall (matched = min of the two counts per page). Before the renderer's merging of
over-split boxes, so this measures Surya itself.

    python3 05_evaluation/layout_counts.py [--md results/layout/count_metrics.md]
"""
import argparse
import json
import os
import re
from collections import defaultdict

FIG = {"figure", "table"}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--md", default="")
    a = p.parse_args()
    splits = json.load(open("data/splits.json"))["splits"]
    rows = []
    for split, pages in splits.items():
        for page in pages:
            label = open(f"data/annotations/{page}.md").read()
            ref = len(re.findall(r"\[Diagram:", label, re.I))
            tags = json.load(open(f"data/tags/{page}.json"))
            found = sum(b["type"] in FIG for b in tags["blocks"])
            rows.append((split, page.split("_")[0], ref, found))
    out = ["| split | source | pages | label drawings | Surya regions | exact count | precision | recall |",
           "|---|---|---|---|---|---|---|---|"]
    groups = defaultdict(list)
    for r in rows:
        groups[(r[0], r[1])].append(r); groups[(r[0], "ALL")].append(r); groups[("all", "ALL")].append(r)
    order = sorted(groups, key=lambda k: (["train", "val", "test", "all"].index(k[0]), k[1] == "ALL", k[1]))
    for key in order:
        g = groups[key]
        ref, found = sum(r[2] for r in g), sum(r[3] for r in g)
        hit = sum(min(r[2], r[3]) for r in g)
        exact = sum(r[2] == r[3] for r in g) / len(g)
        prec = f"{hit / found:.3f}" if found else "-"
        rec = f"{hit / ref:.3f}" if ref else "-"
        out.append(f"| {key[0]} | {key[1]} | {len(g)} | {ref} | {found} | {exact:.3f} | {prec} | {rec} |")
    text = "\n".join(out)
    print(text)
    if a.md:
        open(a.md, "w").write("# Surya figure count vs label drawings\n\n" + __doc__.split("\n\n")[1] + "\n\n" + text + "\n")


if __name__ == "__main__":
    main()
