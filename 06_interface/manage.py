"""One private demo deployment: start/status/token/stop. No branch changes or broad kills."""
import argparse
import importlib.metadata
import json
import os
from pathlib import Path
import re
import secrets
import signal
import socket
import subprocess
import sys
import time
from urllib.request import urlopen

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
STATE = ROOT / 'out/interface_service'
JOB_ROOT = ROOT / 'out/upload_jobs'


def read_state():
    try:
        return json.loads((STATE / 'service.json').read_text())
    except (OSError, ValueError):
        return {}


def alive(pid):
    try:
        os.kill(pid, 0)
        return True
    except (ProcessLookupError, PermissionError, TypeError):
        return False


def owned(state):
    pid = state.get('pid')
    if not pid or not alive(pid):
        return False
    # Prevent signalling an unrelated process after a PID is reused.
    result = subprocess.run(['ps', '-p', str(pid), '-o', 'args='], capture_output=True, text=True)
    return str(HERE / 'manage.py') in result.stdout and state.get('nonce', '!missing!') in result.stdout


def doctor(demo=False, adapter=None):
    for package in ('Flask', 'waitress', 'pillow-heif', 'Pillow', 'PyMuPDF'):
        print(f'{package}: {importlib.metadata.version(package)}')
    if not demo:
        import shutil
        from pipeline import adapter_config, DEFAULT_ADAPTER
        if adapter is None:
            raise RuntimeError("Pass --adapter with the model retrained on the corrected dataset.")
        adapter_config(adapter)
        import torch
        if not torch.cuda.is_available():
            raise RuntimeError("CUDA is unavailable in this Python environment.")
        for command in ('pandoc', 'xelatex'):
            if not shutil.which(command):
                raise RuntimeError(f'Missing {command}. Source the existing GPU environment first.')
        from layout import ENV_ROOT
        for folder in ('surya0221', 'vllm0320'):
            if not (Path(os.environ.get('IE643_LAYOUT_ENVS', ENV_ROOT)) / folder / 'bin/python').is_file():
                raise RuntimeError('The tested layout environments are unavailable.')
        print('Clean adapter and tested layout environment paths: present')
    else:
        print('INTERFACE TEST ONLY: no GPU model validation.')


