# Upload demo: deployment, security and recovery

2026-10-25. This runbook supersedes the interface-launch/token instructions in the older operations log. Local browser inputs/downloads/restarts and the temporary HTTPS page/sign-in are tested on Mac. Public upload testing was declined by the browser permission gate; see the evidence report. A public GPU deployment remains pending the retrained adapter directory and GPU execution. Push remains subject to the user’s explicit “push”.

## Architecture

Browser → temporary Cloudflare HTTPS URL → outbound HTTP/2 tunnel → Waitress bound to `127.0.0.1:7860` → one job worker → tested isolated Surya → selected clean adapter worker → PDF renderer. Layout and recognition GPU allocations run sequentially. No same-Wi-Fi requirement and no inbound router port is opened. The UI and processing stay on the GPU machine; the tunnel provider transports uploads/results. Never claim that public traffic bypasses the provider.

`manage.py` supervises exactly the web/tunnel children it creates; it never kills training, other tmux sessions, or an occupied port. It runs detached from the terminal. Repeated starts are idempotent. It records status privately in `out/interface_service/`; no credential is written there. Its lifetime is the process/machine lifetime, not a reboot-installed service. After reboot, run start again. A restarted Quick Tunnel normally produces a new URL; the application key stays the same. This is temporary demo access, not a permanent hosted address.

## First GPU launch

Do this after training is idle. First inspect existing services, without killing them:

```bash
source /home/intralab/workspace/ie643_env.sh
# Work in the existing checkout used for the final rerun; do not switch branches.
tmux list-panes -a -F 'Session: #S | Command: #{pane_current_command} | PID: #{pane_pid}'
ss -ltnp '( sport = :7860 or sport = :8001 )'
nvidia-smi
```

**Expect:** identify any old UI on7860/manual Surya on8001. Leave training alone. Stop an old UI/tunnel only in its identified service pane and only after any active conversion finishes. No `tmux kill-server`, broad `pkill`, branch switching or killing unknown port owners. The new launcher refuses occupied ports.

After the user authorizes a push and the new code reaches origin:

```bash
git pull --rebase
bash 06_interface/setup_gpu.sh
```

**Expect:** pulls the existing branch’s configured upstream; the current branch stays unchanged; UI dependencies install in the activated environment. Flask3.1.3, Werkzeug3.1.9, Waitress3.0.2, pillow-heif1.8.1, Pillow13.0.0 were tested in the Mac UI layer. Do not replace the separate Surya/vLLM environments.

The corrected-data adapter path was not yet known at implementation time. Do not choose an older directory merely because it exists. Once the training run identifies its final adapter:

```bash
read -r -p 'Corrected-data final_adapter directory: ' FINAL_ADAPTER
python3 06_interface/manage.py doctor --adapter "$FINAL_ADAPTER"
python3 06_interface/manage.py start --adapter "$FINAL_ADAPTER"
```

**Expect:** CUDA, adapter config/weights, PDF tools and layout-environment paths checked; the private supervisor starts the tunnel and web server. Layout package versions are additionally enforced by the existing per-job layout runner. Doctor checks runtime availability, not output accuracy. The adapter config must specify Qwen/Qwen2.5-VL-7B-Instruct with nonempty safetensors weights.

```bash
python3 06_interface/manage.py status
python3 06_interface/manage.py token
```

**Expect:** state ready and current HTTPS URL. The second command prints the access key privately; enter it into the UI. Do not paste it into chat. Store/share it only with the intended evaluator. Download links have no token. The public HTML/assets are visible without authentication; jobs, GPU submissions and downloads require a session or separate private operator bearer credential.

## Final GPU acceptance test

