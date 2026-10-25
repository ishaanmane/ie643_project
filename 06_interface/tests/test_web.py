import base64
from io import BytesIO
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
import time
import unittest
from PIL import Image
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import server


def png():
    stream=BytesIO();Image.new('RGB',(40,60),'white').save(stream,format='PNG');return stream.getvalue()


class WebTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.gate=threading.Event()
        def runner(inputs,output,recognizer,**kwargs):
            self.gate.wait(3);output.mkdir();(output/'result.pdf').write_bytes(b'PDF test artifact')
            return dict(pdf='result.pdf',markdown='missing.md',bundle='missing.zip',report='missing.json',warnings=[],pages=1,elapsed_seconds=1)
        self.application=server.Application(self.temp.name,None,runner)
        self.web=server.create_app(self.application)
        self.client=self.web.test_client()
        self.headers={'Authorization':'Bearer '+self.application.operator_token}
        self.payload=dict(files=[dict(name='../scan.png',data=base64.b64encode(png()).decode())])

    def tearDown(self):
        self.gate.set()
        for _ in range(300):
            if self.application.active is None:break
            time.sleep(.01)
        self.temp.cleanup()

    def login(self,client=None,**kwargs):
        c=client or self.client
        r=c.post('/api/session',json={'token':self.application.token},**kwargs)
        self.assertEqual(r.status_code,200)
        return {'X-CSRF-Token':r.json['csrf']}

    def submit(self):
        r=self.client.post('/api/jobs',json=self.payload,headers=self.headers)
        self.assertEqual(r.status_code,202);return r.json['id']

    def complete(self,jid):
        self.gate.set()
        for _ in range(300):
            if self.application.active is None:return
            time.sleep(.01)
        self.fail('worker did not finish')

    def test_authentication_has_no_query_token_backdoor(self):
        self.assertEqual(self.client.get('/api/health').status_code,401)
        self.assertEqual(self.client.get('/api/health?token='+self.application.token).status_code,401)
        self.assertEqual(self.client.get('/api/health',headers=self.headers).status_code,200)
        self.assertEqual(self.client.post('/api/session',json={'token':'错误'}).status_code,401)

    def test_csrf_origin_host_and_secure_cookie(self):
        csrf=self.login()
        self.assertEqual(self.client.post('/api/jobs',json=self.payload).status_code,403)
        self.assertEqual(self.client.post('/api/jobs',json=self.payload,headers={**csrf,'Origin':'https://attacker.test'}).status_code,403)
        self.assertEqual(self.client.get('/',headers={'Host':'attacker.test'}).status_code,400)
        public=server.create_app(self.application,'https://notes.example.test').test_client()
        response=public.post('/api/session',base_url='https://notes.example.test',json={'token':self.application.token},headers={'Origin':'https://notes.example.test'})
        cookie=response.headers['Set-Cookie']
        for flag in ['Secure','HttpOnly','SameSite=Strict']:self.assertIn(flag,cookie)
        self.assertNotIn(self.application.token,cookie)
        self.assertIn("frame-ancestors 'none'",response.headers['Content-Security-Policy'])

    def test_browser_jobs_are_isolated_and_downloads_have_no_token(self):
        first=self.login();r=self.client.post('/api/jobs',json=self.payload,headers=first);jid=r.json['id']
        other=self.web.test_client();self.login(other)
        self.assertEqual(other.get('/api/jobs/'+jid).status_code,404)
        self.assertEqual(other.get('/api/jobs').json,{'jobs':[]})
        self.complete(jid)
        self.assertEqual(other.get('/download/'+jid+'/pdf').status_code,404)
        response=self.client.get('/download/'+jid+'/pdf');self.assertEqual(response.data,b'PDF test artifact')
        response.close()
        self.assertEqual(self.client.get('/download/'+jid+'/../../etc/passwd').status_code,404)
        self.assertEqual(self.client.delete('/api/jobs/'+jid,headers=first).status_code,200)
        self.assertFalse((Path(self.temp.name)/jid).exists())

    def test_busy_validation_and_safe_filenames(self):
        for files in [[],[{'name':'bad.exe','data':'abcd'}],[{'name':'bad.pdf','data':'not base64'}]]:
            self.assertEqual(self.client.post('/api/jobs',json={'files':files},headers=self.headers).status_code,400)
        jid=self.submit()
        self.assertEqual(self.client.post('/api/jobs',json=self.payload,headers=self.headers).status_code,409)
        self.assertEqual(self.client.delete('/api/jobs/'+jid,headers=self.headers).status_code,409)
        self.assertEqual([p.name for p in (Path(self.temp.name)/jid/'inputs').iterdir()],['001.png'])
        self.assertFalse((Path(self.temp.name)/'scan.png').exists())

    def test_multipart_order_and_server_side_total_limit(self):
        csrf=self.login()
        data={'title':'My notes','files':[(BytesIO(png()),'first.HEIC'),(BytesIO(png()),'next.png')]}
        r=self.client.post('/api/jobs',data=data,headers=csrf)
        self.assertEqual(r.status_code,202)
        folder=Path(self.temp.name)/r.json['id']/'inputs'
        self.assertEqual(sorted(p.name for p in folder.iterdir()),['001.heic','002.png'])
        self.complete(r.json['id'])
        from unittest.mock import patch
        with patch('server.MAX_UPLOAD',100):
            r=self.client.post('/api/jobs',data={'files':[(BytesIO(b'a'*60),'a.png'),(BytesIO(b'a'*60),'b.png')]},headers=csrf)
            self.assertEqual(r.status_code,413)

    def test_normal_multipart_file_larger_than_parser_buffer(self):
        csrf=self.login()
        response=self.client.post('/api/jobs',data={'files':(BytesIO(b'x'*800_000),'large.heic')},headers=csrf)
        self.assertEqual(response.status_code,202)

    def test_persistence_recovery_cleanup_and_secret_permissions(self):
        jid=self.submit();self.complete(jid)
        restored=server.Application(self.temp.name,None)
        self.assertEqual(restored.token,self.application.token)
        self.assertEqual(restored.get(jid)['status'],'done')
        restored.jobs[jid]['created']=time.time()-25*3600
        restored.cleanup();self.assertIsNone(restored.get(jid))
        self.assertEqual(os.stat(Path(self.temp.name)/'.access-token').st_mode&0o777,0o600)
        self.assertEqual(os.stat(self.temp.name).st_mode&0o777,0o700)

    def test_interrupted_job_does_not_resume_or_claim_success(self):
        jid='a'*32;folder=Path(self.temp.name)/jid;folder.mkdir()
        (folder/'status.json').write_text(json.dumps(dict(id=jid,created=time.time(),owner='owner',status='running',message='Working',result=None)))
        restored=server.Application(self.temp.name,None)
        self.assertEqual(restored.get(jid)['status'],'error');self.assertIsNone(restored.active)

    def test_shared_login_key_cannot_become_operator_or_forge_cookies(self):
        import hashlib
        self.assertEqual(self.client.get('/api/health',headers={'Authorization':'Bearer '+self.application.token}).status_code,401)
        forged_app=server.Flask('forger')
        forged_app.secret_key=hashlib.sha256(('intra-session:'+self.application.token).encode()).digest()
        serializer=forged_app.session_interface.get_signing_serializer(forged_app)
        self.client.set_cookie('intra_session',serializer.dumps({'owner':'operator','csrf':'known','_permanent':True}))
        self.assertEqual(self.client.get('/api/health').status_code,401)
        self.assertNotEqual(self.application.token,self.application.operator_token)
        self.assertNotEqual(self.application.token,self.application.signing_secret)
        restored=server.Application(self.temp.name,None)
        self.assertEqual(restored.signing_secret,self.application.signing_secret)

    def test_rate_limited_login_and_plain_text_title(self):
        for _ in range(8):self.assertEqual(self.client.post('/api/session',json={'token':'bad'}).status_code,401)
        self.assertEqual(self.client.post('/api/session',json={'token':'bad'}).status_code,429)
        self.assertEqual(self.client.post('/api/jobs',json={**self.payload,'title':r'\input{/etc/passwd}'},headers=self.headers).status_code,400)


if __name__=='__main__':unittest.main()
