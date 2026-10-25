# Step 6 - Notes2PDF interface

Web page to upload handwritten notes (PDF, HEIC/HEIF, JPG, PNG, WebP, BMP, TIFF; up to 20 pages,
25 MiB) and download a searchable PDF, the Markdown, an editable bundle and a conversion report.
Each upload runs the full pipeline: preprocessing -> Surya diagram crops + Qwen2.5-VL (trained
adapter) -> LaTeX/PDF. Access is by a private key; files are deleted after 24 hours.

## Speed: models stay warm

The first upload loads both models (about a minute). They stay on the GPU while uploads keep
coming and are unloaded after **15 idle minutes** (`--idle-minutes`), which frees the GPU again.
Surya runs with a reduced GPU share so both fit together, and diagram detection runs at the same
time as text recognition. Code: `engine.py` (warm models), `recognition_worker.py` (persistent Qwen
process), `layout.py` (Surya server). **Stop the interface before any training run.**

## Public link: Tailscale Funnel (one-time setup on the GPU machine)

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up --hostname notes2pdf          # opens a login link: sign in with your account
sudo tailscale set --operator=$USER             # lets manage.py switch Funnel on/off without sudo
```
The first `manage.py start` may print a link to enable Funnel for your tailnet; open it once.
The address is then always `https://notes2pdf.<your-tailnet>.ts.net` (tailnet name can be changed
in the Tailscale admin console, DNS page).

## Run

```bash
bash 06_interface/setup_gpu.sh                   # once: web + HEIC packages
python3 06_interface/manage.py start             # uses runs/final_clean/final_adapter
python3 06_interface/manage.py status            # URL and state
python3 06_interface/manage.py token             # access key to give to users
python3 06_interface/manage.py stop
```
Options: `--tunnel cloudflare` (random trycloudflare.com link) or `--tunnel none` (localhost only),
`--adapter <dir>`, `--idle-minutes N`, `--demo` (Mac UI test: no models, source previews only).

| File | Purpose |
|---|---|
| `manage.py` | Start/stop the server and the public link in the background |
| `server.py` | Web server (Flask + Waitress): sign-in, uploads, job status, downloads, 24 h cleanup |
| `pipeline.py` | One upload: decode pages, preprocess, layout + recognition, render PDF, bundle |
| `engine.py`, `recognition_worker.py`, `layout.py` | Warm models (see above) |
| `index.html`, `app.js`, `style.css` | The page |
| `demo.py` | Test mode without models |
| `tests/` | `python3 -m unittest discover -s 06_interface/tests` |

Limits and extreme cases (more than 20 pages, size, formats, timeouts): [../docs/REPORT_NOTES.md](../docs/REPORT_NOTES.md).
