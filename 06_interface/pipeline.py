"""New-input inference using the existing clean adapter; no training or label lookup."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import subprocess
import time
import zipfile

ROOT = Path(__file__).resolve().parents[1]
for folder in ('01_preprocessing', '03_recognition', '04_reconstruction'):
    sys.path.insert(0, str(ROOT / folder))

IMAGE_TYPES = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tif', '.tiff'}
MODEL_ID = 'Qwen/Qwen2.5-VL-7B-Instruct'
DEFAULT_ADAPTER = ROOT / 'runs/final_clean/final_adapter'


def adapter_config(path):
    path = Path(path)
    config = json.loads((path / 'adapter_config.json').read_text())
    if config.get('base_model_name_or_path') != MODEL_ID:
        raise ValueError('This runner supports the trained Qwen2.5-VL-7B clean adapter only.')
    weights = list(path.glob('adapter_model*.safetensors'))
    if not weights or not all(p.stat().st_size for p in weights):
        raise ValueError('Adapter safetensors weights are missing or empty.')
    return config


class CleanRecognizer:
    def __init__(self, adapter=DEFAULT_ADAPTER, max_pixels=1_000_000, max_new_tokens=2048):
        self.adapter = Path(adapter).resolve()
        adapter_config(self.adapter)
        self.max_pixels, self.max_new_tokens = max_pixels, max_new_tokens
        self.model = self.processor = None

    def load(self):
        if self.model is not None:
            return
        import torch
        from transformers import AutoProcessor, BitsAndBytesConfig, Qwen2_5_VLForConditionalGeneration
        from peft import PeftModel
        if not torch.cuda.is_available():
            raise RuntimeError('CUDA GPU not available. Run inference on the GPU machine.')
        dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
        config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type='nf4',
                                   bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=dtype)
        # A saved processor is preferred; the base processor is compatible with training.
        processor_path = self.adapter if (self.adapter / 'preprocessor_config.json').exists() else MODEL_ID
        processor = AutoProcessor.from_pretrained(str(processor_path), min_pixels=4*28*28,
                                                  max_pixels=self.max_pixels)
        base = Qwen2_5_VLForConditionalGeneration.from_pretrained(
            MODEL_ID, quantization_config=config, torch_dtype=dtype,
            device_map={'': 0}, attn_implementation='sdpa')
        model = PeftModel.from_pretrained(base, str(self.adapter), is_trainable=False)
        model.eval()
        model.config.use_cache = True
        self.model, self.processor = model, processor

    def release(self):
        if self.model is None and self.processor is None:
            return
        import gc
        self.model = self.processor = None
        gc.collect()
        import torch
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    def predict(self, image_path):
        import torch
        from qwen_data import load_page_image, PAGE_PROMPT
        self.load()
        image = load_page_image(str(image_path), self.max_pixels)
        messages = [{'role':'user', 'content':[{'type':'image'}, {'type':'text','text':PAGE_PROMPT}]}]
        text = self.processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self.processor(text=[text], images=[[image]], return_tensors='pt').to(self.model.device)
        start = inputs['input_ids'].shape[1]
        with torch.inference_mode():
            output = self.model.generate(**inputs, max_new_tokens=self.max_new_tokens,
                                         do_sample=False, repetition_penalty=1.05, use_cache=True)
        generated = output[:, start:]
        prediction = self.processor.batch_decode(generated, skip_special_tokens=True)[0]
        count = int(generated.shape[1])
        eos = self.model.generation_config.eos_token_id
        eos = eos if isinstance(eos, list) else [eos]
        truncated = count >= self.max_new_tokens and int(generated[0, -1]) not in eos
        return prediction, {'generated_tokens':count, 'possibly_truncated':truncated}


def extract_pages(inputs, raw_dir, max_pages=20):
    """Input order is explicit; PDF/TIFF pages follow their native order."""
    from PIL import Image, ImageOps, ImageSequence
    raw_dir = Path(raw_dir)
    raw_dir.mkdir(parents=True, exist_ok=True)
    pages, manifest = [], []

    def save(image, source, source_page):
        if len(pages) >= max_pages:
            raise ValueError(f'Input exceeds the {max_pages}-page limit; split the document.')
        name = f'upload_notes_page{len(pages)+1:03d}'
        image = ImageOps.exif_transpose(image).convert('RGB')
        # Bound processing memory while retaining the uploaded originals separately.
        image.thumbnail((4000,4000), Image.Resampling.LANCZOS)
        target = raw_dir / (name+'.jpg')
        image.save(target, quality=95)
        pages.append(name)
        manifest.append({'page':name,'input':source,'input_page':source_page})

    for filename in inputs:
        path = Path(filename)
        if path.suffix.lower() == '.pdf':
            import fitz
            with fitz.open(path) as pdf:
                if pdf.needs_pass:
                    raise ValueError('Password-protected PDFs are not supported.')
                if len(pages)+pdf.page_count > max_pages:
                    raise ValueError(f'Input exceeds the {max_pages}-page limit; split the document.')
                for index, page in enumerate(pdf):
                    scale = min(2.0, 4000/max(page.rect.width,page.rect.height))
                    pix = page.get_pixmap(matrix=fitz.Matrix(scale,scale), colorspace=fitz.csRGB, alpha=False)
                    save(Image.frombytes('RGB',[pix.width,pix.height],pix.samples),path.name,index+1)
        elif path.suffix.lower() in IMAGE_TYPES:
            with Image.open(path) as image:
                for index, frame in enumerate(ImageSequence.Iterator(image)):
                    save(frame.copy(),path.name,index+1)
        else:
            raise ValueError('Supported input types: PDF, PNG, JPEG, WebP, BMP, TIFF.')
    if not pages:
        raise ValueError('No pages were found.')
    return pages, manifest


def validate_prediction(text):
    """Keep document content from issuing TeX file/command operations at rendering."""
    if not text.strip():
        raise ValueError('Model returned an empty transcription.')
    blocked = r'\\(?:input|include|includegraphics|openin|openout|read|write(?:18)?|catcode|csname|let|futurelet|expandafter|def|edef|gdef|xdef|newcommand|renewcommand|usepackage|documentclass|special|directlua|endlinechar)\b'
    if '^^' in text or re.search(blocked, text, re.I) or re.search(r'!\[.*?\]\s*\(',text,re.S):
        raise ValueError('Transcription contains a file/resource command; raw prediction saved for review.')
    if re.search(r'<\s*(?:script|iframe|img|object|embed)\b',text,re.I):
        raise ValueError('Transcription contains embedded resources; raw prediction saved for review.')


def recognize_in_worker(recognizer, data, pages, output, progress):
    request = {'adapter': str(recognizer.adapter), 'max_pixels': recognizer.max_pixels,
               'max_new_tokens': recognizer.max_new_tokens, 'pages': pages,
               'images': str(data/'processed'), 'output': str(output)}
    request_path = output/'recognition_request.json'
    request_path.write_text(json.dumps(request))
    log_path = output/'recognition.log'
    progress('Loading Qwen in isolated recognition worker')
    with log_path.open('w') as log:
        proc = subprocess.Popen([sys.executable, str(Path(__file__).with_name('recognition_worker.py')),
                                 str(request_path)], stdout=log, stderr=subprocess.STDOUT)
        try:
            deadline = time.monotonic() + 7200
            previous = ''
            while proc.poll() is None:
                if time.monotonic() >= deadline:
                    raise RuntimeError('Recognition exceeded two hours; inspect recognition.log.')
                lines = log_path.read_text(errors='replace').splitlines()
                status = next((line for line in reversed(lines) if line.startswith('Recognizing page ')), '')
                if status and status != previous:
                    progress(status); previous = status
                time.sleep(1)
            if proc.returncode:
                raise RuntimeError('Recognition worker failed; inspect recognition.log. GPU worker has exited.')
        finally:
            if proc.poll() is None:
                proc.terminate()
                try: proc.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    proc.kill(); proc.wait()
    result = json.loads((output/'recognition_result.json').read_text())
    if [p['page'] for p in result] != pages:
        raise RuntimeError('Recognition worker returned incomplete or unordered pages.')
    for page in pages:
        validate_prediction((output/'predictions'/(page+'.md')).read_text())
    return result


def run_document(inputs, output, recognizer, title='Lecture notes', max_pages=20, progress=None, layout_mode='none'):
    import cv2
    from preprocess import NotesPreprocessor
    from render_document import render_unit
    progress = progress or (lambda message: print(message, flush=True))
    output = Path(output).resolve()
    if output.exists() and any(output.iterdir()):
        raise ValueError('Output folder must be new or empty; existing runs are never overwritten.')
    output.mkdir(parents=True, exist_ok=True)
    if not shutil.which('pandoc') or not (shutil.which('xelatex') or shutil.which('tectonic')):
        raise RuntimeError('PDF generation requires pandoc and xelatex (or tectonic).')
    started = time.time()
    data = output/'data'
    (data/'processed').mkdir(parents=True)
    (data/'tags').mkdir()
    (output/'predictions').mkdir()
    originals = output/'uploads'; originals.mkdir()
    uploads=[]
    for i, filename in enumerate(inputs):
        source=Path(filename)
        target=originals/f'{i+1:03d}{source.suffix.lower()}'
        shutil.copy2(source,target)
        uploads.append({'name':source.name,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
    progress('Reading input pages')
    pages, manifest = extract_pages(inputs, data/'raw', max_pages)
    prep = NotesPreprocessor()
    preprocessing=[]
    for i,page in enumerate(pages,1):
        progress(f'Preprocessing page {i}/{len(pages)}')
        image, info = prep.process_with_info(str(data/'raw'/(page+'.jpg')))
        if not cv2.imwrite(str(data/'processed'/(page+'.jpg')),image):
            raise RuntimeError('Could not save processed page.')
        preprocessing.append({'page':page,**info})
    (output/'preprocessing.json').write_text(json.dumps(preprocessing,indent=2))
    layout_info = {'status': 'disabled'}
    if layout_mode == 'surya':
        from layout import run_layout
        recognizer.release()
        layout_info = run_layout(data, pages, output, progress)
    elif layout_mode != 'none':
        raise ValueError('Unknown layout mode')
    if isinstance(recognizer, CleanRecognizer):
        predictions = recognize_in_worker(recognizer, data, pages, output, progress)
    else:
        predictions=[]
        for i,page in enumerate(pages,1):
            progress(f'Recognizing page {i}/{len(pages)}' + (' — first run loads the trained model' if i==1 else ''))
            text, details = recognizer.predict(data/'processed'/(page+'.jpg'))
            (output/'predictions'/(page+'.md')).write_text(text)
            validate_prediction(text)
            predictions.append({'page':page,**details})
    progress('Checking equations and building searchable PDF')
    report = render_unit('upload_notes',pages,str(output/'predictions'),str(output/'documents'),
                         'pdf',data_dir=str(data),document_title=title,
                         source_pages=[data/'raw'/(p+'.jpg') for p in pages])
    warnings = ['Automatic diagram cropping is unavailable for new uploads in this mode. '
                'Original source pages are appended so diagrams remain available for checking.',
                'Recognition can misread formulas. Compilation checks do not establish mathematical correctness.']
    if layout_mode == 'surya':
        unmatched = [p['page'] for p in report['pages'] if p['descriptions_without_figure']]
        warnings[0] = 'Automatic Surya crops inserted. Generated captions and crop boundaries require review.'
        if unmatched:
            warnings.append('Diagram descriptions without crops: ' + ', '.join(unmatched))
        review = {'unmatched_pages': unmatched, 'pages': report['pages'],
                  'note': 'No guessed or manually corrected boxes were applied.'}
        (output/'diagram_review.json').write_text(json.dumps(review, indent=2))
    if any(p.get('possibly_truncated') for p in predictions):
        warnings.append('At least one prediction reached the token budget; inspect its ending.')
    if report['math']['status'] != 'completed':
        warnings.append('Equation checking did not complete; inspect the report.')
    if report['math'].get('remaining_failed'):
        warnings.append(f"{report['math']['remaining_failed']} equation snippets remain verbatim with warnings.")
    if report.get('pandoc_warnings'):
        warnings.append('The PDF compiler reported warnings; inspect report.json.')
    audit=report.get('pdf_audit',{})
    if audit.get('status') != 'completed' or audit.get('outside_words',0):
        warnings.append('PDF bounds check is unavailable, failed, or found overflow; inspect report.json.')
    inference={'model':MODEL_ID,'adapter':str(getattr(recognizer,'adapter','test backend')),
               'uploads':uploads,'page_map':manifest,'predictions':predictions,
               'elapsed_seconds':round(time.time()-started,2),'warnings':warnings,
               'layout_mode':layout_mode, 'layout':layout_info, 'report':report}
    (output/'inference.json').write_text(json.dumps(inference,indent=2))
    if not report.get('output'):
        raise RuntimeError('PDF compilation failed; see documents/upload_notes/report.json.')
    package=output/'document_bundle.zip'
    with zipfile.ZipFile(package,'w',zipfile.ZIP_DEFLATED) as archive:
        for directory in ('documents','predictions','uploads','data/tags','surya_layout'):
            for path in sorted((output/directory).rglob('*')):
                if path.is_file(): archive.write(path,path.relative_to(output))
        for name in ('inference.json','preprocessing.json'):
            archive.write(output/name,name)
        if (output/'diagram_review.json').exists():
            archive.write(output/'diagram_review.json', 'diagram_review.json')
    progress('Completed — review the PDF against the original pages')
    return {'pdf':str(Path(report['output']).relative_to(output)),
            'markdown':'documents/upload_notes/upload_notes.md',
            'bundle':'document_bundle.zip','report':'inference.json',
            'warnings':warnings,'pages':len(pages),'elapsed_seconds':inference['elapsed_seconds']}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('inputs',nargs='+',type=Path)
    parser.add_argument('--out',required=True,type=Path)
    parser.add_argument('--adapter',type=Path,default=DEFAULT_ADAPTER)
    parser.add_argument('--layout', choices=['surya','none'], default='surya')
    parser.add_argument('--title',default='Lecture notes')
    parser.add_argument('--max-pages',type=int,default=20)
    parser.add_argument('--max-new-tokens',type=int,default=2048)
    args=parser.parse_args()
    if args.max_pages<1 or args.max_new_tokens<1:
        parser.error('Limits must be positive.')
    recognizer=CleanRecognizer(args.adapter,max_new_tokens=args.max_new_tokens)
    result=run_document(args.inputs,args.out,recognizer,args.title,args.max_pages,layout_mode=args.layout)
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
