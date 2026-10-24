# Generation evaluation: Mac mock check

2026-10-25. Input: all annotation labels. Outlines: `--all --mock` (existing headings). Render format: Markdown. Equation checker: Tectonic. This is a pipeline smoke check; LLM outline quality and PDF compilation remain unmeasured.

- units 42, pages 410
- blocks kept 2579/2579 (100.0%)
- outlines used 42, rejected 0, none 0; sections 227 (mean 5.4 per used outline)
- titles dropped 0, repeats merged 0, outline problems 0
- equations 2739, failed to typeset 10 (0.37%)
- equation checks: tectonic
- diagrams matched to a crop 227/243
- PDFs built 0/42

| unit | pages | kept | blocks | outline | sections | titles_dropped | repeats_merged | problems | equations | eq_failed | math_check | matched | diagrams | pdf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hlcs_note01 | 1 | 8 | 8 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 1 | 1 | False |
| hlcs_note02 | 1 | 8 | 8 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 0 | 0 | False |
| hlcs_note03 | 1 | 5 | 5 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 1 | 1 | False |
| hlcs_note04 | 1 | 7 | 7 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 2 | 2 | False |
| hlcs_note05 | 1 | 7 | 7 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 1 | 1 | False |
| hlcs_note06 | 1 | 6 | 6 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 1 | 1 | False |
| hlcs_note07 | 1 | 6 | 6 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 1 | 1 | False |
| hlcs_note08 | 1 | 8 | 8 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 0 | 0 | False |
| hlcs_note09 | 1 | 6 | 6 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 1 | 1 | False |
| hlcs_note10 | 1 | 7 | 7 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 0 | 0 | False |
| hlcs_note11 | 1 | 5 | 5 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 0 | 0 | False |
| hlcs_note12 | 1 | 6 | 6 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 0 | 0 | False |
| hlcs_note13 | 1 | 8 | 8 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 1 | 1 | False |
| hlcs_note14 | 1 | 7 | 7 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 0 | 0 | False |
| hlcs_note15 | 1 | 7 | 7 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 0 | 0 | False |
| hlcs_note16 | 1 | 5 | 5 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 0 | 0 | False |
| hlcs_note17 | 1 | 6 | 6 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 0 | 0 | False |
| hlcs_note18 | 1 | 6 | 6 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 0 | 0 | False |
| hlcs_note19 | 1 | 4 | 4 | used | 1 | 0 | 0 | 0 | 0 | 0 | tectonic | 0 | 0 | False |
| hlcs_note20 | 1 | 6 | 6 | used | 2 | 0 | 0 | 0 | 0 | 0 | tectonic | 0 | 0 | False |
| ie643_lec02 | 16 | 77 | 77 | used | 23 | 0 | 0 | 0 | 64 | 0 | tectonic | 12 | 13 | False |
| ie643_lec03 | 15 | 69 | 69 | used | 11 | 0 | 0 | 0 | 85 | 0 | tectonic | 4 | 4 | False |
| ie643_lec04 | 16 | 74 | 74 | used | 3 | 0 | 0 | 0 | 102 | 0 | tectonic | 4 | 4 | False |
| ie643_lec05 | 19 | 74 | 74 | used | 4 | 0 | 0 | 0 | 110 | 0 | tectonic | 14 | 15 | False |
| ie643_lec06 | 20 | 84 | 84 | used | 5 | 0 | 0 | 0 | 90 | 0 | tectonic | 12 | 13 | False |
| ie643_lec07 | 20 | 84 | 84 | used | 9 | 0 | 0 | 0 | 83 | 0 | tectonic | 8 | 8 | False |
| ie643_lec08 | 20 | 79 | 79 | used | 9 | 0 | 0 | 0 | 100 | 0 | tectonic | 8 | 9 | False |
| ie643_lec09 | 19 | 75 | 75 | used | 5 | 0 | 0 | 0 | 76 | 0 | tectonic | 3 | 6 | False |
| ie643_lec10 | 20 | 78 | 78 | used | 12 | 0 | 0 | 0 | 101 | 0 | tectonic | 14 | 17 | False |
| ie643_lec11 | 20 | 90 | 90 | used | 6 | 0 | 0 | 0 | 109 | 0 | tectonic | 15 | 15 | False |
| ie643_lec12 | 20 | 114 | 114 | used | 8 | 0 | 0 | 0 | 150 | 0 | tectonic | 7 | 9 | False |
| ie802_notes | 56 | 622 | 622 | used | 2 | 0 | 0 | 0 | 721 | 6 | tectonic | 58 | 62 | False |
| mlt_week01 | 16 | 147 | 147 | used | 17 | 0 | 0 | 0 | 131 | 0 | tectonic | 12 | 12 | False |
| mlt_week02 | 12 | 89 | 89 | used | 8 | 0 | 0 | 0 | 113 | 0 | tectonic | 2 | 2 | False |
| mlt_week03 | 13 | 89 | 89 | used | 9 | 0 | 0 | 0 | 91 | 0 | tectonic | 4 | 4 | False |
| mlt_week04 | 19 | 133 | 133 | used | 13 | 0 | 0 | 0 | 136 | 4 | tectonic | 8 | 8 | False |
| mlt_week05 | 15 | 82 | 82 | used | 8 | 0 | 0 | 0 | 89 | 0 | tectonic | 4 | 4 | False |
| mlt_week06 | 6 | 41 | 41 | used | 4 | 0 | 0 | 0 | 38 | 0 | tectonic | 0 | 0 | False |
| mlt_week07 | 10 | 71 | 71 | used | 12 | 0 | 0 | 0 | 59 | 0 | tectonic | 7 | 7 | False |
| mlt_week08 | 13 | 97 | 97 | used | 13 | 0 | 0 | 0 | 86 | 0 | tectonic | 6 | 6 | False |
| mlt_week09 | 13 | 103 | 103 | used | 15 | 0 | 0 | 0 | 122 | 0 | tectonic | 9 | 9 | False |
| mlt_week10 | 12 | 79 | 79 | used | 10 | 0 | 0 | 0 | 83 | 0 | tectonic | 7 | 7 | False |
