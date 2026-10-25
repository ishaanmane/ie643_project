# Local rendering-fix validation — 2026-10-25

Mac Tectonic + Pandoc; GPU XeLaTeX validation pending. Thirteen regression tests pass.
Input annotation/prediction files unchanged. Plain rendering, no outline model.

| Input | Source pages | Blocks retained | Matched descriptions | Diagnosed math failures | Reviewed repairs | Remaining failures | PDF word-bound audit |
|---|---:|---:|---:|---:|---:|---:|---|
| Lecture 7 clean validation predictions | 19 | 91/91 | 8/8 | 0 | 0 | 0 | completed, 0 outside |
| MLT week 6 clean validation predictions | 6 | 37/37 | 2/2 | 1 | 1 | 0 | completed, 0 outside |
| IE802 annotations | 56 | 622/622 | 58/62 | 3 | 0 | 3 | completed, 0 outside |

Lecture 7 page010 remains excluded for uncertain labels, as before. The one extra
matched diagram is an explicitly source-reviewed mapping of the K-fold description
to Surya table b5 on MLT week6 page003. Do not report this as learned grounding
accuracy or an independent model improvement.

Reviewed MLT output pages 1–2 visually: the repaired expression is typeset, and the
K-fold row appears under its corresponding description. Original expression is
retained in report.json and source predictions remain untouched.

The previously clipped notebook expressions (old GPU PDF pages25/29) appear on
local PDF pages23/27; inspected both at full-page resolution. Their endings “weak
relaxation” and “column 1, Rank 1” are now visible inside the page. Full-document
word-bound audit finds zero outside words. This is not a complete PDF quality guarantee:
other crop defects and notebook glyph warnings remain, and some equations shrink.

Adding `cancel` removes the unsupported-command failure. Three notebook snippets
still have malformed bracket/ampersand syntax and retain visible verbatim fallback.
No blanket syntax replacement or semantic correction was applied to annotations.

A regression also corrected Tectonic's warning/error attribution: a prior overfull-box
warning must not be taken as the failing equation when a later equation errors.

Reproduction: `bash 04_reconstruction/run_render_fixes.sh --notebook`.
The script checks compilation outputs and reports bounds-check availability explicitly.
