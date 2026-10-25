import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import pipeline


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
        pipeline.validate_prediction('## Notes\n$$\\frac{x}{y}$$')
        for value in [r'\input{/etc/passwd}',r'\write18{something}', '![](https://example.com/a.png)', '<img src="x">', '']:
            with self.assertRaises(ValueError):pipeline.validate_prediction(value)

    def test_invalid_adapter_not_silently_base_model(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)
            (path/'adapter_config.json').write_text(json.dumps({'base_model_name_or_path':pipeline.MODEL_ID}))
            with self.assertRaisesRegex(ValueError,'weights'):
                pipeline.CleanRecognizer(path)

    def test_new_input_uses_isolated_data_and_source_appendix(self):
        events=[]
        class Recognizer:
            adapter='test-only'
            def release(self):events.append('release')
            def predict(self,path):
                events.append('recognize')
                return '# Notes\n\n$$x=1$$',{'possibly_truncated':False}
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);source=root/'photo.png';Image.new('RGB',(120,180),'white').save(source)
            def fake_render(unit,pages,md_dir,out_root,fmt,**kwargs):
                self.assertEqual(unit,'upload_notes')
                self.assertEqual(len(kwargs['source_pages']),1)
                self.assertNotEqual(Path(kwargs['data_dir']),pipeline.ROOT/'data')
                dest=Path(out_root)/unit;dest.mkdir(parents=True)
                (dest/'upload_notes.pdf').write_bytes(b'unit-test-placeholder')
                (dest/'upload_notes.md').write_text('# Notes')
                return {'pages':[], 'output':str(dest/'upload_notes.pdf'),'math':{'status':'completed','remaining_failed':0},
                        'pdf_audit':{'status':'completed','outside_words':0}}
            with patch('render_document.render_unit',side_effect=fake_render),patch('pipeline.shutil.which',return_value='/test'),patch('preprocess.NotesPreprocessor.process_with_info',return_value=(__import__('numpy').zeros((180,120,3),dtype='uint8'),{'crop':'test'})):
                result=pipeline.run_document([source],root/'job',Recognizer(),progress=lambda _:None)
                events.clear()
                def fake_layout(*args):
                    events.append('layout')
                    return {'status':'completed'}
                with patch('layout.run_layout',side_effect=fake_layout):
                    pipeline.run_document([source],root/'with_layout',Recognizer(),progress=lambda _:None,layout_mode='surya')
                self.assertEqual(events,['release','layout','recognize'])
                self.assertTrue((root/'with_layout/diagram_review.json').exists())
            self.assertEqual(result['pages'],1)
            self.assertTrue((root/'job/document_bundle.zip').exists())
            self.assertTrue((root/'job/predictions/upload_notes_page001.md').exists())
            with self.assertRaisesRegex(ValueError,'never overwritten'):
                pipeline.run_document([source],root/'job',Recognizer())


if __name__=='__main__':unittest.main()
