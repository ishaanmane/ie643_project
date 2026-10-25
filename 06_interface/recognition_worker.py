"""Short-lived GPU recognition worker; process exit releases model/CUDA memory."""
import json
from pathlib import Path
import sys
from pipeline import CleanRecognizer, validate_prediction


def main():
    request = json.loads(Path(sys.argv[1]).read_text())
    output = Path(request['output'])
    recognizer = CleanRecognizer(request['adapter'], request['max_pixels'], request['max_new_tokens'])
    predictions = []
    for i, page in enumerate(request['pages'], 1):
        print(f'Recognizing page {i}/{len(request["pages"])}', flush=True)
        text, details = recognizer.predict(Path(request['images']) / (page + '.jpg'))
        (output / 'predictions' / (page + '.md')).write_text(text)
        validate_prediction(text)
        predictions.append({'page': page, **details})
    (output / 'recognition_result.json').write_text(json.dumps(predictions, indent=2))


if __name__ == '__main__':
    main()
