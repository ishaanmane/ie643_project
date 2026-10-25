"""Local upload UI for the trained model. One conversion at a time; no new web framework."""
import argparse
import base64
import binascii
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mimetypes
from pathlib import Path
import secrets
import threading
import time
from urllib.parse import parse_qs, urlparse
import uuid

from pipeline import CleanRecognizer, DEFAULT_ADAPTER, IMAGE_TYPES, run_document

MAX_REQUEST = 40 * 1024 * 1024  # includes base64 overhead
MAX_FILES = 20


class Application:
    def __init__(self, root, recognizer, runner=run_document):
        self.root=Path(root).resolve();self.root.mkdir(parents=True,exist_ok=True)
        self.recognizer=recognizer;self.runner=runner
        self.token=secrets.token_urlsafe(32)
        self.lock=threading.Lock();self.jobs={};self.active=None

    def submit(self, payload):
        files=payload.get('files')
        if not isinstance(files,list) or not 1<=len(files)<=MAX_FILES:
            raise ValueError('Choose between 1 and 20 files.')
        title=payload.get('title','Lecture notes')
        if not isinstance(title,str) or not 1<=len(title.strip())<=120:
            raise ValueError('Title must contain 1–120 characters.')
        decoded=[]
        for item in files:
            if not isinstance(item,dict) or not isinstance(item.get('name'),str):
                raise ValueError('Invalid upload item.')
            name=Path(item['name']).name
            if Path(name).suffix.lower() not in IMAGE_TYPES | {'.pdf'}:
                raise ValueError('Upload PDF or supported image files.')
            try:
                content=base64.b64decode(item.get('data',''),validate=True)
            except (ValueError,TypeError,binascii.Error):
                raise ValueError('Invalid file encoding.')
            if not content: raise ValueError('Empty files cannot be converted.')
            decoded.append((name,content))
        with self.lock:
            if self.active:
                raise BlockingIOError('A conversion is already running. Wait for it to finish.')
            jid=uuid.uuid4().hex
            self.active=jid
            self.jobs[jid]={'id':jid,'status':'running','message':'Preparing uploaded files','result':None}
        try:
            inputs=self.root/jid/'inputs';inputs.mkdir(parents=True)
            paths=[]
            for i,(name,content) in enumerate(decoded):
                path=inputs/f'{i+1:03d}_{name}';path.write_bytes(content);paths.append(path)
            thread=threading.Thread(target=self.worker,args=(jid,paths,title.strip()),daemon=True)
            thread.start()
        except Exception:
            with self.lock:
                self.active=None;self.jobs[jid]['status']='error'
            raise
        return jid

    def worker(self,jid,paths,title):
        def update(message):
            with self.lock:
                self.jobs[jid]['message']=message
        try:
            output=self.root/jid/'output'
            result=self.runner(paths,output,self.recognizer,title=title,max_pages=20,progress=update)
            with self.lock:
                self.jobs[jid].update(status='done',message='Conversion complete',result=result)
        except Exception as error:
            with self.lock:
                self.jobs[jid].update(status='error',message=str(error))
        finally:
            with self.lock:
                self.active=None
                snapshot=dict(self.jobs[jid])
            (self.root/jid/'status.json').write_text(json.dumps(snapshot,indent=2))

    def get(self,jid):
        with self.lock:
            return dict(self.jobs[jid]) if jid in self.jobs else None


def make_handler(app):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,format,*args):
            # Download links include an access token; never print request paths.
            pass

        def respond(self,status,body,content_type='application/json'):
            if not isinstance(body,bytes): body=json.dumps(body).encode()
            self.send_response(status)
            self.send_header('Content-Type',content_type)
            self.send_header('Content-Length',str(len(body)))
            self.send_header('Cache-Control','no-store')
            self.send_header('X-Content-Type-Options','nosniff')
            self.send_header('Referrer-Policy','no-referrer')
            self.end_headers()
            self.wfile.write(body)

        def authenticated(self):
            query=parse_qs(urlparse(self.path).query)
            supplied=self.headers.get('Authorization','').removeprefix('Bearer ')
            supplied=supplied or query.get('token',[''])[0]
            return secrets.compare_digest(supplied,app.token)

        def do_GET(self):
            path=urlparse(self.path).path
            if path=='/':
                return self.respond(200,Path(__file__).with_name('index.html').read_bytes(),'text/html; charset=utf-8')
            if not self.authenticated(): return self.respond(401,{'error':'Open the full URL printed by the server, including its access token.'})
            if path=='/api/health':
                return self.respond(200,{'status':'ready','active':app.active})
            if path.startswith('/api/jobs/'):
                job=app.get(path.rsplit('/',1)[-1])
                return self.respond(200,job) if job else self.respond(404,{'error':'Job not found; the server may have restarted.'})
            if path.startswith('/download/'):
                parts=path.strip('/').split('/')
                if len(parts)!=3: return self.respond(404,{'error':'Unknown download'})
                _,jid,kind=parts
                job=app.get(jid)
                if not job or job['status']!='done' or kind not in ('pdf','markdown','bundle','report'):
                    return self.respond(404,{'error':'Download not ready'})
                root=(app.root/jid/'output').resolve()
                target=(root/job['result'][kind]).resolve()
                if not target.is_relative_to(root) or not target.is_file():
                    return self.respond(404,{'error':'File unavailable'})
                self.send_response(200)
                self.send_header('Content-Type',mimetypes.guess_type(target.name)[0] or 'application/octet-stream')
                self.send_header('Content-Length',str(target.stat().st_size))
                self.send_header('Content-Disposition',f'attachment; filename="{target.name}"')
                self.send_header('Cache-Control','no-store');self.send_header('Referrer-Policy','no-referrer')
                self.end_headers()
                with target.open('rb') as stream:
                    while True:
                        block=stream.read(1024*1024)
                        if not block: break
                        self.wfile.write(block)
                return
            return self.respond(404,{'error':'Not found'})

        def do_POST(self):
            if not self.authenticated(): return self.respond(401,{'error':'Access token missing or invalid.'})
            if urlparse(self.path).path!='/api/jobs': return self.respond(404,{'error':'Not found'})
            try:
                size=int(self.headers.get('Content-Length','0'))
                if not 0<size<=MAX_REQUEST:
                    return self.respond(413,{'error':'Upload is too large. Keep total files below 25 MiB.'})
                self.connection.settimeout(60)
                payload=json.loads(self.rfile.read(size))
                if not isinstance(payload,dict): raise ValueError('Expected an upload object.')
                jid=app.submit(payload)
                return self.respond(202,{'id':jid})
            except BlockingIOError as error:
                return self.respond(409,{'error':str(error)})
            except (ValueError,TypeError,TimeoutError) as error:
                return self.respond(400,{'error':str(error)})
    return Handler


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--adapter',type=Path,default=DEFAULT_ADAPTER)
    parser.add_argument('--port',type=int,default=7860)
    parser.add_argument('--out',type=Path,default=Path('out/upload_jobs'))
    args=parser.parse_args()
    app=Application(args.out,CleanRecognizer(args.adapter))
    server=ThreadingHTTPServer(('127.0.0.1',args.port),make_handler(app))
    print(f'Open on this machine or through port forwarding:\nhttp://127.0.0.1:{args.port}/#token={app.token}',flush=True)
    print('One conversion at a time. First conversion loads the trained model. Keep this tmux pane running.',flush=True)
    server.serve_forever()


if __name__=='__main__':
    main()
