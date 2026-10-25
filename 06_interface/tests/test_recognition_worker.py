import json
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pipeline

class WorkerTests(unittest.TestCase):
    def test_success_checks_saved_output_and_uses_separate_process(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp);(out/'predictions').mkdir()
            (out/'predictions/p.md').write_text('Notes')
            (out/'recognition_result.json').write_text(json.dumps([{'page':'p'}]))
            model=SimpleNamespace(adapter='adapter',max_pixels=100,max_new_tokens=20)
            proc=Mock(returncode=0);proc.poll.return_value=0
            with patch('pipeline.subprocess.Popen',return_value=proc) as launch:
                result=pipeline.recognize_in_worker(model,out,['p'],out,lambda _:None)
            self.assertEqual(result,[{'page':'p'}])
            self.assertTrue(launch.call_args.args[0][1].endswith('recognition_worker.py'))
            self.assertEqual(launch.call_args.args[0][0],sys.executable)
            proc.terminate.assert_not_called()

    def test_failure_does_not_proceed_to_render(self):
        with tempfile.TemporaryDirectory() as tmp:
            model=SimpleNamespace(adapter='adapter',max_pixels=100,max_new_tokens=20)
            proc=Mock(returncode=1);proc.poll.return_value=1
            with patch('pipeline.subprocess.Popen',return_value=proc):
                with self.assertRaisesRegex(RuntimeError,'worker failed'):
                    pipeline.recognize_in_worker(model,Path(tmp),['p'],Path(tmp),lambda _:None)

    def test_unused_recognizer_release_does_not_initialize_cuda(self):
        recognizer=object.__new__(pipeline.CleanRecognizer)
        recognizer.model=recognizer.processor=None
        with patch.dict(sys.modules, {'torch':None}):
            recognizer.release()
