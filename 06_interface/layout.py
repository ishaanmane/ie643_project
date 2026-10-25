"""Surya v2 layout: a private vLLM server plus the surya_layout client.

SuryaServer can stay running between uploads (the interface keeps it warm and stops it
after an idle period); run_layout() is the one-shot batch form used by 02_layout/run_layout.py.
Never stops a server it did not start."""
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
        (data / 'tags' / (page + '.json')).write_text(json.dumps(tags, indent=2))


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


class SuryaServer:
    """Private vLLM server for Surya on localhost. gpu_fraction leaves room for Qwen
    when both stay loaded (0.35 of 16 GB is enough for the 0.7B model and its cache)."""

    def __init__(self, log_dir, gpu_fraction=0.35):
        env_root = Path(os.environ.get('IE643_LAYOUT_ENVS', str(ENV_ROOT)))
        self.surya, self.vllm = env_root / 'surya0221/bin', env_root / 'vllm0320/bin'
        self.port = int(os.environ.get('IE643_LAYOUT_PORT', '8001'))
        self.log_dir, self.gpu_fraction = Path(log_dir), gpu_fraction
        self.proc = None
        self.env = os.environ.copy()
        self.env.update(SURYA_INFERENCE_BACKEND='vllm', SURYA_INFERENCE_URL=f'http://127.0.0.1:{self.port}/v1')
        self.env.setdefault('HF_HOME', '/home/intralab/workspace/hf_cache')

    @property
    def running(self):
        return self.proc is not None and self.proc.poll() is None

    def start(self, progress=print):
        if self.running:
            return
        for python, package, expected in [(self.surya/'python', 'surya-ocr', '0.22.1'),
                                          (self.vllm/'python', 'vllm', '0.32.0')]:
            installed = subprocess.check_output([str(python), '-c',
                f'from importlib.metadata import version; print(version({package!r}))'], text=True).strip()
            if installed != expected:
                raise RuntimeError(f'{package}: expected {expected}, found {installed}')
        with socket.socket() as probe:
            try: probe.bind(('127.0.0.1', self.port))
            except OSError:
                raise RuntimeError(f'Port {self.port} is occupied. Stop the other Surya server first.')
        self.log_dir.mkdir(parents=True, exist_ok=True)
        command = [str(self.vllm/'vllm'), 'serve', MODEL, '--host', '127.0.0.1', '--port', str(self.port),
                   '--dtype', 'half', '--max-model-len', '8192', '--max-num-batched-tokens', '8192',
                   '--limit-mm-per-prompt', '{"video": 0}', '--enforce-eager',
                   '--gpu-memory-utilization', str(self.gpu_fraction)]
        progress('Loading the layout model (first upload only)')
        log = (self.log_dir/'surya_server.log').open('w')
        self.proc = subprocess.Popen(command, env=self.env, stdout=log, stderr=subprocess.STDOUT,
                                     start_new_session=True)
        deadline = time.monotonic() + 600
        while True:
            if self.proc.poll() is not None:
                self.proc = None
                raise RuntimeError(f'Surya server exited; see {self.log_dir}/surya_server.log.')
            try:
                with urlopen(self.env['SURYA_INFERENCE_URL'] + '/models', timeout=2) as response:
                    if any(m['id'] == MODEL for m in json.load(response).get('data', [])):
                        return
            except (OSError, ValueError):
                pass
            if time.monotonic() >= deadline:
                self.stop()
                raise RuntimeError('Surya startup timed out.')
            time.sleep(2)

    def detect(self, data, pages, output, progress=print, timeout=1800):
        """Layout for data/processed/*.jpg -> data/tags/ and data/crops/."""
        self.start(progress)
        layout_out = Path(output) / 'surya_layout'
        layout_out.mkdir(exist_ok=True)
        with (layout_out/'client.log').open('w') as client_log:
            subprocess.run([str(self.surya/'surya_layout'), str(Path(data)/'processed'), '--images',
                            '--output_dir', str(layout_out)], env=self.env, stdout=client_log,
                           stderr=subprocess.STDOUT, check=True, timeout=timeout)
        convert_results(layout_out/'processed/results.json', Path(data), pages)
        return {'model': MODEL, 'surya_version': '0.22.1', 'vllm_version': '0.32.0',
                'pages': len(pages), 'status': 'completed'}

    def stop(self):
        if self.proc is not None:
            stop_owned_server(self.proc)
            self.proc = None


def run_layout(data, pages, output, progress, timeout=1800):
    """One-shot: start Surya with the whole GPU, run all pages, stop it."""
    server = SuryaServer(Path(output) / 'surya_layout', gpu_fraction=0.90)
    progress(f'Detecting diagrams and layout on {len(pages)} pages')
    try:
        return server.detect(data, pages, output, progress, timeout)
    finally:
        progress('Releasing Surya GPU memory')
        server.stop()
