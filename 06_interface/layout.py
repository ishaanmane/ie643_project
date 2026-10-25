"""Managed, isolated Surya v2 server. Never stops a server it did not start."""
import json
import os
from pathlib import Path
import signal
import socket
import subprocess
import sys
import time
from urllib.request import urlopen

MODEL = 'datalab-to/surya-ocr-2'
ENV_ROOT = Path('/home/intralab/workspace/ie643_layout_envs')


def convert_results(results, data, pages):
    from PIL import Image
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '02_layout'))
    from surya_to_tags import convert_page
    raw = json.loads(Path(results).read_text())
    mapped = {Path(k).stem: v for k, v in raw.items()}
    if set(mapped) != set(pages):
        raise ValueError('Surya page coverage does not match the uploaded pages.')
    crops = data / 'crops'; crops.mkdir(exist_ok=True)
    prepared = []
    for page in pages:
        entries = mapped[page]
        if not isinstance(entries, list) or len(entries) != 1 or entries[0].get('error'):
            raise ValueError(f'Invalid Surya result: {page}')
        item = entries[0]
        image_path = data / 'processed' / (page + '.jpg')
        with Image.open(image_path) as image:
            w, h = image.size
        if item.get('image_bbox') != [0, 0, w, h]:
            raise ValueError(f'Surya/image coordinate mismatch: {page}')
        for box in item['bboxes']:
            x0, y0, x1, y1 = box['bbox']
            if not (0 <= x0 < x1 <= w and 0 <= y0 < y1 <= h):
                raise ValueError(f'Invalid Surya bounding box: {page}')
        prepared.append((page, item, image_path))
    for page, item, image_path in prepared:
        tags, warning = convert_page(page, item, str(image_path), str(crops))
        if warning: raise ValueError(warning)
        tags['source'] = 'surya-ocr 0.22.1 / ' + MODEL + '; unverified'
        (data / 'tags_draft' / (page + '.json')).write_text(json.dumps(tags, indent=2))


def stop_owned_server(proc):
    # vLLM has GPU worker children; terminate the entire private process group.
    try: os.killpg(proc.pid, signal.SIGTERM)
    except ProcessLookupError: pass
    deadline = time.monotonic() + 30
    while time.monotonic() < deadline:
        proc.poll()
        try: os.killpg(proc.pid, 0)
        except ProcessLookupError: return
        time.sleep(.25)
    try: os.killpg(proc.pid, signal.SIGKILL)
    except ProcessLookupError: pass
    proc.wait(timeout=10)


def run_layout(data, pages, output, progress, timeout=1800):
    env_root = Path(os.environ.get('IE643_LAYOUT_ENVS', str(ENV_ROOT)))
    surya = env_root / 'surya0221/bin'
    vllm = env_root / 'vllm0320/bin'
    for python, package, expected in [(surya/'python', 'surya-ocr', '0.22.1'),
                                      (vllm/'python', 'vllm', '0.32.0')]:
        installed = subprocess.check_output([str(python), '-c',
            f'from importlib.metadata import version; print(version({package!r}))'], text=True).strip()
        if installed != expected:
            raise RuntimeError(f'{package}: expected {expected}, found {installed}')
    port = int(os.environ.get('IE643_LAYOUT_PORT', '8001'))
    with socket.socket() as probe:
        try: probe.bind(('127.0.0.1', port))
        except OSError:
            raise RuntimeError(f'Port {port} is occupied. Stop the manual Surya server before using managed layout.')
    env = os.environ.copy()
    env['SURYA_INFERENCE_BACKEND'] = 'vllm'
    env['SURYA_INFERENCE_URL'] = f'http://127.0.0.1:{port}/v1'
    env.setdefault('HF_HOME', '/home/intralab/workspace/hf_cache')
    layout_out = output / 'surya_layout'
    layout_out.mkdir()
    command = [str(vllm/'vllm'), 'serve', MODEL, '--host', '127.0.0.1', '--port', str(port),
               '--dtype', 'half', '--max-model-len', '8192', '--max-num-batched-tokens', '8192',
               '--limit-mm-per-prompt', '{"video": 0}', '--enforce-eager',
               '--gpu-memory-utilization', '0.90']
    progress('Loading tested Surya v2 layout model')
    with (layout_out/'server.log').open('w') as log:
        proc = subprocess.Popen(command, env=env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        try:
            deadline = time.monotonic() + 600
            while True:
                if proc.poll() is not None:
                    raise RuntimeError('Surya server exited; inspect surya_layout/server.log.')
                try:
                    with urlopen(env['SURYA_INFERENCE_URL']+'/models', timeout=2) as response:
                        models = json.load(response)
                    if any(m['id'] == MODEL for m in models.get('data', [])): break
                except (OSError, ValueError): pass
                if time.monotonic() >= deadline:
                    raise RuntimeError('Surya startup timed out; inspect surya_layout/server.log.')
                time.sleep(2)
            progress(f'Detecting diagrams and layout on {len(pages)} pages')
            with (layout_out/'client.log').open('w') as client_log:
                subprocess.run([str(surya/'surya_layout'), str(data/'processed'), '--images',
                                '--output_dir', str(layout_out)], env=env, stdout=client_log,
                               stderr=subprocess.STDOUT, check=True, timeout=timeout)
        finally:
            progress('Releasing Surya GPU memory')
            stop_owned_server(proc)
    convert_results(layout_out/'processed/results.json', data, pages)
    return {'model': MODEL, 'surya_version': '0.22.1', 'vllm_version': '0.32.0',
            'pages': len(pages), 'status': 'completed'}