def supervise(args):
    os.umask(0o077)
    import fcntl
    service_lock = (STATE / 'service.lock').open('a')
    try:
        fcntl.flock(service_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        return
    children = []
    funnel_on = False
    stop = False
    def signal_stop(*_):
        nonlocal stop
        stop = True
    signal.signal(signal.SIGTERM, signal_stop)
    signal.signal(signal.SIGINT, signal_stop)
    state = dict(pid=os.getpid(), nonce=args.nonce, mode='interface_test' if args.demo else 'gpu',
                 state='starting', started=time.time(), url=None, port=args.port)
    def save():
        temp = STATE / 'service.tmp'
        temp.write_text(json.dumps(state, indent=2))
        os.replace(temp, STATE / 'service.json')
    save()
    try:
        with socket.socket() as probe:
            probe.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            probe.bind(('127.0.0.1', args.port))
        origin = None
        if args.tunnel == 'tailscale':
            # Stable HTTPS name https://<machine>.<tailnet>.ts.net, served by tailscaled itself.
            status = json.loads(subprocess.check_output(['tailscale', 'status', '--json'], text=True))
            if status.get('BackendState') != 'Running':
                raise RuntimeError('Tailscale is not logged in; run: sudo tailscale up --hostname notes2pdf')
            origin = 'https://' + status['Self']['DNSName'].rstrip('.')
            try:
                subprocess.run(['tailscale', 'funnel', '--bg', str(args.port)], check=True,
                               capture_output=True, text=True, timeout=60)
            except subprocess.TimeoutExpired as error:
                # First use on a tailnet: Tailscale waits until Funnel is approved in the browser.
                said = (error.stdout or '') + (error.stderr or '') if isinstance(error.stdout, str) else ''
                link = re.search(r'https://login\.tailscale\.com/\S+', said)
                raise RuntimeError('Tailscale Funnel needs one-time approval: open '
                                   + (link.group(0) if link else 'the link printed by `tailscale funnel --bg 7860`')
                                   + ' and approve, then run start again.') from None
            funnel_on = True
        elif args.tunnel == 'cloudflare':
            cloudflared = Path(args.cloudflared).expanduser()
            if not cloudflared.is_file():
                raise RuntimeError('cloudflared is missing; set --cloudflared to the existing binary.')
            tunnel_log = STATE / 'tunnel.log'
            with tunnel_log.open('w') as log:
                tunnel = subprocess.Popen([str(cloudflared), 'tunnel', '--protocol', 'http2', '--url',
                    f'http://127.0.0.1:{args.port}'], stdout=log, stderr=subprocess.STDOUT)
            children.append(tunnel)
            deadline = time.monotonic() + 90
            while time.monotonic() < deadline and not stop:
                text = tunnel_log.read_text(errors='replace')
                match = re.search(r'https://[a-z0-9-]+\.trycloudflare\.com', text)
                if match and 'Registered tunnel connection' in text:
                    origin = match.group(0)
                    break
                if tunnel.poll() is not None:
                    raise RuntimeError('Tunnel exited; inspect out/interface_service/tunnel.log.')
                time.sleep(.5)
            if not origin:
                raise RuntimeError('No registered HTTPS tunnel; inspect tunnel.log.')
        command = [sys.executable, str(HERE / 'server.py'), '--port', str(args.port), '--out', str(JOB_ROOT)]
        if args.adapter and not args.demo:
            command += ['--adapter', str(args.adapter.resolve()), '--idle-minutes', str(args.idle_minutes)]
        if origin:
            command += ['--public-origin', origin]
        if args.demo:
            command += ['--demo']
        with (STATE / 'web.log').open('a') as log:
            web = subprocess.Popen(command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
        children.append(web)
        url = origin or f'http://127.0.0.1:{args.port}'
        deadline = time.monotonic() + 30
        while time.monotonic() < deadline and not stop:
            try:
                with urlopen(f'http://127.0.0.1:{args.port}/api/session', timeout=2) as response:
                    if response.status == 200:
                        break
            except OSError:
                if web.poll() is not None:
                    raise RuntimeError('Web server exited; inspect out/interface_service/web.log.')
                time.sleep(.3)
        else:
            raise RuntimeError('Web server did not become ready.')
        state.update(state='ready', url=url)
        save()
        while not stop:
            if any(child.poll() is not None for child in children):
                raise RuntimeError('A service exited. Inspect logs, then run start again. The public URL may change.')
            time.sleep(1)
    except Exception as error:
        state.update(state='error', error=str(error))
        save()
    finally:
        # Signal only child processes we created; their PID handles are still held.
        for child in reversed(children):
            if child.poll() is None:
                child.terminate()
        for child in reversed(children):
            try:
                child.wait(timeout=40)
            except subprocess.TimeoutExpired:
                child.kill()
                child.wait()
        if funnel_on:
            subprocess.run(['tailscale', 'funnel', '--https=443', 'off'], stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, timeout=60)
        if state['state'] != 'error':
            state['state'] = 'stopped'
        save()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['start', 'status', 'token', 'stop', 'doctor', '_serve'])
    parser.add_argument('--tunnel', choices=['tailscale', 'cloudflare', 'none'], default='tailscale',
                        help='tailscale: stable https://notes2pdf.<tailnet>.ts.net; cloudflare: random trycloudflare.com link; none: localhost only')
    parser.add_argument('--demo', action='store_true', help='Source-preview interface test; NO OCR inference.')
    parser.add_argument('--port', type=int, default=7860)
    parser.add_argument('--cloudflared', default='~/.local/bin/cloudflared')
    parser.add_argument('--adapter', type=Path, default=ROOT / 'runs/final_clean/final_adapter', help='Trained adapter (default: runs/final_clean/final_adapter).')
    parser.add_argument('--idle-minutes', type=int, default=15, help='Unload models after this long without uploads.')
    parser.add_argument('--nonce', help=argparse.SUPPRESS)
    args = parser.parse_args()
    STATE.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(STATE, 0o700)
    if args.action == 'doctor':
        doctor(args.demo, args.adapter)
    elif args.action == '_serve':
        supervise(args)
    elif args.action == 'token':
        path = JOB_ROOT / '.access-token'
        if not path.is_file():
            raise SystemExit('Start the service once before retrieving its access key.')
        print(path.read_text().strip())
    elif args.action == 'status':
        state = read_state()
        print(json.dumps({**state, 'supervisor_running': owned(state)}, indent=2))
    elif args.action == 'stop':
        state = read_state()
        if not owned(state):
            raise SystemExit('No owned deployment is running; no processes were stopped.')
        # Do not interrupt a conversion to tidy up terminal sessions.
        port = state.get('port', args.port)
        try:
            from urllib.request import Request
            key_file = JOB_ROOT / '.operator-token'
            if not key_file.exists():
                key_file = JOB_ROOT / '.access-token'  # migration from the earlier UI
            key = key_file.read_text().strip()
            with urlopen(Request(f'http://127.0.0.1:{port}/api/health', headers={'Authorization': 'Bearer ' + key}), timeout=3) as r:
                if json.load(r)['busy']:
                    raise SystemExit('Conversion is running. Wait before stopping the service.')
        except OSError:
            if state.get('state') == 'ready':
                raise SystemExit('Cannot verify the web server is idle. Inspect web.log before stopping it.')
        os.kill(state['pid'], signal.SIGTERM)
        deadline = time.monotonic() + 50
        while owned(state) and time.monotonic() < deadline:
            time.sleep(.2)
        if owned(state):
            raise SystemExit('Shutdown is still in progress; check status before restarting.')
        print('Stopped this deployment only; other tmux sessions are untouched.')
    else:
        if owned(read_state()):
            print('Already running. Use manage.py status for its URL.')
            return
        doctor(args.demo, args.adapter)
        nonce = secrets.token_hex(16)
        command = [sys.executable, str(HERE / 'manage.py'), '_serve', '--nonce', nonce, '--port', str(args.port),
                   '--cloudflared', args.cloudflared, '--tunnel', args.tunnel, '--idle-minutes', str(args.idle_minutes)]
        if args.adapter: command += ['--adapter', str(args.adapter.resolve())]
        if args.demo: command += ['--demo']
        with (STATE / 'supervisor.log').open('a') as log:
            proc = subprocess.Popen(command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        # Bounded command; services continue after terminal disconnects.
        deadline = time.monotonic() + 12
        while time.monotonic() < deadline:
            state = read_state()
            if state.get('nonce') == nonce and state.get('state') in ('ready', 'error'):
                print(json.dumps(state, indent=2))
                return
            if proc.poll() is not None:
                raise SystemExit('Supervisor exited; inspect supervisor.log.')
            time.sleep(.3)
        print('Starting in the background. Run manage.py status in a few seconds.')


def url_port(url, default):
    from urllib.parse import urlsplit
    return urlsplit(url or '').port or default


if __name__ == '__main__':
    main()
