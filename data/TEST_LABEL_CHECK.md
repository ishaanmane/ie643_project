# Checking the test labels — instructions

## Why this is needed

Every page image in `data/raw_scans/` has a label: a text file in `data/annotations/` with the same name
(`ie643_lec03_page001.jpg` → `ie643_lec03_page001.md`). The label is what the page *says*, typed out in
Markdown, with maths in LaTeX and drawings described as `[Diagram: ...]`.

These labels were written by AI and have never been checked by a person.

The model is scored by comparing what it reads from the image against this label, character by character
(CER = character error rate, WER = word error rate, equation exact match). On the **test pages** that score
is the final result reported in the project. If a label is wrong, a correct model output gets counted as an
error, so the reported score is wrong too. That is why only the 76 test pages must be checked by hand.

**Goal:** after your check, each test label must contain exactly what is written on the page — no more, no less.

## Pages to check (76)

| Unit | Pages | Type |
|---|---|---|
| ie643_lec03 | 001–015 | chalkboard, many equations |
| ie643_lec09 | 001–019 | chalkboard, many equations |
| mlt_week03 | 001–013 | digital-ink notes |
| mlt_week09 | 001–013 | digital-ink notes |
| ie802_notes | 045–056 | notebook photos |
| hlcs_note17 – hlcs_note20 | 001 (one page each) | notebook photos |

Order: do the two `ie643` lectures first (most errors expected), then the 16 notebook pages, then MLT. If time runs out, write down which pages you finished.

## How to check one page

1. Open the image `data/raw_scans/<page>.jpg` and zoom in.
2. Open `data/annotations/<page>.md` side by side. Use a Markdown preview (VS Code: Cmd+Shift+V) so equations are easy to compare.
3. Go through the page **top to bottom, line by line**, and tick each line on the image against the label.
4. Fix mistakes directly in the `.md` file and save.
5. Add the page to the log at the end of this file.

## What to check and fix

### 1. Text
- Every word on the page is in the label, and nothing is in the label that is not on the page.
- Words are spelled **exactly as written**: keep the writer's abbreviations (`bckwd`, `w.r.t.`, `eqn`) and
  their spelling mistakes. Do not correct or expand anything.
- Numbers are right (`0.01` not `0.1`, `10^3` not `10^5`).
- Side notes, margin notes, arrows with words, small text in corners — all must be there.
- Struck-out text that is still readable: leave it out. `??` written on the page: keep it.

### 2. Equations (most important)
Compare symbol by symbol:
- Letters: `w` vs `\omega`, `v` vs `\nu`, `x` vs `\chi`, `e` vs `\epsilon`, `a` vs `\alpha`, `B` vs `\beta`.
- Subscripts and superscripts: `w_j` vs `w^j`, `x_i^t` vs `x_t^i`, `w^{t+1}` vs `w^t + 1`.
- Signs and relations: `+` / `-`, `=` / `\leq` / `\geq` / `<`, `\in` vs `\epsilon`.
- Sums, integrals, limits: `\sum_{i=1}^{n}` — check both the lower and upper limit.
- Brackets: every bracket opened on the page is closed in the same place.
- Marks on letters: hat `\hat{w}`, bar `\bar{x}`, star `w^*`, transpose `^T`, prime `'`, bold vectors.
- Fractions: the right thing on top and below.

If the maths means the same thing but is typed differently (`\frac{1}{2}` vs `1/2`, `\cdot` vs nothing),
**leave it** — only fix what is actually different on the page.

### 3. Order
Lines appear in the order a reader would read the page (normally top to bottom, left column before right).
If a block is clearly out of place, move it.

### 4. Diagrams
- Each drawing, graph, figure or table-like sketch on the page has **one** `[Diagram: ...]` line, at the
  place where the drawing is.
- The description says roughly what is drawn (e.g. "plot of loss vs epochs with a decreasing curve").
  Do not polish wording — it is not scored exactly. Only fix it if it describes the wrong thing,
  or if a drawing has no `[Diagram]` / a `[Diagram]` has no drawing.
