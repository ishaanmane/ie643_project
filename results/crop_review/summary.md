# Hand-graded figure crops (final reconstruction, outlined PDFs)

Every figure the renderer placed, graded by a person against the caption and the source page
(`05_evaluation/crop_review.py`; grades in `val_grades.json`, `test_grades.json`).

| | figures | correct | partial crop | wrong drawing | not a drawing | right drawing (correct + partial) |
|---|---|---|---|---|---|---|
| test | 38 | 30 (78.9%) | 3 | 4 | 1 | 86.8% |
| val | 20 | 12 (60.0%) | 4 | 3 | 1 | 80.0% |
| **both** | **58** | **42 (72.4%)** | **7** | **7** | **2** | **84.5%** |

By source (val + test):

| source | figures | correct | partial | wrong | not a drawing |
|---|---|---|---|---|---|
| chalkboard (ie643) | 16 | 15 | 0 | 0 | 1 |
| digital ink (mlt) | 18 | 17 | 0 | 1 | 0 |
| notebook photos (ie802) | 24 | 10 | 7 | 6 | 1 |

Chalkboard and digital-ink figures are almost all right (32 of 34). Nearly all errors are on the
dense IE802 notebook pages, where many small sketches sit next to text: Surya splits or merges
them and position-based matching then pairs some descriptions with the neighbouring sketch.
