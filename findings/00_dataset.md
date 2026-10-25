# 00 · Dataset

- **410 pages** from four sources: IE643 chalkboard frames (205), MLT digital-ink notes (129),
  IE802 notebook photos (56), HumynLabs notebook photos (20). Labels: one Markdown file per page,
  `$...$` / `$$...$$` maths, `[Diagram: ...]` for drawings.
- **Split by unit**, so near-identical neighbouring pages never cross splits: **train 303, val 31,
  test 76**. IE802 is a single notebook, so it is split by page block (1-40 train, 41-44 val,
  45-56 test); HumynLabs notes 16 (val) and 17-20 (test) are held out whole. Checked: no val/test
  page is a near-copy of a train page (highest 5-gram overlap 0.49 < 0.5).
- **Change from development:** notebook photos were only in train before, so the hardest input was
  never measured. They are now in val and test (16 test pages).
- **`??` in labels is content**: all 12 such marks were checked against the images; the lecturers
  wrote them. Only `[illegible]` now excludes a page (none remain).
- **Test labels audited** page by page against the images (AI-assisted, readings confirmed by the
  user; `data/TEST_LABEL_AUDIT.md`). Three hard spots on IE802 pages 048/049 were read from zoomed
  crops ("Egon Balas" confident; `n^2`, `\Phi` likely).
- **Limitations:** few writers per source; IE802 test pages share the writer with its train pages;
  11 labels were first drafted with Gemini, the rest by direct transcription.