- Words written inside the drawing (axis labels, node names) go inside the description.

### 5. Unreadable parts
If something on the page truly cannot be read even when zoomed in, write `[illegible]` in its place.
(Pages containing `[illegible]` are automatically left out of the scores.)

## What NOT to change

- Markdown style: `#` headings, `-` bullets, numbered lists, `**bold**`.
- Line breaks and blank lines.
- How the LaTeX is typed when it shows the same thing.
- The writer's own spelling or abbreviations.

These do not affect correctness, and changing them makes labels inconsistent with the 303 training pages.

## Examples

| Page shows | Label had | Fix |
|---|---|---|
| w<sub>j</sub><sup>t+1</sup> | `w_j^t + 1` | `w_j^{t+1}` |
| Σ from i=1 to n | `\sum_{i=0}^{n}` | `\sum_{i=1}^{n}` |
| "bckwd pass" | `backward pass` | `bckwd pass` |
| margin note "(convex!)" | missing | add `(convex!)` on its own line where it appears |
| a small sketch of a neuron | no diagram line | add `[Diagram: single neuron with inputs x1..xd, weights w1..wd, output y]` |
| ≥ | `>` | `\geq` |

## When finished

Tell Claude "test labels done". It will rebuild the splits, run `00_dataset/check_dataset.py`,
and record the check in `data/VERIFICATION.md`.

## Log (fill in as you go)

AI-assisted audit completed for all 76 requested review pages; 74 are eligible for scoring and two are excluded because their labels contain [illegible]. This is not full human verification. See [TEST_LABEL_AUDIT.md](TEST_LABEL_AUDIT.md) for confirmations, exclusions and limitations.

