# InTra upload interface

Updated 2026-10-25. This replaces the earlier stdlib HTTP UI and token-in-download links. See [deployment and security runbook](../docs/INTERFACE_DEPLOYMENT.md) and [Mac validation evidence](../results/interface_validation/README.md).

## What the user does

1. Open the temporary HTTPS URL and enter the operator’s access key.
2. Name the document; select or drop PDF, **HEIC/HEIF/HIF**, JPEG, PNG, WebP, BMP or TIFF files.
3. Move/remove files to set reading order. PDF/TIFF/HEIF frames stay in their native order within each file. Maximum 20 files, 20 decoded pages and 25 MiB total.
4. Create the document and follow stage progress. Refreshing or a server restart preserves completed-job access in the same signed-in browser session.
5. Download the PDF, editable bundle, Markdown or report. Review formulas/crops against the appended sources. Delete a completed job when finished, or let it expire after 24 hours.

The browser sends binary multipart uploads, so HEIC never needs a browser decoder or an external conversion service. Pillow/libheif decode it on the processing machine. Container orientation and EXIF are handled before JPEG normalization; alpha becomes white. Image content must match its extension. Images over 40 megapixels and documents over 20 pages are rejected before model inference.

## Model selection and GPU lifecycle

GPU mode requires an **explicit `--adapter` path**. It must identify the model retrained on the corrected dataset; the launcher must not silently reuse historical weights. The user will confirm that directory when training completes.

Fresh uploads never consult reference annotations, dataset splits or cached predictions. The selected trained clean adapter and original recognition pipeline are reused. Tested Surya **0.22.1** and vLLM **0.32.0** remain separate environments; old Surya 0.7.0 is not used. Surya runs first and exits, then isolated Qwen recognition runs and exits, followed by rendering. The GPU must be idle before a conversion; do not interrupt training to test the UI.

## Start once, without more tmux sessions

After code is transferred to the GPU and the existing Qwen environment is activated:

```bash
bash 06_interface/setup_gpu.sh
```

**Expect:** pinned UI/HEIC dependencies installed in that environment; no branch switch or model download/training.

```bash
read -r -p 'Corrected-data final_adapter directory: ' FINAL_ADAPTER
python3 06_interface/manage.py start --adapter "$FINAL_ADAPTER"
```

**Expect:** one owned supervisor starts Waitress on localhost:7860 and an HTTP/2 Cloudflare Quick Tunnel. A temporary HTTPS URL appears, or startup continues in the background. Repeating start reuses the running service. The key is not printed in public logs.

```bash
python3 06_interface/manage.py status
python3 06_interface/manage.py token
```

**Expect:** current URL/status, then the private access key. Paste the key only into the interface. Do not put it in Git, screenshots or chat. See the runbook for stopping/migration from old tmux processes.

## Mac test mode

```bash
out/interface-py312/bin/python 06_interface/manage.py start --local --demo --port 7861
```

**Expect:** localhost:7861, persistent private key and a conspicuous interface-test banner. This mode runs actual input decoding and the existing preprocessing code, but **no OCR/layout model**. Its source-preview PDF is stamped on every page. It is not reconstruction or accuracy evidence. The Mac environment is local/ignored; for another Mac, install the UI requirements, NumPy, OpenCV and PyMuPDF in a supported Python environment first.

## Security and tests

Flask + Waitress, loopback binding, exact trusted hosts/origin, CSRF checks, signed HttpOnly/SameSite cookies (Secure for the HTTPS deployment), rate-limited login, one GPU job, bounded uploads/connections, explicit download paths, browser-session job ownership, persistent job state, expiry/deletion and private credentials. Keys are never stored in browser storage or download query strings. A content security policy blocks remote scripts and embedding.

Uploaded predictions cannot introduce arbitrary TeX commands/environments or Markdown images/resources. Upload rendering disables raw HTML/TeX; XeLaTeX shell escape is disabled, including syntax checks. Ordinary math remains supported; unknown commands fail closed and preserve raw output for operator review. All 100 previously saved prediction pages passed the tightened validator after adding the harmless arrow commands they use. The service is intended for an authenticated, single-GPU classroom demo, not hostile public multitenant hosting.

```bash
python3 -m unittest discover -s 06_interface/tests -v
python3 -m unittest discover -s 04_reconstruction/tests -v
```

**Expect:** 25 interface tests and 13 renderer tests. See the saved validation report for exactly what ran on Mac and what still needs the GPU. No public GPU deployment or new model inference is claimed by the Mac tests.
