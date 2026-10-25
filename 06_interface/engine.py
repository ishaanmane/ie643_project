"""Warm models for the interface: load on the first upload, stay loaded while uploads keep
coming, unload after an idle period so the GPU is free again.

Both models stay on the GPU together (about 13 GB of 16): Surya through its own vLLM server
with a reduced memory share, Qwen + the trained adapter in one persistent worker process.
Unloading = stopping those processes, which frees all their GPU memory.
"""
import json
from pathlib import Path
import subprocess
import sys
import threading
import time

from layout import SuryaServer
from pipeline import adapter_config, validate_prediction

HERE = Path(__file__).resolve().parent


class WarmModels:
    def __init__(self, adapter, log_dir, idle_minutes=15, max_pixels=1_000_000, max_new_tokens=2048,
                 surya_gpu_fraction=0.35):
        self.adapter = Path(adapter).resolve()
        adapter_config(self.adapter)
        self.max_pixels, self.max_new_tokens = max_pixels, max_new_tokens
        self.log_dir = Path(log_dir); self.log_dir.mkdir(parents=True, exist_ok=True)
        self.idle_seconds = idle_minutes * 60
        self.surya = SuryaServer(self.log_dir, gpu_fraction=surya_gpu_fraction)
        self.qwen = None
        self.lock = threading.RLock()       # one job at a time uses the models
        self.qwen_lock = threading.Lock()   # one request at a time on the worker pipe
        self.last_used = time.monotonic()
        self.busy = False
        threading.Thread(target=self._idle_watch, daemon=True).start()

    # ---- state -------------------------------------------------------------------------
    @property
    def loaded(self):
        return self.surya.running or (self.qwen is not None and self.qwen.poll() is None)

    def status(self):
        idle = time.monotonic() - self.last_used
        return {'loaded': self.loaded, 'busy': self.busy,
                'unloads_in_seconds': max(0, int(self.idle_seconds - idle)) if self.loaded and not self.busy else None}

    def __enter__(self):
        self.lock.acquire(); self.busy = True
        return self

    def __exit__(self, *exc):
        self.busy = False; self.last_used = time.monotonic(); self.lock.release()

    def _idle_watch(self):
        while True:
            time.sleep(30)
            self.unload_if_idle()

    def unload_if_idle(self):
        if self.loaded and not self.busy and time.monotonic() - self.last_used > self.idle_seconds:
            with self.lock:
                if not self.busy:
                    self.unload()
                    return True
        return False

    def unload(self):
        with self.lock:
            self.surya.stop()
            if self.qwen is not None:
                self.qwen.stdin.close()
                try: self.qwen.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    self.qwen.kill(); self.qwen.wait()
                self.qwen = None

    # ---- models ------------------------------------------------------------------------
    def _start_qwen(self, progress):
        if self.qwen is not None and self.qwen.poll() is None:
            return
        progress('Loading the recognition model (first upload only)')
        self.qwen = subprocess.Popen(  # same process group: dies with the server if it is killed
            [sys.executable, str(HERE / 'recognition_worker.py'), '--adapter', str(self.adapter),
             '--max-pixels', str(self.max_pixels), '--max-new-tokens', str(self.max_new_tokens)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=(self.log_dir / 'qwen_worker.log').open('a'),
            text=True, bufsize=1, cwd=HERE)
        line = self.qwen.stdout.readline()
        if not line or not json.loads(line).get('ready'):
            self.qwen = None
            raise RuntimeError(f'Recognition model failed to load; see {self.log_dir}/qwen_worker.log.')

    def layout(self, data, pages, output, progress):
        return self.surya.detect(data, pages, output, progress)

    def recognize(self, data, pages, output, progress):
        self._start_qwen(progress)
        results = []
        for i, page in enumerate(pages, 1):
            progress(f'Reading page {i} of {len(pages)}')
            target = Path(output) / 'predictions' / (page + '.md')
            with self.qwen_lock:
                self.qwen.stdin.write(json.dumps({'image': str(Path(data) / 'processed' / (page + '.jpg')),
                                                  'out': str(target)}) + '\n')
                line = self.qwen.stdout.readline()
            if not line:
                self.qwen = None
                raise RuntimeError(f'Recognition model stopped; see {self.log_dir}/qwen_worker.log.')
            answer = json.loads(line)
            if not answer.get('ok'):
                raise RuntimeError('Recognition failed: ' + answer.get('error', 'unknown error'))
            validate_prediction(target.read_text())
            results.append({'page': page, 'generated_tokens': answer['generated_tokens'],
                            'possibly_truncated': answer['possibly_truncated']})
        return results
