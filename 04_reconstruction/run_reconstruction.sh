#!/usr/bin/env bash
# Stage 4 on the final predictions (GPU machine, from the repo root):
#   for val and test: LLM outline -> PDFs without and with the outline -> generation reports.
# The outline step loads Qwen2.5-VL (about 6 GB): stop the interface first (manage.py stop).
# Predictions are the fine-tuned clean model's (preds/final_clean_<split>); no hand fixes applied.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -W ignore::ResourceWarning -m unittest discover -s 04_reconstruction/tests -q
mkdir -p results/reconstruction out
for split in val test; do
  pred=preds/final_clean_$split
  out=out/reconstruction_$split
  python3 04_reconstruction/outline.py --all --split $split --pages-md $pred --max-new-tokens 4096 \
    --out $out/outlines 2>&1 | tee $out.outline.log | grep -E "OK|REJECTED|skipped" || true
  python3 04_reconstruction/render_document.py --all --split $split --pages-md $pred \
    --out $out/plain --format pdf | tee $out.plain.log
  python3 04_reconstruction/render_document.py --all --split $split --pages-md $pred \
    --outlines $out/outlines --out $out/outlined --format pdf | tee $out.outlined.log
  python3 04_reconstruction/evaluate_generation.py --docs $out/plain \
    --md results/reconstruction/${split}_plain.md | tail -12
  python3 04_reconstruction/evaluate_generation.py --docs $out/outlined --outlines $out/outlines \
    --md results/reconstruction/${split}_outlined.md | tail -12
  mkdir -p results/reconstruction/pdfs_$split
  for d in $out/outlined/*/; do
    u=$(basename "$d"); [ -f "$d/$u.pdf" ] && cp "$d/$u.pdf" results/reconstruction/pdfs_$split/
  done
  cp -r $out/outlines results/reconstruction/outlines_$split
done
echo "Saved: results/reconstruction/ (reports, outlines, outlined PDFs for val and test)"
