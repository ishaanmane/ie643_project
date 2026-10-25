import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from PIL import Image
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from layout import convert_results, stop_owned_server

class LayoutTests(unittest.TestCase):
    def test_real_surya_schema_converts_picture_and_retains_equation(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp);(d/'processed').mkdir();(d/'tags').mkdir()
            Image.new('RGB',(100,80),'white').save(d/'processed/p.jpg')
            item={'image_bbox':[0,0,100,80], 'bboxes':[
                {'bbox':[10,10,40,40],'label':'Picture','position':0},
                {'bbox':[50,10,90,40],'label':'Equation','position':1}]}
            r=d/'results.json';r.write_text(json.dumps({'p':[item]}))
            convert_results(r,d,['p'])
            tags=json.loads((d/'tags/p.json').read_text())
            self.assertEqual([b['type'] for b in tags['blocks']],['figure','equation'])
            self.assertTrue(Path(tags['blocks'][0]['crop']).exists())
            self.assertIn('0.22.1',tags['source'])
            item['image_bbox']=[0,0,200,80];r.write_text(json.dumps({'p':[item]}))
            with self.assertRaisesRegex(ValueError,'coordinate mismatch'):convert_results(r,d,['p'])
            with self.assertRaisesRegex(ValueError,'coverage'):convert_results(r,d,['missing'])

    def test_owned_server_cleanup_does_not_target_other_groups(self):
        from unittest.mock import Mock
        proc=Mock(pid=12345)
        with patch('layout.os.killpg',side_effect=[None,ProcessLookupError]) as kill:
            stop_owned_server(proc)
        self.assertEqual([c.args[0] for c in kill.call_args_list],[12345,12345])