1. Upload an actual iPhone HEIC plus a small PDF. Reorder them and submit once.
2. Verify layout then recognition then rendering; download/open the result, bundle and report.
3. Confirm the inference report names the new adapter, layout is Surya, page count/order is right and crops/source appendix exist. Inspect fidelity visually.
4. Refresh: the result should remain available. After an idle service restart, sign-in and completed downloads should still work at the current origin.
5. Inspect GPU memory after completion. It should return to the idle baseline; no managed vLLM or recognition worker should remain. Repeat one upload to check model reload/release.
6. Open a signed-out/private browser: it should show a login form and reject job/download URLs without a session. A different browser session using the same access key cannot enumerate the first browser’s jobs. A separate private operator credential, never shared in the browser login, can inspect all jobs intentionally.

This test needs the GPU; Mac preview tests do not replace it. Never run it alongside training on the same GPU.

## Status, stop and logs

```bash
python3 06_interface/manage.py status
python3 06_interface/manage.py stop
```

**Expect:** status includes mode/URL. Stop refuses while conversion is active, then stops only owned children. No extra tmux session is needed.

```bash
tail -60 out/interface_service/web.log
tail -60 out/interface_service/tunnel.log
tail -60 out/interface_service/supervisor.log
```

**Expect:** the actual failure. Detailed conversion errors stay in private logs and job directories; the browser gets a bounded error message. Do not post logs without checking for private document text. Job layout/recognition logs remain under `out/upload_jobs/<id>/output/`.

A stopped/failed tunnel can change URL on the next start. Reopen the newest URL and sign in. A healthy, already-running deployment is reused. The web server never defaults to all network interfaces; public access must go through the configured HTTPS origin.

## Retention, recovery and access

- The random access key is generated once in `out/upload_jobs/.access-token` with mode0600; the root directory is0700. Keep `out/` out of Git and publicly served directories.
- The shared demo login key cannot act as the operator credential or derive the independent cookie-signing secret. All three files are random and mode0600; the operator key is used locally by the launcher, never printed by `manage.py token`.
- Signed session cookies contain browser-owner/CSRF identifiers, not the access key. They are HttpOnly/SameSite=Strict; Secure is enabled for the HTTPS origin. Sessions expire after eight hours of inactivity. Restarted servers reuse the private signing secret kept independently in the private .session-secret file.
- Jobs persist to disk. Interrupted jobs become errors on restart and never silently resume or claim success. A completed job remains accessible to its original browser session. Signing out removes that browser’s access; the operator can still inspect local artifacts.
- Completed/error jobs are removed after24h (a minute-level sweep plus request checks). Active jobs are not pruned. At most50 retained jobs and a minimum1GiB free-space reserve prevent unbounded normal submissions; conversions are serialized. Inputs remain capped at25MiB,20 files,20 pages and40MP per image.
- Delete removes the job’s inputs, generated files and status from disk; it is permanent. Download what you need first. Backup copies already downloaded are not removed.
- HTML, JS and CSS contain no secrets or external script/font dependencies. Host/origin checks, CSRF, content security policy, bounded parser/server resources and session ownership are tested.
- Prediction TeX is restricted to reviewed math commands/environments; Markdown image/resource insertion is rejected, raw HTML/TeX input is disabled in upload Pandoc rendering, and shell escape is disabled. These are controls for a small authenticated demo, not a substitute for container/OS isolation if this becomes a hostile multiuser service. No automated audit claims it is impossible to compromise.

## Local test provenance

See [interface validation](../results/interface_validation/README.md): real encoded HEIC/HEIF + PDF browser upload, reorder, preprocessing, marked PDF download, byte/hash/page checks, session/job recovery, unauthenticated endpoint checks,25 CPU interface tests and13 renderer tests. Mac uses Python3.12.14 in ignored `out/interface-py312`; no changes were made to model weights or training data by this interface task.

The public file-upload permission was declined during the Mac test; no real notes were uploaded to Cloudflare by this test. Run that acceptance step yourself only with material you intend to send through the provider.

Primary references: [pillow-heif plugin](https://pillow-heif.readthedocs.io/en/stable/pillow-plugin.html), [Flask security](https://flask.palletsprojects.com/en/stable/web-security/), [Flask deployment with Waitress](https://flask.palletsprojects.com/en/stable/deploying/waitress/).
