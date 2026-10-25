import json
from pathlib import Path
import sys
import tempfile
import time
import unittest
from unittest.mock import Mock, patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import engine


def fake_worker(answers):
    proc = Mock()
    proc.poll.return_value = None
    proc.stdout.readline.side_effect = [json.dumps(a) + '\n' for a in answers]
    return proc


class WarmModelTests(unittest.TestCase):
    def make(self, tmp):
        with patch('engine.adapter_config'), patch('engine.threading.Thread'):
            return engine.WarmModels(tmp, Path(tmp) / 'logs', idle_minutes=15)

    def test_worker_is_loaded_once_and_reused_across_uploads(self):
        with tempfile.TemporaryDirectory() as tmp:
            models = self.make(tmp)
            d = Path(tmp); (d / 'predictions').mkdir(); (d / 'processed').mkdir()
            answers = [{'ready': True}] + [{'ok': True, 'generated_tokens': 5, 'possibly_truncated': False}] * 3
            proc = fake_worker(answers)
            def write_prediction(line):
                Path(json.loads(line)['out']).write_text('Notes $x$')
            proc.stdin.write.side_effect = write_prediction
            with patch('engine.subprocess.Popen', return_value=proc) as launch:
                models.recognize(d, ['a', 'b'], d, lambda _: None)
                models.recognize(d, ['c'], d, lambda _: None)
            self.assertEqual(launch.call_count, 1)
            self.assertEqual((d / 'predictions/c.md').read_text(), 'Notes $x$')

    def test_worker_error_is_reported_not_rendered(self):
        with tempfile.TemporaryDirectory() as tmp:
            models = self.make(tmp)
            d = Path(tmp); (d / 'predictions').mkdir()
            proc = fake_worker([{'ready': True}, {'ok': False, 'error': 'OutOfMemoryError: CUDA'}])
            with patch('engine.subprocess.Popen', return_value=proc):
                with self.assertRaisesRegex(RuntimeError, 'OutOfMemoryError'):
                    models.recognize(d, ['a'], d, lambda _: None)

    def test_unloads_only_after_idle_period_and_never_while_busy(self):
        with tempfile.TemporaryDirectory() as tmp:
            models = self.make(tmp)
            models.qwen = fake_worker([]); models.surya = Mock(running=True)
            self.assertFalse(models.unload_if_idle())          # just used
            models.last_used = time.monotonic() - 16 * 60
            models.busy = True
            self.assertFalse(models.unload_if_idle())          # a job is running
            models.busy = False
            self.assertTrue(models.unload_if_idle())
            models.surya.stop.assert_called_once()
            self.assertIsNone(models.qwen)


if __name__ == '__main__':
    unittest.main()
