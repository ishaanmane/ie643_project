"""Optional PDF word-bounds audit using Poppler; no Python PDF package required."""
import shutil
import subprocess
import xml.etree.ElementTree as ET


def audit_pdf(path, tolerance=0.5):
    if not shutil.which('pdftotext'):
        return {'status': 'unchecked', 'reason': 'pdftotext is not installed'}
    try:
        result = subprocess.run(['pdftotext', '-bbox', str(path), '-'],
                                capture_output=True, text=True, timeout=120)
        if result.returncode:
            return {'status': 'error', 'reason': result.stderr[-1200:]}
        root = ET.fromstring(result.stdout)
        outside = []
        pages = [e for e in root.iter() if e.tag.rsplit('}', 1)[-1] == 'page']
        for number, page in enumerate(pages, 1):
            width, height = float(page.attrib['width']), float(page.attrib['height'])
            for word in page.iter():
                if word.tag.rsplit('}', 1)[-1] != 'word':
                    continue
                box = [float(word.attrib[k]) for k in ('xMin', 'yMin', 'xMax', 'yMax')]
                if box[0] < -tolerance or box[1] < -tolerance or box[2] > width+tolerance or box[3] > height+tolerance:
                    outside.append({'page': number, 'text': word.text, 'bbox': box})
        return {'status': 'completed', 'pages': len(pages), 'outside_words': len(outside),
                'examples': outside[:30], 'scope': 'word bounds only; not overlap, glyph or semantic correctness'}
    except (OSError, subprocess.TimeoutExpired, ET.ParseError, ValueError, KeyError) as e:
        return {'status': 'error', 'reason': str(e)}
