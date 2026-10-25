# 01 · Dataset

## What it contains

| Prefix | Source | Medium | Pages | Image size |
|---|---|---|---|---|
| `ie643_lecNN_pageNNN` | IE643 class scribes, lectures 2-12 | chalkboard frames | 205 | 7168x4320 (189 pages); 2044x1228 for lecture 2 (16 pages, blocky) |
| `mlt_weekNN_pageNNN` | MLT notes, weeks 1-10 | digital stylus, multi-colour | 129 | about 2448x3170 |
| `ie802_notes_pageNNN` | IE802 notebook | notebook photos and scans | 56 | 1786x2526 (7 pages landscape scans) |
| `hlcs_noteNN_page001` | HumynLabs CS notes (Hugging Face) | notebook photos | 20 | 2380x3368 |

Each page has a Markdown label in `data/annotations/<page>.md`: LaTeX for math (`$...$` inline, `$$...$$` display), headings and lists kept, figures described as `[Diagram: ...]` (195 of 410 pages contain one). Median label 520 characters, longest 1,701 (942 tokens).

## How the labels were made

| Method | Pages |
|---|---|
| Gemini API (stopped by the free tier's 20 requests/day) | 11 |
| Direct AI transcription of each page | 399 |

All labels are AI-written and **not yet human-verified**. 12 pages contain `??` where the reading was uncertain; 2 pages are genuinely blank.

## Splits

Split **by unit** (lecture or week), never by random page: consecutive pages repeat the same equations, so a random split would leak near-duplicates into test.

| Split | Units held out | Pages | By source |
|---|---|---|---|
| train | all other units | 318 | chalkboard 146, digital 97, IE802 55, HumynLabs 20 |
| val | `lec07`, `week06` | 25 | chalkboard 19, digital 6 |
| test | `lec03`, `lec09`, `week03`, `week09` | 55 | chalkboard 29, digital 26 |
| held back | pages still containing `??` | 12 | 6 would be train, 5 test, 1 val |

Built by `00_dataset/build_dataset.py`; checked by `00_dataset/check_dataset.py` (current state: 0 FAIL, 4 WARN, all warnings known).

## Leakage checks

- No page in two splits; no lecture or week spread over two splits.
- 5-gram text similarity of every val/test page against every train page: highest 0.49 (test, `lec09_page003` vs `lec08_page010`) and 0.47 (val, `lec07_page018` vs `lec08_page007`). Lecture 08 re-derives backpropagation equations also used in lectures 07 and 09: same equations, different handwriting. 2 of 24 val and 3 of 55 test pages fall between 0.4 and 0.49.
- The four val pages the fine-tuned model read almost perfectly have similarity 0.08, 0.15, 0.33 and 0.39 to their closest train page, so those scores are mostly genuine reading.

## Fixes made during the session

| Problem | Fix |
|---|---|
| The builder listed pages from `data/processed/` (gitignored), so a fresh clone would have written empty training files | Lists from `data/raw_scans/` |
| `??` pages were used as training targets and test references | Left out of every split until fixed |
| The prompt said "LaTeX ($$...$$) for **all** math" while 336 labels also use inline `$...$` | Prompt now matches the labels: inline, display, and `[Diagram: ...]` |
| The scorer compared against the label copy inside the JSONL, which goes stale after a correction | Reads `data/annotations/` |

## Variants built from the same splits

| Variant | Image | Prompt extra | Files |
|---|---|---|---|
| clean | `data/processed/` | none | `data/{train,val,test}.jsonl` |
| boxed | `data/processed_boxed/` (Surya boxes drawn) | "boxes are hints" | `data/boxed/*.jsonl` |
| boxed_json | `data/processed_boxed/` | the page's layout tags as JSON | built in `03_recognition/qwen_data.py` |

## Known gaps

1. **No notebook-photo pages in val or test**: that medium is trained on but never measured.
2. Labels unverified; the 12 `??` pages are out of the splits.
3. Low writer diversity: each source is mostly one person's handwriting.
4. Lecture 2 is low resolution and gives the worst layout results.
5. Region-level tags (boxes, order) exist for all pages only as unchecked Surya drafts.
