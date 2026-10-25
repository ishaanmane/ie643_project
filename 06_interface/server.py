"""Authenticated, loopback-only notes interface served by Waitress."""
import argparse
import base64
from collections import deque
from datetime import timedelta
from functools import partial
import hashlib
import json
import logging
import os
from pathlib import Path
import re
import secrets
import shutil
import threading
import time
from urllib.parse import urlsplit
import uuid

from flask import Flask, jsonify, request, send_file, session
from werkzeug.exceptions import HTTPException
from pipeline import CleanRecognizer, DEFAULT_ADAPTER, IMAGE_TYPES, run_document

MAX_FILES = 20
MAX_UPLOAD = 25 * 1024 * 1024
MAX_STORED_JOBS = 50
MIN_FREE_BYTES = 1024 * 1024 * 1024
MAX_REQUEST = 36 * 1024 * 1024  # JSON/base64 compatibility; browser uses multipart.
LOG = logging.getLogger('intra')
ID = re.compile(r'^[a-f0-9]{32}$')

def matches(value, expected):
    return isinstance(value, str) and secrets.compare_digest(value.encode(), expected.encode())


def private_token(root, filename='.access-token'):
    """Persist a credential without truncating an existing file or following symlinks."""
    path = Path(root) / filename
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        if path.is_symlink() or not path.is_file():
            raise ValueError('Credential path must be a regular file.')
    else:
        with os.fdopen(fd, 'w') as stream:
            stream.write(secrets.token_urlsafe(32) + '\n')
    os.chmod(path, 0o600)
    token = path.read_text().strip()
    if not re.fullmatch(r'[A-Za-z0-9_-]{40,128}', token):
        raise ValueError('Invalid credential file; do not use a short password.')
    return token


