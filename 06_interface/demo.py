"""Local transport/decoder test. Never represents model recognition."""
import json
from pathlib import Path
import time
import zipfile
from pipeline import extract_pages


def run_demo(inputs, output, recognizer=None, title='Lecture notes', max_pages=20, progress=print):
    import fitz
    import cv2
    from preprocess import NotesPreprocessor
    started = time.time()
    output = Path(output)
    output.mkdir(parents=True)
    progress('Checking image formats and page order')
    pages, mapping = extract_pages(inputs, output / 'pages', max_pages)
    pdf = fitz.open()
    prep = NotesPreprocessor()
    records = []
    for i, name in enumerate(pages, 1):
        progress(f'Preprocessing page {i}/{len(pages)} — interface test, no model')
        source = output / 'pages' / (name + '.jpg')
        image, info = prep.process_with_info(str(source))
        cv2.imwrite(str(output / 'pages' / (name + '_processed.jpg')), image)
        records.append(info)
        page = pdf.new_page(width=595, height=842)
        page.insert_text((36, 30), 'INTERFACE TEST ONLY - NO OCR OR LAYOUT MODEL', fontsize=11, color=(.65, .15, .1))
        page.insert_text((36, 50), f'Source page {i} - upload decoding and preprocessing verified', fontsize=10)
        page.insert_image(fitz.Rect(36, 68, 559, 806), filename=str(source), keep_proportion=True)
    pdf.save(output / 'interface_test.pdf')
    pdf.close()
    warnings = ['INTERFACE TEST ONLY. This PDF contains source previews; no model recognition or diagram detection ran.']
    (output / 'interface_test.md').write_text('# Interface test only\n\nNo OCR or layout model ran.\n')
    report = dict(mode='interface_test_only', pages=len(pages), page_map=mapping, preprocessing=records,
                  warnings=warnings, elapsed_seconds=round(time.time() - started, 2))
    (output / 'inference.json').write_text(json.dumps(report, indent=2))
    with zipfile.ZipFile(output / 'document_bundle.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in output.rglob('*'):
            if path.is_file() and path.suffix != '.zip':
                archive.write(path, path.relative_to(output))
    return dict(pdf='interface_test.pdf', markdown='interface_test.md', bundle='document_bundle.zip',
                report='inference.json', pages=len(pages), warnings=warnings, elapsed_seconds=report['elapsed_seconds'])
