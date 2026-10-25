import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import render_document as renderer
from pdf_audit import audit_pdf

FIXES = json.loads((Path(__file__).resolve().parents[1] / 'experiments' / 'reviewed_render_fixes.json').read_text())


class ReviewedFixTests(unittest.TestCase):
    def make_input(self, root):
        page = 'mlt_week06_page003'
        for directory in ['tags', 'processed', 'md']:
            (root / directory).mkdir()
        Image.new('RGB', (1501,2000), 'white').save(root/'processed'/f'{page}.jpg')
        tags = {'image_size':[1501,2000], 'blocks':[
            {'id':'b1','order':1,'type':'table','bbox':[283,7,704,80]},
            {'id':'b5','order':5,'type':'table','bbox':[211,304,621,351]}]}
        (root/'tags'/f'{page}.json').write_text(json.dumps(tags))
        (root/'md'/f'{page}.md').write_text('[Diagram: '+FIXES['figures'][0]['description']+']\n\n$$'+FIXES['math'][0]['original']+'$$')
        return page

    def render(self, root, page, fixes):
        def checker(snippets):
            bad = {s for s in snippets if s == FIXES['math'][0]['original']}
            return bad, {'status':'completed','checked_with':'test stub','error':None}
        with patch.object(renderer, 'D', str(root)), patch.object(renderer, 'equation_check', side_effect=checker), patch.object(renderer.shutil, 'which', return_value=None):
            return renderer.render_unit('mlt_week06',[page],str(root/'md'),str(root/'out'),'md',reviewed_fixes=fixes)

    def test_reviewed_link_selects_fold_row_and_preserves_original_diagnosis(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);page=self.make_input(root)
            before=(root/'md'/f'{page}.md').read_bytes()
            report=self.render(root,page,FIXES)
            self.assertEqual(report['pages'][0]['matched'],1)
            self.assertTrue((root/'out/mlt_week06/figures'/f'{page}_b5.png').exists())
            self.assertFalse((root/'out/mlt_week06/figures'/f'{page}_b1.png').exists())
            self.assertEqual(report['math']['failed'],1)
            self.assertEqual(report['math']['remaining_failed'],0)
            self.assertEqual(len(report['math']['reviewed_repairs']),1)
            self.assertEqual(report['preservation']['missing'],0)
            self.assertEqual(before,(root/'md'/f'{page}.md').read_bytes())

    def test_without_opt_in_tables_remain_unmatched_and_math_keeps_fallback(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);page=self.make_input(root)
            report=self.render(root,page,None)
            self.assertEqual(report['pages'][0]['matched'],0)
            self.assertEqual(report['math']['remaining_failed'],1)
            self.assertEqual(report['math']['reviewed_repairs'],[])

    def test_changed_box_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);page=self.make_input(root)
            path=root/'tags'/f'{page}.json'
            tags=json.loads(path.read_text());tags['blocks'][1]['bbox'][0]=212
            path.write_text(json.dumps(tags))
            with self.assertRaisesRegex(ValueError,'changed'):
                self.render(root,page,FIXES)

    def test_tectonic_warning_is_not_mistaken_for_error(self):
        responses = [subprocess.CompletedProcess([], 1, '',
            'warning: m.tex:5: overfull box\nerror: m.tex:6: undefined control sequence'),
            subprocess.CompletedProcess([], 0, '', '')]
        with patch.object(renderer.subprocess, 'run', side_effect=responses):
            self.assertEqual(renderer.check_latex(['wide but valid', 'bad'], 'tectonic'), {'bad'})

    def test_missing_pdf_checker_is_not_success(self):
        with patch('pdf_audit.shutil.which',return_value=None):
            self.assertEqual(audit_pdf('missing.pdf')['status'],'unchecked')


if __name__ == '__main__':
    unittest.main()
