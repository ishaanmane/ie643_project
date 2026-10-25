"""Hand-graded check of the figures in the reconstructed PDFs.

build: one self-contained HTML page with every figure the renderer placed (crop + the
       description used as its caption) and, beside it, the source page. You mark each one.
score: reads the JSON the page exports and reports the rates.

    python3 05_evaluation/crop_review.py build --docs out/reconstruction_test/outlined --out results/crop_review/test.html
    python3 05_evaluation/crop_review.py score results/crop_review/test_grades.json

Grades per figure: correct (right drawing, complete), partial (right drawing, cut off),
wrong (crop shows a different drawing than the caption), not_drawing (text or equation boxed).
"""
import argparse
import base64
import glob
import io
import json
import os
import re
from collections import Counter

from PIL import Image

FIG = re.compile(r"!\[(.*?)\]\((figures/[^)]+)\)", re.S)
PAGE_MARK = re.compile(r"<!-- page: (\S+) -->")


def thumb(path, size):
    with Image.open(path) as im:
        im = im.convert("RGB")
        im.thumbnail((size, size))
        buf = io.BytesIO(); im.save(buf, "JPEG", quality=75)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def build(docs, out):
    items = []
    for md in sorted(glob.glob(os.path.join(docs, "*", "*.md"))):
        unit_dir = os.path.dirname(md)
        page = None
        for line in open(md).read().splitlines():
            m = PAGE_MARK.search(line)
            if m:
                page = m.group(1)
            for cap, rel in FIG.findall(line):
                items.append({"id": f"{os.path.basename(unit_dir)}/{os.path.basename(rel)}", "page": page,
                              "caption": cap.replace("\\[", "[").replace("\\]", "]"),
                              "crop": thumb(os.path.join(unit_dir, rel), 520),
                              "source": thumb(os.path.join("data/processed", page + ".jpg"), 700) if page else ""})
    cards = "\n".join(f'''<section data-id="{i['id']}"><h2>{n}. {i['page']}</h2><div class="row">
<figure><img src="{i['crop']}"><figcaption>{i['caption']}</figcaption></figure>
<details><summary>source page</summary><img src="{i['source']}"></details></div>
<div class="grades">''' + "".join(f'<label><input type="radio" name="g{n}" value="{g}"> {t}</label>' for g, t in
        [("correct", "correct"), ("partial", "partial crop"), ("wrong", "wrong drawing"), ("not_drawing", "not a drawing")])
        + "</div></section>" for n, i in enumerate(items, 1))
    html = f'''<!doctype html><meta charset="utf-8"><title>Crop review</title>
<style>body{{font:14px system-ui;margin:24px auto;max-width:1100px;color:#1f2a26}}section{{border-top:1px solid #ddd;padding:14px 0}}
.row{{display:flex;gap:20px;align-items:flex-start}}figure{{margin:0;max-width:540px}}img{{max-width:100%;border:1px solid #eee}}
figcaption{{color:#556;margin-top:6px}}details{{flex:1}}.grades label{{margin-right:18px}}#bar{{position:sticky;top:0;background:#fff;padding:8px 0}}</style>
<div id="bar"><b>{len(items)} figures.</b> For each: is the crop the drawing the caption describes, and is it complete?
<button onclick="save()">Export grades</button> <span id="n"></span></div>
{cards}
<script>
function save(){{const g={{}};document.querySelectorAll('section').forEach((s,i)=>{{const c=s.querySelector('input:checked');if(c)g[s.dataset.id]=c.value;}});
const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify(g,null,1)],{{type:'application/json'}}));a.download='grades.json';a.click();}}
document.addEventListener('change',()=>{{document.getElementById('n').textContent=document.querySelectorAll('input:checked').length+' graded';}});
</script>'''
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    open(out, "w").write(html)
    print(f"{len(items)} figures -> {out}")


def score(path):
    g = Counter(json.load(open(path)).values())
    n = sum(g.values())
    for k in ("correct", "partial", "wrong", "not_drawing"):
        print(f"{k:12s} {g[k]:4d}  {g[k] / max(n, 1):.3f}")
    print(f"graded {n}; right drawing (correct + partial) {(g['correct'] + g['partial']) / max(n, 1):.3f}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("action", choices=["build", "score"])
    p.add_argument("path", nargs="?")
    p.add_argument("--docs")
    p.add_argument("--out")
    a = p.parse_args()
    build(a.docs, a.out) if a.action == "build" else score(a.path)
