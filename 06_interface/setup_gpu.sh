#!/usr/bin/env bash
# Run once after sourcing the existing Qwen environment. Does not install/switch models or branches.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 - <<'PY'
import sys
if sys.version_info < (3, 11):
    raise SystemExit('Use the existing GPU Python 3.11 environment first.')
if sys.prefix == sys.base_prefix:
    raise SystemExit('Activate the existing Qwen environment first; do not install into system Python.')
PY
if command -v uv >/dev/null 2>&1; then
  uv pip install --python "$(command -v python3)" -r 06_interface/requirements.txt
else
  python3 -m pip install -r 06_interface/requirements.txt
fi
python3 - <<'PY'
from importlib.metadata import version
from pillow_heif import register_heif_opener
register_heif_opener(thumbnails=False)
for package in ('Flask', 'Werkzeug', 'waitress', 'pillow-heif', 'Pillow'):
    print(f'{package}: {version(package)}')
PY
if ! command -v tailscale >/dev/null 2>&1; then
  echo 'Tailscale is not installed (needed for the https://notes2pdf.<tailnet>.ts.net link). See 06_interface/README.md.'
fi
echo 'UI setup complete. Start only after training is idle, with an explicit corrected-data adapter path.'
