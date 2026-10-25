"""Regressions for observed rendering/reporting failures. No GPU required."""
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import render_document as renderer
import evaluate_generation as evaluation


class RendererTests(unittest.TestCase):
    def test_repeated_or_reordered_content_is_not_reported_as_preserved(self):
        self.assertEqual(renderer.missing_source_blocks(['same', 'same'], 'same'), ['same'])
        self.assertEqual(renderer.missing_source_blocks(['first', 'last'], 'last first'), ['last'])
        self.assertEqual(renderer.missing_source_blocks(['[Diagram: x [y]]'], r'![x \[y\]](a.png)'), [])

    def test_tall_and_wide_crops_fit_without_forcing_two_dimensions(self):
        for w, h in [(667, 134), (134, 667), (100, 100)]:
            percent = renderer.figure_width_percent((w, h))
            width = percent / 100 * (8.5 - 4 / 2.54)
            self.assertLessEqual(percent, 55)
            self.assertLessEqual(width * h / w, .30 * (11 - 4 / 2.54) + 1e-9)

    def test_missing_package_is_checker_error_not_zero_failures(self):
        response = subprocess.CompletedProcess([], 1, '', 'missing package unicode-math')
        with patch.object(renderer.shutil, 'which', return_value='/fake'), patch.object(renderer.subprocess, 'run', return_value=response):
            _, report = renderer.equation_check(['x'])
        self.assertEqual(report['status'], 'error')
        self.assertIn('missing package', report['error'])

    def test_timeout_is_reported(self):
        with patch.object(renderer.shutil, 'which', return_value='/fake'), patch.object(renderer.subprocess, 'run', side_effect=subprocess.TimeoutExpired('xelatex', 300)):
            _, report = renderer.equation_check(['x'])
        self.assertEqual(report['status'], 'error')

    def test_diagnosed_equation_removed_then_remainder_compiles(self):
        for engine in ['xelatex', 'tectonic']:
            responses = [subprocess.CompletedProcess([], 1, '', 'error: m.tex:5: undefined control sequence'),
                         subprocess.CompletedProcess([], 0, '', '')]
            with patch.object(renderer.subprocess, 'run', side_effect=responses):
                self.assertEqual(renderer.check_latex([r'\bogus', 'x'], engine), {r'\bogus'})

    def test_retry_limit_is_not_success(self):
        response = subprocess.CompletedProcess([], 1, '', 'error: m.tex:5: undefined control sequence')
        with patch.object(renderer.subprocess, 'run', return_value=response):
            with self.assertRaises(renderer.MathCheckError):
                renderer.check_latex([r'\bogus', 'x'], 'tectonic', max_rounds=1)

    def test_summary_uses_rendered_outline_and_counts_missing_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'run.json').write_text(json.dumps({'units':['a','b','c'], 'run_id':'new'}))
            report = {'unit':'a', 'run_id':'new', 'pages':[], 'missing_pages':['page1'],
                      'outline_sections':0, 'preservation':{'blocks':0,'missing':0},
                      'math':{'equations':3,'failed':0,'status':'error'}, 'output':'absent.pdf'}
            (root/'a').mkdir()
            (root/'a'/'report.json').write_text(json.dumps(report))
            (root/'c').mkdir()
            (root/'c'/'report.json').write_text(json.dumps(dict(report, unit='c', run_id='old')))
            (root/'outlines').mkdir()
            (root/'outlines'/'a.json').write_text(json.dumps({'outline':{'sections':[{'start':'p1.0'}]}}))
            output = io.StringIO()
            with patch.object(sys, 'argv', ['evaluate_generation.py','--docs',tmp,'--outlines',str(root/'outlines')]), contextlib.redirect_stdout(output):
                evaluation.main()
            text = output.getvalue()
            for expected in ['missing reports 2: b, c','missing input pages 1','outlines used 0', 'PDFs built 0/3', 'incomplete or unknown math checks 1']:
                self.assertIn(expected, text)


class OutlineRetryTests(unittest.TestCase):
    def test_retry_keeps_accepted_and_backs_up_rejected(self):
        import outline
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            accepted = '{"outline":{"sections":[{"start":"p1.0"}]}}'
            rejected = '{"outline":null,"raw_model_output":"cut off"}'
            (root/'mlt_week01.json').write_text(accepted)
            (root/'mlt_week02.json').write_text(rejected)
            blocks = [{'id':'p1.0','page':'mlt_week02_page001','type':'heading','text':'# Regression'}]
            with patch.object(sys, 'argv', ['outline.py','--all','--mock','--retry-rejected','--out',tmp]), \
                 patch.object(outline, 'all_units', return_value={'mlt_week01':[], 'mlt_week02':[]}), \
                 patch.object(outline, 'collect_blocks', return_value=blocks), contextlib.redirect_stdout(io.StringIO()):
                outline.main()
            self.assertEqual((root/'mlt_week01.json').read_text(), accepted)
            self.assertTrue(json.loads((root/'mlt_week02.json').read_text())['outline'])
            backups = list((root/'retry_backups').glob('*/mlt_week02.json'))
            self.assertEqual(len(backups),1)
            self.assertEqual(backups[0].read_text(), rejected)


if __name__ == '__main__':
    unittest.main()