| Page | Status | Findings |
|---|---|---|
| ie643_lec03_page001 | AI pass | Removed headings/explanation absent from scan; restored source heading wording/case. User confirmed source-only rule. |
| ie643_lec03_page002 | AI pass | Restored x1/w1 diagram input; for→by; removed absent plain w vector; fixed h subscript tilde. |
| ie643_lec03_page003 | AI pass | Moved plain vectors into left-column reading order; compared equations. |
| ie643_lec03_page004 | AI pass | Omitted invented +1/−1 outputs, as user confirmed; preserved incomplete definition. Restored source x and vector/offset labels; split two diagram descriptions. |
| ie643_lec03_page005 | AI pass | User confirmed loop starts at 0; retained following written 2,3. Removed absent For; restored source heading/condition wording. |
| ie643_lec03_page006 | AI pass | User confirmed sign argument z. Restored missing (x,y)= on example pair. |
| ie643_lec03_page007 | AI pass | Compared formula and online-learning drawing; no substantive discrepancy. |
| ie643_lec03_page008 | AI pass | Fixed fluctuations→fluctuation and heading case; retained literal ??. |
| ie643_lec03_page009 | AI pass | Compared definition and both inequalities; no substantive discrepancy. |
| ie643_lec03_page010 | AI pass | Restored missing “are there”; compared formula, graph and annotations. |
| ie643_lec03_page011 | AI pass | Compared separability definition and three inequalities; no substantive discrepancy. |
| ie643_lec03_page012 | AI pass | Compared all prose and M bounds; no substantive discrepancy. |
| ie643_lec03_page013 | AI pass | Removed absent “How do”; compared before/after annotations and dot-product chain. |
| ie643_lec03_page014 | AI pass | Compared linearity identity and two margin inequalities; no substantive discrepancy. |
| ie643_lec03_page015 | AI pass | Fixed summation upper limit 1→T; retained written ??. |
| ie643_lec09_page001 | AI pass | Compared announcement text, date and time; no substantive discrepancy. |
| ie643_lec09_page002 | AI pass | Restored final phi prime and l+1 in w_mi annotation; placed a_j annotation under its derivative. Preserved source final weight superscript l. |
| ie643_lec09_page003 | AI pass | Compared matrix factors/indices; restored standalone l annotation below left vector. |
| ie643_lec09_page004 | AI pass | Removed added comparison prose and subset relation; moved R^d annotation to the source pair. |
| ie643_lec09_page005 | AI pass | Removed invented vector name/equality preceding component vector. |
| ie643_lec09_page006 | AI pass | Compared one-hot vector, k-th component and loss annotations; no substantive discrepancy. |
| ie643_lec09_page007 | AI pass | Restored source distrn. abbreviation; compared probability vector and constraints. |
| ie643_lec09_page008 | AI pass | Restored distrns abbreviation; compared KL formula and divergence names. |
| ie643_lec09_page009 | AI pass | User confirmed retaining reverse-KL expansion and clipped +ve; removed absent not-equal commentary, joined KL expression and restored +ve. |
| ie643_lec09_page010 | AI pass | Restored missing x^i in R^d annotation. |
| ie643_lec09_page011 | AI pass | Restored Bernoulli r.v in diagram caption; compared both optimization sums. |
| ie643_lec09_page012 | AI pass | Restored initial min; compared KL expansion and CE objective. |
| ie643_lec09_page013 | AI pass | Removed false claim that normalization fraction is crossed out; compared softmax indices. |
| ie643_lec09_page014 | AI pass | Removed absent l−1 diagram label; compared architecture, equation and literal ??. |
| ie643_lec09_page015 | AI pass | Corrected derivative subscript o→j after enlarged inspection; compared remaining derivatives. |
| ie643_lec09_page016 | AI pass | Moved left-column loss before right-column derivative chain. |
| ie643_lec09_page017 | AI pass | Compared softmax derivative cases and expansion; no substantive discrepancy. |
| ie643_lec09_page018 | AI pass | Fixed second sum range k≠j to k=1…C. Preserved written ??. |
| ie643_lec09_page019 | AI pass | Removed absent summary equation and explanatory sentence. |
| ie802_notes_page045 | AI pass | User confirmed y_i≥0 and second perspective denominator λ²; applied denominator correction. Remaining prose/formulas compared. |
| ie802_notes_page046 | AI pass | Compared four drawings and inequalities; user confirmed hand lines and chopp. Applied source spelling chopp. |
| ie802_notes_page047 | AI pass | Added missing fifth drawing; set→get; user confirmed x₁/x₂ in circle inequality, corrected m₁/m₂. |
| ie802_notes_page048 | Excluded: illegible | Applied confirmed Q′/b₁; corrected if→it and error prone. Neither reviewer nor user could read bracketed note after feasible red; marked [illegible]. |
| ie802_notes_page049 | Excluded: illegible | Removed invented i≠j. User could not confidently identify text after introduce or convex-hull reference symbol; marked both [illegible], without guessing lambda. |
| ie802_notes_page050 | AI pass | Compared model/taxonomy; user confirmed k/a, replacing kla. |
| ie802_notes_page051 | AI pass | Fixed 0 and 1→0 or 1; compared both algorithms, vector and cardinality condition. |
| ie802_notes_page052 | AI pass | Added missing x3–x4 graph edge; compared quadratic coefficients, trial values and prose. |
| ie802_notes_page053 | AI pass | Restored “not work then” and missing fifth entry 1 in final six-element vector; compared rounding expressions and constraints. |
| ie802_notes_page054 | AI pass | Added subscript i in first rounding argument; moved continuous annotation to NLP relaxation; preserved absent bar in second written argument. |
| ie802_notes_page055 | AI pass | Omitted struck-out cᵀy, retained min/constraints; corrected source lowercase a in surrogate objective. |
| ie802_notes_page056 | AI pass | Removed struck-out Bonmin; restored NO and SOCs ?. User confirmed Quesada, Local B and CG; corrected latter two labels. |
| hlcs_note17_page001 | AI pass | Added handwritten V.V.I and Kailash Joshi; restored source case. Retained Sort int misspelling; omitted branding per user. |
| hlcs_note18_page001 | AI pass | Added handwritten name; restored source case including user-confirmed uppercase Y in declaration and Cout line; omitted branding. |
| hlcs_note19_page001 | AI pass | Restored Using and Cout; compared literals, cast and return; omitted branding per user. |
| hlcs_note20_page001 | AI pass | Added Kailash Joshi; restored Class and annotation case; removed invented ClassName = wording from comment; omitted branding. |
| mlt_week03_page001 | AI pass | Moved split denominator and z_i=k explanation to actual page 002, per user. Preserved visible n fragment on page 001 and source n^k claim. |
| mlt_week03_page002 | AI pass | Restored visible denominator fragment and explanation from scan; compared example, objective and source n^k. |
| mlt_week03_page003 | AI pass | Compared algorithm, assignments, means and convergence prose; no substantive discrepancy. |
| mlt_week03_page004 | AI pass | Removed invented globally from “optimal”. |
| mlt_week03_page005 | AI pass | Compared mean-minimization proof and assignments; no substantive discrepancy. |
| mlt_week03_page006 | AI pass | Removed false RHS equality to F; placed source F annotation under LHS; restored algorithm’s and removed invented LHS wording. |
| mlt_week03_page007 | AI pass | Corrected swapped diagram line labels. User confirmed retaining algebraically cancelled norm terms. |
| mlt_week03_page008 | AI pass | Replaced invented continuation/others wording with actual sentence about least distance. |
| mlt_week03_page009 | AI pass | Compared k-means++ sampling expression and prose; no substantive discrepancy. |
| mlt_week03_page010 | AI pass | Added two missing plots and table markers; removed crossed-out headers, kept S(x). Retained source 53 total versus 55 denominators. |
| mlt_week03_page011 | AI pass | Added missing partially blank table and table markers; corrected misleading centroid description; restored mean labels on the three written centers. |
| mlt_week03_page012 | AI pass | Compared model-selection prose and formulas; no substantive discrepancy. |
| mlt_week03_page013 | AI pass | Compared AIC/BIC expressions and drawing; retained source wording. |
| mlt_week09_page001 | AI pass | Separated two drawings; included red outlier; preserved h_w(w) and incomplete set brace exactly as written. |
| mlt_week09_page002 | AI pass | Restored repeated clipped input from adjacent page under user’s recovery rule; compared update condition and vector. |
| mlt_week09_page003 | AI pass | Fixed 1/y misread to annotation y under (1); restored both case equations/annotations; split plots and corrected circled green point. |
| mlt_week09_page004 | AI pass | Restored missing initial plot; >→≥; fixed both displayed weight vectors in final drawing. |
| mlt_week09_page005 | AI pass | Restored w-star in margin assumption; compared three updates and source non-convergence claim. |
| mlt_week09_page006 | AI pass | Corrected w-prime diagram description: collinear normalized vector, not rotated w1; compared normalization equations. |
| mlt_week09_page007 | AI pass | Restored y²=+1 annotation; preserved written mistake-count bounds, including source off-by-one inconsistency. |
| mlt_week09_page008 | AI pass | Compared Cauchy-Schwartz derivation, projection drawing and bounds; no substantive discrepancy. |
| mlt_week09_page009 | AI pass | Restored l→no. of mistakes annotation; compared radius-margin bound. |
| mlt_week09_page010 | AI pass | Compared probability model, level-set diagram and score explanation; no substantive discrepancy. |
| mlt_week09_page011 | AI pass | Compared link-function statements and sigmoid plot. Preserved source g(0)=0 and −1 limit despite inconsistency with sigmoid. |
| mlt_week09_page012 | AI pass | Compared likelihood, logs and derivative. Preserved source missing derivative summation. |
| mlt_week09_page013 | AI pass | Restored missing gradient symbol; recovered clipped exponential numerator from page 012 with user authorization; moved Θ annotation to residual y−g. |
