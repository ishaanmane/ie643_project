import base64
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from http.server import ThreadingHTTPServer

from PIL import Image
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import pipeline
from server import Application, make_handler


class InputTests(unittest.TestCase):
    def test_multi_page_images_preserve_order_and_enforce_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);source=root/'pages.tiff'
            Image.new('RGB',(50,80),'red').save(source,save_all=True,append_images=[Image.new('RGB',(50,80),'blue')])
            pages,manifest=pipeline.extract_pages([source],root/'pages')
            self.assertEqual(len(pages),2)
            self.assertEqual([m['input_page'] for m in manifest],[1,2])
            with self.assertRaisesRegex(ValueError,'page limit'):
                pipeline.extract_pages([source],root/'limited',max_pages=1)

    def test_pdf_rasterization(self):
        import fitz
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            with fitz.open() as pdf:
                pdf.new_page(width=200,height=300)
                pdf.save(root/'new.pdf')
            pages,_=pipeline.extract_pages([root/'new.pdf'],root/'pages')
            self.assertEqual(pages,['upload_notes_page001'])
            self.assertTrue((root/'pages'/f'{pages[0]}.jpg').exists())

    def test_prediction_resource_commands_rejected_but_math_allowed(self):
        pipeline.validate_prediction(r'## Notes\n$$\frac{x}{y}$$')
        for value in [r'\input{/etc/passwd}',r'\write18{something}', '![](https://example.com/a.png)', '<img src="x">', '']:
            with self.assertRaises(ValueError):pipeline.validate_prediction(value)

    def test_invalid_adapter_not_silently_base_model(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)
            (path/'adapter_config.json').write_text(json.dumps({'base_model_name_or_path':pipeline.MODEL_ID}))
            with self.assertRaisesRegex(ValueError,'weights'):
                pipeline.CleanRecognizer(path)

    def test_new_input_uses_isolated_data_and_source_appendix(self):
        class Recognizer:
            adapter='test-only'
            def predict(self,path):return '# Notes\n\n$$x=1$$',{'possibly_truncated':False}
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);source=root/'photo.png';Image.new('RGB',(120,180),'white').save(source)
            def fake_render(unit,pages,md_dir,out_root,fmt,**kwargs):
                self.assertEqual(unit,'upload_notes')
                self.assertEqual(len(kwargs['source_pages']),1)
                self.assertNotEqual(Path(kwargs['data_dir']),pipeline.ROOT/'data')
                dest=Path(out_root)/unit;dest.mkdir(parents=True)
                (dest/'upload_notes.pdf').write_bytes(b'unit-test-placeholder')
                (dest/'upload_notes.md').write_text('# Notes')
                return {'output':str(dest/'upload_notes.pdf'),'math':{'status':'completed','remaining_failed':0},
                        'pdf_audit':{'status':'completed','outside_words':0}}
            with patch('render_document.render_unit',side_effect=fake_render),patch('pipeline.shutil.which',return_value='/test'),patch('preprocess.NotesPreprocessor.process_with_info',return_value=(__import__('numpy').zeros((180,120,3),dtype='uint8'),{'crop':'test'})):
                result=pipeline.run_document([source],root/'job',Recognizer(),progress=lambda _:None)
            self.assertEqual(result['pages'],1)
            self.assertTrue((root/'job/document_bundle.zip').exists())
            self.assertTrue((root/'job/predictions/upload_notes_page001.md').exists())
            with self.assertRaisesRegex(ValueError,'never overwritten'):
                pipeline.run_document([source],root/'job',Recognizer())


class WebTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.gate=threading.Event()
        def runner(inputs,output,recognizer,**kwargs):
            self.gate.wait(3)
            output=Path(output);output.mkdir()
            (output/'result.pdf').write_bytes(b'test-only')
            return {'pdf':'result.pdf','markdown':'missing.md','bundle':'missing.zip','report':'missing.json',
                    'warnings':[],'pages':1,'elapsed_seconds':1}
        self.app=Application(self.temp.name,None,runner)
        self.server=ThreadingHTTPServer(('127.0.0.1',0),make_handler(self.app))
        self.thread=threading.Thread(target=self.server.serve_forever,daemon=True);self.thread.start()
        self.url=f'http://127.0.0.1:{self.server.server_port}'

    def tearDown(self):
        self.gate.set();self.server.shutdown();self.server.server_close();self.thread.join()
        for _ in range(100):
            if self.app.active is None:break
            time.sleep(.01)
        self.temp.cleanup()

    def request(self,path,payload=None,authenticated=True):
        headers={'Authorization':'Bearer '+self.app.token} if authenticated else {}
        req=Request(self.url+path,data=json.dumps(payload).encode() if payload else None,headers=headers)
        return urlopen(req,timeout=5)

    def test_auth_busy_progress_and_download(self):
        with self.assertRaises(HTTPError) as error:self.request('/api/health',authenticated=False)
        self.assertEqual(error.exception.code,401)
        payload={'files':[{'name':'../scan.png','data':base64.b64encode(b'test').decode()}]}
        with self.request('/api/jobs',payload) as response:jid=json.load(response)['id']
        with self.assertRaises(HTTPError) as error:self.request('/api/jobs',payload)
        self.assertEqual(error.exception.code,409)
        self.gate.set()
        for _ in range(100):
            if self.app.get(jid)['status']=='done':break
            time.sleep(.01)
        with self.request('/download/'+jid+'/pdf') as response:self.assertEqual(response.read(),b'test-only')
        with self.assertRaises(HTTPError):self.request('/download/'+jid+'/../../../etc/passwd')
        self.assertFalse((Path(self.temp.name)/'scan.png').exists())

    def test_bad_upload_rejected(self):
        for files in [[],[{'name':'bad.exe','data':'abcd'}],[{'name':'bad.pdf','data':'not base64'}]]:
            with self.assertRaises(HTTPError) as error:self.request('/api/jobs',{'files':files})
            self.assertEqual(error.exception.code,400)


if __name__=='__main__':unittest.main()
