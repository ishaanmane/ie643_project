"""Persistent Qwen recognition worker: loads the model once, then reads one JSON request
per line on stdin and answers one JSON line on stdout. Ending the process frees the GPU.

Request:  {"image": "/path/page.jpg", "out": "/path/page.md"}
Answer:   {"ok": true, "generated_tokens": 812, "possibly_truncated": false}
          {"ok": false, "error": "..."}
The first line written is {"ready": true} once the model is loaded.
"""
import argparse
import json
from pathlib import Path
import sys

from pipeline import CleanRecognizer


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--adapter', required=True)
    p.add_argument('--max-pixels', type=int, default=1_000_000)
    p.add_argument('--max-new-tokens', type=int, default=2048)
    a = p.parse_args()
    out = sys.stdout
    sys.stdout = sys.stderr  # library prints must not corrupt the protocol
    recognizer = CleanRecognizer(a.adapter, a.max_pixels, a.max_new_tokens)
    recognizer.load()
    out.write(json.dumps({'ready': True}) + '\n'); out.flush()
    for line in sys.stdin:
        try:
            request = json.loads(line)
            text, details = recognizer.predict(request['image'])
            Path(request['out']).write_text(text)
            answer = {'ok': True, **details}
        except Exception as error:  # report and keep serving
            answer = {'ok': False, 'error': f'{type(error).__name__}: {error}'}
        out.write(json.dumps(answer) + '\n'); out.flush()


if __name__ == '__main__':
    main()
