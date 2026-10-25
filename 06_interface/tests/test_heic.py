from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from PIL import Image
from pillow_heif import register_heif_opener
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import pipeline
register_heif_opener(thumbnails=False)

class DecoderTests(unittest.TestCase):
    def test_actual_heic_and_heif_in_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            Image.new('RGB',(80,120),'red').save(root/'apple.HEIC',format='HEIF')
            Image.new('RGB',(120,80),'blue').save(root/'next.heif',format='HEIF')
            pages,mapping=pipeline.extract_pages([root/'apple.HEIC',root/'next.heif'],root/'pages')
            self.assertEqual([m['input'] for m in mapping],['apple.HEIC','next.heif'])
            with Image.open(root/'pages'/f'{pages[0]}.jpg') as im:
                self.assertEqual(im.size,(80,120));self.assertGreater(im.getpixel((20,20))[0],230)
            with Image.open(root/'pages'/f'{pages[1]}.jpg') as im:self.assertGreater(im.getpixel((20,20))[2],230)

    def test_phone_exif_orientation_applied_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);im=Image.new('RGB',(80,120),'green');exif=Image.Exif();exif[274]=6
            im.save(root/'phone.jpg',exif=exif)
            pages,_=pipeline.extract_pages([root/'phone.jpg'],root/'jpeg_pages')
            with Image.open(root/'jpeg_pages'/f'{pages[0]}.jpg') as decoded:self.assertEqual(decoded.size,(120,80))
            # libheif applies the container transform and resets EXIF orientation.
            # Do not apply original_orientation a second time (which would undo it).
            im.save(root/'phone.heic',format='HEIF',exif=exif)
            with Image.open(root/'phone.heic') as heic: expected=heic.size
            pages,_=pipeline.extract_pages([root/'phone.heic'],root/'heic_pages')
            with Image.open(root/'heic_pages'/f'{pages[0]}.jpg') as decoded:self.assertEqual(decoded.size,expected)

    def test_alpha_and_forged_extensions_and_oversized_images(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);Image.new('RGBA',(40,60),(0,0,0,0)).save(root/'transparent.png')
            pages,_=pipeline.extract_pages([root/'transparent.png'],root/'pages')
            with Image.open(root/'pages'/f'{pages[0]}.jpg') as im:self.assertEqual(im.getpixel((10,10)),(255,255,255))
            (root/'fake.heic').write_bytes((root/'transparent.png').read_bytes())
            with self.assertRaisesRegex(ValueError,'extension'):pipeline.extract_pages([root/'fake.heic'],root/'fake')
            with patch('pipeline.MAX_IMAGE_PIXELS',100):
                with self.assertRaisesRegex(ValueError,'megapixel'):pipeline.extract_pages([root/'transparent.png'],root/'large')

    def test_encrypted_corrupt_and_too_many_pdf_pages(self):
        import fitz
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);doc=fitz.open();doc.new_page()
            doc.save(root/'locked.pdf',encryption=fitz.PDF_ENCRYPT_AES_256,owner_pw='owner',user_pw='secret');doc.close()
            with self.assertRaisesRegex(ValueError,'Password-protected'):
                pipeline.extract_pages([root/'locked.pdf'],root/'locked')
            (root/'broken.pdf').write_bytes(b'not a PDF')
            with self.assertRaisesRegex(ValueError,'could not be opened'):
                pipeline.extract_pages([root/'broken.pdf'],root/'broken')
            doc=fitz.open()
            for _ in range(21):doc.new_page()
            doc.save(root/'long.pdf');doc.close()
            with self.assertRaisesRegex(ValueError,'20-page limit'):
                pipeline.extract_pages([root/'long.pdf'],root/'long')

    def test_dangerous_tex_commands_and_environments_rejected(self):
        pipeline.validate_prediction(r'Notes $$\begin{bmatrix}x\\y\end{bmatrix}\frac{1}{2}$$')
        for text in ['![scan][resource]\n\n[resource]: /etc/passwd', '![shortcut]\n\n[shortcut]: https://example.com/secret', r'\font\foo=/etc/passwd',r'\pdfobj file{/etc/passwd}',r'\begin{document}x\end{document}',r'\href{file:///etc/passwd}{x}',r'\csname input\endcsname{x}']:
            with self.subTest(text=text),self.assertRaises(ValueError):pipeline.validate_prediction(text)

    def test_unknown_math_command_is_a_warning_not_a_failure(self):
        warnings = pipeline.validate_prediction(r'$$\mathscr{L} = \hslash \omega$$')
        self.assertTrue(any('hslash' in w for w in warnings))

if __name__=='__main__':unittest.main()
