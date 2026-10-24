# Generation evaluation

Mac, Tectonic, actual clean validation predictions, page order (no outline).
Lecture 7 page010 is intentionally outside the validation split pending label verification;
all 25 available validation predictions were rendered. This is a renderer regression check.

- expected units 2, missing reports 0: none
- units 2, pages 25, missing input pages 1
- intermediate Markdown blocks retained 128/128 (100.0%)
- outlines used 0, rejected 0, none 2; sections 0 (mean 0.0 per used outline)
- titles dropped 0, repeats merged 0, outline problems 0
- unique equation snippets per unit 128, diagnosed failures 1 (0.78%)
- units with incomplete or unknown math checks 0; zero diagnosed failures does not establish correctness
- equation checks: tectonic
- diagrams matched to a crop 9/10
- PDFs built 2/2
- Text retention and syntax checks are not OCR accuracy, equation correctness, or visual PDF quality.

| unit | pages | missing_pages | kept | blocks | outline | sections | titles_dropped | repeats_merged | problems | equations | eq_failed | math_status | math_check | matched | diagrams | pdf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ie643_lec07 | 19 | 1 | 91 | 91 | none | 0 | 0 | 0 | 0 | 89 | 0 | completed | tectonic | 8 | 8 | True |
| mlt_week06 | 6 | 0 | 37 | 37 | none | 0 | 0 | 0 | 0 | 39 | 1 | completed | tectonic | 1 | 2 | True |
