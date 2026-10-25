#!/usr/bin/env bash
# Run from the GPU repo after pulling the tested changes. No model loading/training.
set -euo pipefail
cd "$(dirname "$0")/.."
case "${1:-}" in
  ""|--notebook) ;;
  *) echo 'Usage: bash 04_reconstruction/run_render_fixes.sh [--notebook]' >&2; exit 2 ;;
esac
mkdir -p out
python3 -W ignore::ResourceWarning -m unittest discover -s 04_reconstruction/tests -q
python3 04_reconstruction/render_document.py \
  --unit ie643_lec07 --unit mlt_week06 \
  --pages-md preds/lora_clean_val --format pdf \
  --reviewed-fixes 04_reconstruction/reviewed_render_fixes.json \
  --out out/reconstruction_grounded_val \
  > out/render_grounded_val.log 2>&1 || { tail -40 out/render_grounded_val.log; exit 1; }
tail -2 out/render_grounded_val.log
python3 04_reconstruction/evaluate_generation.py \
  --docs out/reconstruction_grounded_val \
  --md results/generation_eval_grounded_val.md > out/generation_grounded_val.log
if [ "${1:-}" = --notebook ]; then
  python3 04_reconstruction/render_document.py \
    --unit ie802_notes --format pdf --out out/reconstruction_fitted_notebook \
    > out/render_fitted_notebook.log 2>&1 || { tail -40 out/render_fitted_notebook.log; exit 1; }
  tail -1 out/render_fitted_notebook.log
fi
python3 - "${1:-}" <<'PY'
import json
from pathlib import Path
import sys
roots = [Path('out/reconstruction_grounded_val')]
if sys.argv[1] == '--notebook':
    roots.append(Path('out/reconstruction_fitted_notebook'))
for root in roots:
    for p in sorted(root.glob('*/report.json')):
        r = json.loads(p.read_text())
        if not r.get('output') or not Path(r['output']).is_file():
            raise SystemExit(f"PDF missing: {p}; inspect pandoc_errors in that report")
        audit = r.get('pdf_audit', {})
        print(f"{r['unit']}: PDF bounds {audit.get('status', 'unknown')}; outside words {audit.get('outside_words', 'not checked')}")
        if audit.get('status') == 'error' or audit.get('outside_words', 0):
            raise SystemExit(f"PDF audit needs review: {p}")
print('Summary saved: results/generation_eval_grounded_val.md')
PY
