"""Summarise a generation run: outlines (outline.py) + rendered documents (render_document.py).

Usage (from the repo root):
    python3 04_reconstruction/evaluate_generation.py --docs out/documents_all --outlines out/outlines_all [--md results/generation_eval.md]

Per unit and in total: blocks kept (must be 100%), sections, whether the LLM outline was used
or rejected, titles dropped and repeats merged, equations typeset/failed, figures matched,
and whether a PDF was produced.
"""
import argparse
import glob
import json
import os


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--docs", required=True, help="output folder of render_document.py")
    p.add_argument("--outlines", default=None, help="output folder of outline.py")
    p.add_argument("--md", default=None, help="also write the table as Markdown")
    a = p.parse_args()

    rows = []
    for rp in sorted(glob.glob(os.path.join(a.docs, "*", "report.json"))):
        r = json.load(open(rp))
        unit = r["unit"]
        o = {}
        if a.outlines and os.path.exists(os.path.join(a.outlines, unit + ".json")):
            o = json.load(open(os.path.join(a.outlines, unit + ".json")))
        orep = o.get("report", {})
        pages = r["pages"]
        rows.append({
            "unit": unit, "pages": len(pages),
            "blocks": r["preservation"]["blocks"], "kept": r["preservation"]["blocks"] - r["preservation"]["missing"],
            "outline": "none" if not o else ("used" if o.get("outline") else "rejected"),
            "sections": len((o.get("outline") or {}).get("sections", [])),
            "titles_dropped": len(orep.get("titles_replaced", [])),
            "repeats_merged": len(orep.get("merged_repeats", [])),
            "problems": len(orep.get("problems", [])),
            "equations": r["math"]["equations"], "eq_failed": r["math"]["failed"],
            "diagrams": sum(x["descriptions"] for x in pages), "matched": sum(x["matched"] for x in pages),
            "pdf": bool(r.get("output") and r["output"].lower().endswith(".pdf")),
            "math_check": r["math"].get("checked_with", "unknown"),
        })
    if not rows:
        raise SystemExit("no report.json files under " + a.docs)

    cols = ["unit", "pages", "kept", "blocks", "outline", "sections", "titles_dropped", "repeats_merged",
            "problems", "equations", "eq_failed", "math_check", "matched", "diagrams", "pdf"]
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for x in rows:
        lines.append("| " + " | ".join(str(x[c]) for c in cols) + " |")
    T = {k: sum(x[k] for x in rows) for k in ("pages", "blocks", "kept", "sections", "titles_dropped",
                                              "repeats_merged", "problems", "equations", "eq_failed",
                                              "diagrams", "matched")}
    used = sum(x["outline"] == "used" for x in rows)
    rejected = sum(x["outline"] == "rejected" for x in rows)
    summary = [
        f"units {len(rows)}, pages {T['pages']}",
        f"blocks kept {T['kept']}/{T['blocks']} ({100 * T['kept'] / max(T['blocks'], 1):.1f}%)",
        f"outlines used {used}, rejected {rejected}, none {len(rows) - used - rejected}; "
        f"sections {T['sections']} (mean {T['sections'] / max(used, 1):.1f} per used outline)",
        f"titles dropped {T['titles_dropped']}, repeats merged {T['repeats_merged']}, outline problems {T['problems']}",
        f"equations {T['equations']}, failed to typeset {T['eq_failed']} ({100 * T['eq_failed'] / max(T['equations'], 1):.2f}%)",
        "equation checks: " + ", ".join(sorted({x["math_check"] for x in rows})),
        f"diagrams matched to a crop {T['matched']}/{T['diagrams']}",
        f"PDFs built {sum(x['pdf'] for x in rows)}/{len(rows)}",
    ]
    print("\n".join(lines))
    print("\n" + "\n".join(summary))
    if a.md:
        os.makedirs(os.path.dirname(os.path.abspath(a.md)), exist_ok=True)
        open(a.md, "w").write("# Generation evaluation\n\n" + "\n".join(f"- {s}" for s in summary)
                              + "\n\n" + "\n".join(lines) + "\n")
        print("\nwritten", a.md)


if __name__ == "__main__":
    main()