class Application:
    def __init__(self, root, recognizer, runner=run_document, retention_hours=24, demo=False):
        self.root = Path(root).resolve()
        self.root.mkdir(parents=True, exist_ok=True, mode=0o700)
        os.chmod(self.root, 0o700)
        self.token = private_token(self.root)
        self.signing_secret = private_token(self.root, '.session-secret')
        self.operator_token = private_token(self.root, '.operator-token')
        self.recognizer, self.runner = recognizer, runner
        self.retention = retention_hours * 3600
        self.demo = demo
        self.lock = threading.RLock()
        self.jobs, self.active = {}, None
        self.login_attempts = deque(maxlen=32)
        self._restore()
        self.cleanup()

    def _save(self, jid):
        folder = self.root / jid
        temp = folder / 'status.tmp'
        temp.write_text(json.dumps(self.jobs[jid], indent=2))
        os.replace(temp, folder / 'status.json')

    def _restore(self):
        for folder in self.root.iterdir():
            if not ID.fullmatch(folder.name) or folder.is_symlink() or not folder.is_dir():
                continue
            try:
                data = json.loads((folder / 'status.json').read_text())
                if data.get('id') != folder.name or not isinstance(data.get('created'), (float, int)):
                    continue
                self.jobs[folder.name] = data
                if data['status'] == 'running':
                    data.update(status='error', message='The server restarted during conversion. Upload again to retry.')
                    self._save(folder.name)
            except (OSError, ValueError, KeyError):
                # Never expose or execute an incomplete job after restart.
                continue

    def cleanup(self):
        with self.lock:
            for jid, job in list(self.jobs.items()):
                if jid != self.active and time.time() - job['created'] > self.retention:
                    shutil.rmtree(self.root / jid)
                    del self.jobs[jid]

    def submit(self, payload, owner='operator'):
        """Compatibility for scripted JSON uploads; enforce limits after decoding too."""
        if not isinstance(payload, dict) or not isinstance(payload.get('files'), list):
            raise ValueError('Choose supported files.')
        if not 1 <= len(payload['files']) <= MAX_FILES:
            raise ValueError('Choose between 1 and 20 files.')
        files = []
        total = 0
        for item in payload['files']:
            if not isinstance(item, dict) or not isinstance(item.get('name'), str):
                raise ValueError('Invalid upload item.')
            encoded = item.get('data', '')
            if not isinstance(encoded, str) or len(encoded) > ((MAX_UPLOAD + 2) // 3) * 4:
                raise ValueError('Keep total uploads below 25 MiB.')
            try:
                data = base64.b64decode(encoded, validate=True)
            except (ValueError, TypeError):
                raise ValueError('Invalid file encoding.') from None
            total += len(data)
            if total > MAX_UPLOAD:
                raise ValueError('Keep total uploads below 25 MiB.')
            files.append((item['name'], data))
        return self.submit_files(files, payload.get('title', 'Lecture notes'), owner)

    def submit_files(self, files, title, owner='operator'):
        if not 1 <= len(files) <= MAX_FILES:
            raise ValueError('Choose between 1 and 20 files.')
        if not isinstance(title, str) or not 1 <= len(title.strip()) <= 120 or any(ord(c) < 32 for c in title):
            raise ValueError('Use a title of 1–120 characters without control characters.')
        # Titles are plain text, never a source of TeX commands.
        if '\\' in title or '<' in title or '>' in title:
            raise ValueError('Use a plain-text document title.')
        total = 0
        prepared = []
        for name, content in files:
            if not isinstance(name, str):
                raise ValueError('Invalid filename.')
            name = Path(name.replace('\\', '/')).name
            suffix = Path(name).suffix.lower()
            if suffix not in IMAGE_TYPES | {'.pdf'}:
                raise ValueError('Use PDF, HEIC/HEIF, JPEG, PNG, WebP, BMP or TIFF.')
            if not content:
                raise ValueError('Empty files cannot be converted.')
            total += len(content)
            if total > MAX_UPLOAD:
                raise ValueError('Keep total uploads below 25 MiB.')
            prepared.append((suffix, content))
        self.cleanup()
        with self.lock:
            if self.active:
                raise BlockingIOError('Another conversion is running. Try again when it finishes.')
            if len(self.jobs) >= MAX_STORED_JOBS or shutil.disk_usage(self.root).free < MIN_FREE_BYTES:
                raise ValueError('The workspace is full. Delete completed jobs or ask the operator to free space.')
            jid = uuid.uuid4().hex
            self.active = jid
            self.jobs[jid] = dict(id=jid, owner=owner, created=time.time(), status='running',
                                  message='Checking your files', result=None)
            try:
                inputs = self.root / jid / 'inputs'
                inputs.mkdir(parents=True, mode=0o700)
                paths = []
                for i, (suffix, content) in enumerate(prepared, 1):
                    path = inputs / f'{i:03d}{suffix}'
                    path.write_bytes(content)
                    paths.append(path)
                self._save(jid)
                threading.Thread(target=self.worker, args=(jid, paths, title.strip()), daemon=True).start()
            except Exception:
                self.active = None
                shutil.rmtree(self.root / jid, ignore_errors=True)
                self.jobs.pop(jid, None)
                raise
        return jid

    def worker(self, jid, paths, title):
        def update(message):
            with self.lock:
                self.jobs[jid]['message'] = message
                self._save(jid)
        try:
            result = self.runner(paths, self.root / jid / 'output', self.recognizer,
                                 title=title, max_pages=20, progress=update)
            with self.lock:
                self.jobs[jid].update(status='done', message='Your document is ready', result=result)
        except Exception as error:
            LOG.exception('Conversion failed for job %s', jid)
            # Detailed paths/tracebacks belong on the machine, not the public endpoint.
            message = str(error) if isinstance(error, ValueError) else 'Conversion failed. Ask the operator to inspect this job’s logs.'
            with self.lock:
                self.jobs[jid].update(status='error', message=message[:300])
        finally:
            with self.lock:
                self._save(jid)
                self.active = None

    def get(self, jid, owner='operator'):
        with self.lock:
            job = self.jobs.get(jid)
            if not job or (owner != 'operator' and job.get('owner') != owner):
                return None
            return {key: job[key] for key in ('id', 'created', 'status', 'message', 'result')}

    def delete(self, jid, owner):
        with self.lock:
            if not self.get(jid, owner):
                return False
            if jid == self.active:
                raise BlockingIOError('Wait for conversion to finish before deleting it.')
            shutil.rmtree(self.root / jid)
            del self.jobs[jid]
            return True


def create_app(application, public_origin=None):
    if public_origin:
        parsed = urlsplit(public_origin)
        if parsed.scheme != 'https' or not parsed.hostname or parsed.path not in ('', '/') or parsed.query or parsed.fragment or parsed.username:
            raise ValueError('Public origin must be an HTTPS origin without a path or credentials.')
        public_origin = public_origin.rstrip('/')
    app = Flask(__name__, static_folder=None)
    app.config.update(SECRET_KEY=hashlib.sha256(application.signing_secret.encode()).digest(),
                      MAX_CONTENT_LENGTH=MAX_REQUEST, MAX_FORM_MEMORY_SIZE=512 * 1024,
                      MAX_FORM_PARTS=MAX_FILES + 2, SESSION_COOKIE_NAME='intra_session',
                      SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Strict',
                      SESSION_COOKIE_SECURE=bool(public_origin), PERMANENT_SESSION_LIFETIME=timedelta(hours=8),
                      TRUSTED_HOSTS=['127.0.0.1', 'localhost'] + ([urlsplit(public_origin).hostname] if public_origin else []))
    app.extensions['intra'] = application

    def owner():
        supplied = request.headers.get('Authorization', '')
        if supplied.startswith('Bearer ') and matches(supplied[7:], application.operator_token):
            return 'operator'
        return session.get('owner')

    @app.before_request
    def guard():
        if request.method in ('POST', 'DELETE'):
            origin = request.headers.get('Origin')
            allowed = public_origin or request.host_url.rstrip('/')
            if origin and origin != allowed:
                return jsonify(error='This request came from a different site.'), 403
        if request.path in ('/', '/app.js', '/style.css', '/api/session'):
            return None
        if not owner():
            return jsonify(error='Sign in with the demo access key.'), 401
        if request.method in ('POST', 'DELETE') and owner() != 'operator':
            if not matches(request.headers.get('X-CSRF-Token', ''), session.get('csrf', '')):
                return jsonify(error='Your session changed. Refresh and sign in again.'), 403

    @app.after_request
    def headers(response):
        response.headers.update({'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff',
            'Referrer-Policy': 'no-referrer', 'X-Frame-Options': 'DENY',
            'Permissions-Policy': 'camera=(), microphone=(), geolocation=()',
            'Content-Security-Policy': "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' blob:; connect-src 'self'; frame-ancestors 'none'; object-src 'none'; base-uri 'none'; form-action 'self'"})
        if public_origin:
            response.headers['Strict-Transport-Security'] = 'max-age=86400'
        return response

    @app.errorhandler(HTTPException)
    def http_error(error):
        message = 'Keep total uploads below 25 MiB.' if error.code == 413 else error.description
        return jsonify(error=message), error.code

    @app.errorhandler(Exception)
    def unexpected(error):
        LOG.exception('Interface request failed')
        return jsonify(error='The server could not complete this request.'), 500

    @app.get('/')
    def index():
        return send_file(Path(__file__).with_name('index.html'))

    @app.get('/app.js')
    @app.get('/style.css')
    def asset():
        return send_file(Path(__file__).with_name(request.path[1:]))

    @app.route('/api/session', methods=['GET', 'POST', 'DELETE'])
    def login():
        if request.method == 'POST':
            with application.lock:
                now = time.monotonic()
                while application.login_attempts and application.login_attempts[0] < now - 60:
                    application.login_attempts.popleft()
                if len(application.login_attempts) >= 8:
                    return jsonify(error='Too many sign-in attempts. Wait one minute.'), 429
                application.login_attempts.append(now)
            payload = request.get_json(silent=True) or {}
            key = payload.get('token', '') if isinstance(payload, dict) else ''
            if not isinstance(key, str) or not matches(key, application.token):
                return jsonify(error='That access key is not valid.'), 401
            session.clear()
            session.update(owner=secrets.token_urlsafe(24), csrf=secrets.token_urlsafe(24))
            session.permanent = True
        elif request.method == 'DELETE':
            if not owner() or not matches(request.headers.get('X-CSRF-Token', ''), session.get('csrf', '')):
                return jsonify(error='Refresh your session before signing out.'), 403
            session.clear()
        return jsonify(authenticated=bool(owner()), csrf=session.get('csrf'), demo=application.demo,
                       limits=dict(files=MAX_FILES, pages=20, bytes=MAX_UPLOAD, retention_hours=application.retention / 3600))

    @app.get('/api/health')
    def health():
        application.cleanup()
        return jsonify(status='ready', busy=application.active is not None, demo=application.demo)

    @app.get('/api/jobs')
    def recent_jobs():
        application.cleanup()
        with application.lock:
            jobs = [application.get(jid, owner()) for jid in application.jobs]
        jobs = sorted((j for j in jobs if j), key=lambda j: j['created'], reverse=True)[:10]
        return jsonify(jobs=jobs)

    @app.post('/api/jobs')
    def submit():
        if application.active:
            return jsonify(error='Another conversion is running. Try again when it finishes.'), 409
        try:
            if request.is_json:
                jid = application.submit(request.get_json(), owner())
            else:
                uploads = request.files.getlist('files')
                if not 1 <= len(uploads) <= MAX_FILES:
                    raise ValueError('Choose between 1 and 20 files.')
                files, total = [], 0
                for upload in uploads:
                    data = upload.stream.read(MAX_UPLOAD - total + 1)
                    total += len(data)
                    if total > MAX_UPLOAD:
                        return jsonify(error='Keep total uploads below 25 MiB.'), 413
                    files.append((upload.filename, data))
                jid = application.submit_files(files, request.form.get('title', 'Lecture notes'), owner())
            return jsonify(id=jid), 202
        except BlockingIOError as error:
            return jsonify(error=str(error)), 409
        except ValueError as error:
            return jsonify(error=str(error)), 400

    @app.get('/api/jobs/<jid>')
    def job(jid):
        application.cleanup()
        value = application.get(jid, owner())
        return (jsonify(value), 200) if value else (jsonify(error='Job expired or unavailable in this browser session.'), 404)

    @app.delete('/api/jobs/<jid>')
    def delete(jid):
        try:
            return (jsonify(deleted=True), 200) if application.delete(jid, owner()) else (jsonify(error='Job not found.'), 404)
        except BlockingIOError as error:
            return jsonify(error=str(error)), 409

    @app.get('/download/<jid>/<kind>')
    def download(jid, kind):
        application.cleanup()
        value = application.get(jid, owner())
        if not value or value['status'] != 'done' or kind not in ('pdf', 'markdown', 'bundle', 'report'):
            return jsonify(error='Download unavailable.'), 404
        root = (application.root / jid / 'output').resolve()
        relative = value['result'].get(kind)
        if not isinstance(relative, str):
            return jsonify(error='Download unavailable.'), 404
        path = (root / relative).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            return jsonify(error='Download unavailable.'), 404
        return send_file(path, as_attachment=True, conditional=False, download_name=path.name)

    return app


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--adapter', type=Path, help='Explicit adapter from the corrected-data training run.')
    parser.add_argument('--layout', choices=['surya', 'none'], default='surya')
    parser.add_argument('--port', type=int, default=7860)
    parser.add_argument('--out', type=Path, default=Path('out/upload_jobs'))
    parser.add_argument('--public-origin', help='Exact HTTPS tunnel origin; required for public deployment.')
    parser.add_argument('--demo', action='store_true', help='Mac interface test: source preview PDF only, NO model inference.')
    args = parser.parse_args()
    if args.demo:
        from demo import run_demo
        recognizer, runner = None, run_demo
    else:
        if args.adapter is None:
            parser.error('Specify --adapter with the corrected-data model directory.')
        recognizer, runner = CleanRecognizer(args.adapter), partial(run_document, layout_mode=args.layout)
    application = Application(args.out, recognizer, runner, demo=args.demo)
    def expire_jobs():
        while True:
            time.sleep(60)
            try:
                application.cleanup()
            except OSError:
                LOG.exception('Job expiry cleanup failed')
    threading.Thread(target=expire_jobs, daemon=True).start()
    # One server process owns the GPU lock; never launch multiple WSGI workers.
    from waitress import serve
    print(f'Interface: {args.public_origin or "http://127.0.0.1:" + str(args.port)}', flush=True)
    print(f'Access key: stored privately at {application.root / ".access-token"}; use manage.py token to display it.', flush=True)
    if args.demo:
        print('INTERFACE TEST MODE: real file decoding, no OCR or layout model.', flush=True)
    serve(create_app(application, args.public_origin), host='127.0.0.1', port=args.port,
          threads=4, connection_limit=12, channel_timeout=60, max_request_body_size=MAX_REQUEST,
          max_request_header_size=16384, clear_untrusted_proxy_headers=True, expose_tracebacks=False)


if __name__ == '__main__':
    main()
