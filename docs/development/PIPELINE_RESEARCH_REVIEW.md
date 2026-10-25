# Pipeline research review and submission-day decisions

Research and code audit: 2026-10-25. Constraint supplied by the user: submission is
today; the existing QLoRA training run takes about one hour on the 16 GB GPU.

## Decision

Keep the working clean Qwen2.5-VL-7B adapter. Treat the second, text-only outline
pass as an optional experiment until it beats preservation of existing headings.
Use Surya as fallible spatial evidence alongside full-page transcription. Fix
known renderer defects and audit the evaluation before spending another training
hour. There is no evidence that the present model is globally best, or that a
new structure model is necessary for this dataset.

This is a research recommendation, not the result of running alternative models
on our GPU. No new model training or combined Surya/Qwen inference was performed
for this review. The existing all-unit outline job can finish unchanged.

## 1. What each task means

| Task | Question | Example | Current implementation |
|---|---|---|---|
| Region detection | Where is content? | A rectangle around a drawing | Surya boxes |
| Layout classification/order | What kind of region is it, and what follows it? | Heading, equation, table; reading order | Surya tags/order |
| Recognition | What does the region/page say? | Characters, mathematical symbols, Markdown | Clean Qwen adapter |
| Logical structure recovery | How are elements related? | A paragraph belongs to a heading; a label belongs to a figure; a derivation continues on the next page | Partly represented in Markdown; relationships largely missing |
| Editorial organisation | Would another section title/grouping help a reader? | Propose a new topic heading spanning three pages | Current outline LLM partly does this |
| Rendering | How should verified content be typeset? | Figure sizing, line wrapping, page breaks | Python, Pandoc, LaTeX |

These capabilities may share one model; they do not require six separate trained
networks. Layout detection already includes some structural understanding.
Finding a heading box does not establish its parent heading across pages or which
figure an adjacent annotation explains.

The official project statement asks to preserve original content and logical
structure. Inventing an improved pedagogical outline is optional. A faithful
reflow with existing headings is a valid technical baseline. The course statement
uses “develop/finetune a model” for deliverables 3 and 4; it does not explicitly
say that each deliverable needs a different checkpoint. Do not promise the TA's
interpretation. Describe the trained structured-output recognizer, pretrained
layout model, optional zero-shot organiser and deterministic renderer honestly.

Research separates page extraction from hierarchy and cross-page relationships.
MPDocBench-Parse evaluates text, figures, reading order, continuation and heading
trees separately; its findings show that correct heading detection does not
guarantee a correct document hierarchy. This supports evaluating relationships
rather than treating the number of headings as accuracy. [MPDocBench-Parse](https://arxiv.org/abs/2605.22100)

## 2. What the current all-unit job establishes

It runs base Qwen on annotation text and produces outline JSON for 42 units. It
does not train a model, rerun handwriting recognition, use the clean adapter,
or supply Surya layout evidence to the outline prompt.

It tests coverage, malformed/truncated JSON, rejected outlines, large inputs,
and whether downstream rendering works across the dataset. Labels isolate
reconstruction from recognition errors, though these AI labels are not verified
ground truth. The run includes training, validation, test and uncertain pages;
it is an engineering coverage check, not an unbiased held-out accuracy score.

The all-unit run is useful but not mandatory before trying a renderer fix. A
smaller A/B comparison would have been sufficient for initial model selection.
Let the already-running job finish and keep its outputs. Do not treat it as a
reason to delay the submission's working demonstration.

For model selection, hold transcript and renderer constant and compare:

| Variant | Inputs/behaviour | Measures |
|---|---|---|
| A | Existing Markdown headings; no second model | Whether an organiser is needed |
| B | Current base-Qwen text-only outline | Added value of topic organisation |
| C | Same organiser plus reliably aligned Surya evidence | Added value of spatial grounding |
| D, later | C plus source-crop rereads | Added value of recognition repair |

Use validation units for selecting changes. Existing all-unit outputs can be
used for failure diagnosis, but do not use repeated test-based tuning and then
describe those test results as untouched.

## 3. What we already know about using Surya as input

The recognition experiment already compared these two trained configurations:

| Configuration | CER | Text-only CER | Existing equation-match score |
|---|---:|---:|---:|
| Clean image | 0.277 | 0.222 | 0.244 |
| Boxes drawn on image + layout JSON + boxed prompt | 0.287 | 0.258 | 0.273 |

Source: `findings/04_recognition_finetuning.md`, corroborated by training logs.
The same-condition clean zero-shot CER was **0.776**, falling to **0.277** after
fine-tuning. The 0.712 baseline belongs to the boxed configuration and should not
be presented as the clean configuration's starting score.

Clean extraction retained more side notes in the inspected pages. However,
boxes, JSON, prompt and learned adapter all changed between configurations.
The evidence supports choosing clean as the current practical extraction model;
it does not isolate drawn boxes as the only cause, establish statistical
significance, or show that all layout conditioning is harmful. Equation matching
also favoured the boxed configuration under the current limited metric.

Adding layout at reconstruction time is a different experiment. Keep the
full-page transcript, then use layout to identify relationships and suspicious
regions. Never delete text just because Surya missed a box.

## 4. How to combine the models properly

### 4.1 Establish a shared representation

Each content block should have an immutable id, page id, original text, recognized
type, candidate source regions, association status, and any approved presentation
relationships. Retain raw model output and source image references separately
from rendered text. A box may correspond to several text blocks, and one text
block may span several boxes.

Our audit found **4,283 Surya blocks and zero populated `text_preview` fields**.
The stored files contain layout, not an independent OCR transcript. Examples:

- Lecture 7 source page 17: six Markdown blocks, one whole-page Surya figure.
- Lecture 7 source page 18: three Markdown blocks, five Surya regions.
- Week 6 source page 3: eight Markdown blocks and eight Surya regions, but the
  lists still contain different semantic units, including a footer and tables.

Equal counts do not imply alignment. Do not attach a box to the nth Markdown
block solely because both occupy position n.

Docling's document representation is a useful design reference: it separates
content items from hierarchy and retains provenance. We can adopt that idea
without replacing our renderer or installing Docling today. [Docling document model](https://docling-project.github.io/docling/concepts/docling_document/)

### 4.2 Obtain evidence for alignment

Surya's OCR mode can provide recognized blocks with spatial information, unlike
our saved layout-only run. Align its text to Qwen's text with similarity, order
and compatible region types, allowing unmatched and many-to-many cases. A
targeted crop read is another option for difficult headings or annotations.
[Surya documentation](https://github.com/datalab-to/surya)

Treat agreement as evidence, not proof: models can share an error. Disagreement
should trigger source inspection or mark uncertainty, not automatically replace
the clean transcript. A crop read also changes the recognizer's input distribution;
use full-page context where needed and evaluate that change.

MinerU2.5's global-layout/local-recognition design is relevant evidence that
layout-guided high-resolution crops are a productive architecture. Its benchmark
results do not establish performance on our particular chalkboard handwriting.
[MinerU2.5](https://arxiv.org/abs/2509.22186)

### 4.3 Constrain reconstruction decisions

The organiser should propose source-backed relations such as `section_parent`,
`caption_of`, `label_of` and `continues`. It should refer to existing ids, preserve
mathematical text, and abstain when alignment is uncertain. Generated editorial
titles must be distinguishable from headings actually present in the source.
Use complete heading/caption text and enough neighbouring context instead of
silently truncating every block to 90 characters.

For submission day, implement the well-understood deterministic improvements
first. A full relation model is a larger change and needs its own labels/checks.

## 5. Model choices: evidence and limits

No external leaderboard can identify the best model for our handwritten notes.
Different releases, benchmark versions, language mixes and rendering/evaluation
settings are not directly comparable. The following are candidates to test, not
models whose superiority on this project has been established.

| Candidate | Relevant capability | Project-specific judgment |
|---|---|---|
| Existing clean Qwen2.5-VL-7B adapter | Already trained on our handwriting and verified to run on the GPU | Keep as submission recognizer and baseline. It already learns Markdown structure. |
| Existing base Qwen2.5-VL-7B outline pass | No new download; structured section proposals | Keep optional. Train-time recognition skill does not establish outline quality. |
| Surya OCR + layout | Region types, positions, order and OCR | Closest incremental source of spatial evidence; assess handwritten OCR and preserve unmatched content. [Official repository](https://github.com/datalab-to/surya) |
| PaddleOCR-VL-1.6, 0.9B family | Compact document parsing; training targets weak regions and supervision quality | Sensible future OCR/parser comparison; not a lecture-wide organiser by itself. Its published benchmark score is not handwriting accuracy on our pages. [Model card](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6), [report](https://arxiv.org/abs/2606.03264) |
| MinerU2.5, 1.2B | Global layout followed by native-resolution crop recognition | Strong architectural comparison for our figure/math problems; migration and domain testing required. [Paper](https://arxiv.org/abs/2509.22186) |
| LightOnOCR-3, 0.8B/1B/4B variants | Grounding mode returns block labels, boxes and recognized content | Could reduce text-to-box alignment work; handwriting and diagram-boundary accuracy still need measurement. Earlier LightOnOCR-2-1B is a smaller established comparison, not the latest family. [Current model card](https://huggingface.co/lightonai/LightOnOCR-3-4B), [earlier model](https://huggingface.co/lightonai/LightOnOCR-2-1B) |
| Qwen3-VL-4B/8B or Qwen3.5-4B | General multimodal document/grounding capabilities | Alternatives for a controlled later bake-off. They require compatible loaders and inference settings; our current outline script hardcodes the Qwen2.5-VL class, so changing `--model` alone is insufficient. [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL), [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) |
| olmOCR 2, 7B | Document-specialized Qwen-derived OCR; training rewards test content and ordering | Useful evaluation/training ideas. Published focus is digitized print documents; do not infer handwritten superiority. [Paper](https://arxiv.org/abs/2510.19817) |
| LayoutLMv3 or a smaller relation classifier | Text/image/layout features for classification | Requires aligned OCR and task-specific supervision; not an off-the-shelf PDF rebuilder. [Paper](https://arxiv.org/abs/2204.08387) |

On 16 GB, parameter count alone does not establish feasibility. Vision tokens,
activation/KV memory, quantization support and serving allocations matter. The
existing 7B QLoRA run's measured peak is 13.2 GB. Run candidate models sequentially
and keep experiment environments separate from the working environment. No new
candidate's VRAM consumption was measured in this audit.

## 6. Should we train a separate structure model?

**Not from scratch, and not as the next step today.** One hour of optimization
does not supply missing supervision. Our 410 pages provide only 42 units, with
36 represented in training, 2 in validation and 4 in test. Twenty units are
single-page HumynLabs notes. There are no human-checked document hierarchy or
caption/label relationship targets, and the Surya boxes are unverified drafts.

Training a model to reproduce its own proposed headings would be distillation,
not independent evidence of correctness. It can copy teacher mistakes. Training
on all 42 units would also erase the existing unit-held-out comparison.

If relationship errors remain after alignment and rendering are correct, train a
small pretrained classifier or LoRA adapter with bounded outputs: block type,
heading level, parent id, caption/figure link or continuation link. Construct
human-corrected examples from training units, hold out whole units/writers,
compare against rules and the zero-shot model, and track a learning curve.
There is no justified universal minimum sample count for this task.

For equation recognition, a separate narrow model or adapter is more motivated
by the current errors than a free-form document rewriter. Uni-MuMER shows that
task-specific adaptation can improve handwritten math; it uses Qwen2.5-VL-3B
and structured spatial/error/counting tasks. Its full-parameter, multi-GPU recipe
is not equivalent to our one-hour QLoRA run. MathWriting offers equation-focused
data, but isolated digital ink differs from chalkboard photos. Those are later
experiments after source labels and evaluation are corrected.
[Uni-MuMER](https://arxiv.org/abs/2505.23566), [MathWriting](https://github.com/google-research/google-research/blob/master/mathwriting/README.md)

A further training epoch today is defensible only if a specific training-data
error or measured validation trend motivates it, sufficient validation/package
time remains, and the current adapter is retained. It is not automatically more
valuable than repairing a known content or rendering defect. Do not revise the
test split and describe previously trained-on notebook pages as unseen.

## 7. Ambiguities and weaknesses verified in our implementation

| Area | Finding | Consequence/action |
|---|---|---|
| Title grounding | Title words are checked against five-character word prefixes from the whole unit. | A title may pass without being supported at that section. Prefer existing local headings; membership is not semantic verification. |
| Outline granularity | Prompt asks for at least two sections even for a tiny one-topic note. | Allow a single section or no added section. More sections are not inherently better. |
| Input context | Every block preview is capped at 90 characters. | Topic/relationship information can disappear. Keep full headings and relevant neighbourhoods. |
| Large units | IE802 has 622 blocks and a 54,006-character prompt, requesting up to 103 sections, but the output cap is 1,536 tokens. | Truncation is a risk, not a confirmed outcome of the running job. Record finish reason and use bounded/chunked proposals if needed. |
| Validator | Invalid levels are coerced to 2; first-section coverage is reported rather than enforced. | Update documentation and distinguish valid-with-repairs from strict compliance. |
| Figure geometry | All PDF images were stretched to the same width/height. | Fix aspect ratio; no model training is needed. See `RECONSTRUCTION_REVIEW.md`. |
| Figure candidates | Only `figure` regions enter matching; the missing K-fold diagram is labelled `table`. | Add evidence-based fallback candidates; do not globally relabel tables. |
| Crop completeness | Whole-page/mixed boxes and cut labels occur. Merging is driven partly by description counts. | A missing description can induce a bad merge. Validate geometry/content and record uncertain crops. |
| Tiny drawings | Extra unmatched figures under 3% page area are omitted. | Important small diagrams may be lost despite all Markdown blocks being retained. Measure visual coverage separately. |
| Image provenance | The converter checks dimensions, but renderer ignores the returned tag image size. | Validate the actual input/tag pairing; preserve preprocessing metadata and transforms. Equal dimensions alone do not prove the same crop. |
| Preservation | Current metric checks whether each source string occurs somewhere in the pre-neutralization Markdown. | Does not prove occurrence count, order, diagram correctness or final-PDF content. |
| Math checks | Compiler infrastructure errors can be mistaken for no failing equations. Checks happen separately from PDF compilation. | Track pass/fail/unchecked/checker-error separately; a timeout or missing package is not a math pass. |
| Equation correctness | The incorrect Ridge annotation compiles. | Syntax validity is independent of source fidelity. Do not auto-correct mathematical meaning from context. |
| Generation coverage | Summary totals only available reports and does not aggregate missing source pages. | Require an expected-unit/page manifest; otherwise an incomplete run can look successful. |
| Outline usage | Evaluator infers use from the external outline JSON, not definitive renderer provenance. | Save outline identity/hash and actually applied sections in each render report. |
| Recognition CER/WER | Scores are page-macro averages capped at 1.0; missing predictions are excluded from the average. | Report exact definition and coverage; add uncapped corpus edit rates or a clearly defined failure-inclusive measure. |
| Equation metric | Reference display equations are looked up in a set of predicted equations. | It is recall-like; extra equations and duplicate omissions are not penalized. It excludes inline math. |
| References | Evaluation reads current annotation files, which can differ from those used in older scores. | Pin dataset/reference revisions in run manifests. |
| Labels/splits | AI references unverified; validation has only two units; no notebook photos in validation/test. | Source-check references, report by domain and limit generalization claims. New notebook test pages must be genuinely unseen. |
| Dataset interpretation | All-unit generation uses all annotation files, including the 12 `??` pages excluded from recognition splits. | State the input manifest and purpose; do not equate the 410-page run with held-out recognition evaluation. |
| Documentation | Main README, pipeline document and recognition README still contain obsolete counts/status. | Synchronize submission-facing docs with measured findings and working entry points. |
| Deliverable readiness | No end-to-end upload interface or `pipeline.py` was found in the audited repository inventory. | A runnable new-input demonstration is a submission priority, independent of another model's score. |

Small diagnostic counterexamples were executed: the current equation metric gave
1.0 when one repeated reference equation was omitted and an extra wrong equation
was added; the current containment criterion accepted both a missing duplicate
block and reversed blocks. These are metric limitations, not claims that the
actual render run necessarily had those failures.

Several earlier prose claims need narrowing: declining validation loss does not
prove absence of overfitting; one clean-vs-boxed run does not establish a measured
run-to-run variance; the external-dataset plan's attribution of Uni-MuMER to only
page/equation prompt mixing omits its actual auxiliary tasks. Keep historical
results, but describe their evidence accurately.

## 8. Evaluation that would support an improvement claim

| Property | Suitable evidence |
|---|---|
| Transcript | Coverage plus declared CER/WER definitions; source-checked references and per-source results |
| Formula fidelity | One-to-one equation matching with precision/recall, normalized exact match and manual source checks |
| Formula presentation | Compilation status plus CDM/rendered-expression comparison when available |
| Layout | Type accuracy and box IoU against checked regions, crop completeness for diagrams |
| Reading order | Pairwise ordering accuracy/inversions among matched regions; count missing regions separately |
| Hierarchy | Heading boundary/level/parent accuracy or tree-edit distance against human structure labels |
| Relations | Caption/label-to-figure link precision/recall and continuation-link checks |
| Content preservation | Per-occurrence source-id ledger, ordering constraints and final-artifact checks |
| PDF quality | Aspect ratio, overflow, clipped glyphs/crops, duplicated headings, source-to-PDF spot checks |
| Deployment | Runtime, peak VRAM, output coverage and reproducibility manifest |

OmniDocBench offers component-aware evaluation rather than a single text score.
CDM compares rendered formulas to reduce sensitivity to equivalent LaTeX spellings;
it still does not prove algebraic correctness or faithful extraction from the
original image. MPDocBench-Parse adds document-level hierarchy/continuation
evaluation. Use these ideas at an appropriate scale; do not spend submission day
installing a large benchmark stack if manual source checks will answer the
immediate questions. [OmniDocBench](https://github.com/opendatalab/OmniDocBench),
[CDM](https://github.com/opendatalab/UniMERNet/blob/main/cdm/README.md),
[MPDocBench-Parse](https://arxiv.org/abs/2605.22100)

Keep historical metrics for reproducibility and label revised definitions
separately. With only two validation units, avoid statistical-significance or
unseen-writer claims. Have a second reviewer check a sample of subjective
headings/relations where possible.

## 9. Submission-day work order

1. Finish the running baseline outline job; preserve its JSON and terminal output.
2. Fix deterministic, already-confirmed defects: figure aspect ratio, explicit
   checker-error reporting, expected input coverage and clear metric labels.
   Test crop-candidate changes on inspected examples before applying globally.
3. Render the two validation units from actual clean predictions both with and
   without the existing outline. Compare their PDFs against source images. This
   checks the final path users will see; labels-only PDFs are a diagnostic set.
4. Prefer faithful existing-heading output if the optional organiser adds no
   demonstrated benefit. Do not delay a working PDF for the all-42-unit render.
5. Make the upload/inference/render demonstration runnable, verify one genuinely
   new input if available, and package the adapter, environment and commands.
6. Record measured results, limitations, exact split/reference revisions and a
   few scan-to-PDF examples in the report. Correct outdated README status/counts.
7. Only if these are complete and time remains, run a bounded Surya OCR/grounding
   pilot or a justified training experiment. Keep the known working model and
   environment intact.

The figure/metric fixes and interface are recommendations here, not completed
implementation work. The next user action is to let the tmux job finish and send
its final output; no new training/install command is required for this review.

## 10. Research scope and primary sources

Sources were checked on 2026-10-25. Recommendations are our synthesis; published
scores are not substituted for tests on our data. Versioned checkpoint names in
this review are deliberate comparison candidates, not a universal ranking.

- [Surya official repository](https://github.com/datalab-to/surya): layout, OCR and reading-order output contracts.
- [MPDocBench-Parse](https://arxiv.org/abs/2605.22100): multi-page fidelity and logical hierarchy.
- [Docling document schema](https://docling-project.github.io/docling/concepts/docling_document/): hierarchy and provenance representation.
- [MinerU2.5](https://arxiv.org/abs/2509.22186): global layout and local crop recognition.
- [PaddleOCR-VL-1.6 report](https://arxiv.org/abs/2606.03264): region-focused data improvement.
- [PaddleOCR-VL-1.6 checkpoint](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6): available model/pipeline.
- [LightOnOCR-3-4B](https://huggingface.co/lightonai/LightOnOCR-3-4B): grounded block output.
- [LightOnOCR-2-1B](https://huggingface.co/lightonai/LightOnOCR-2-1B): smaller earlier OCR baseline.
- [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL): model variants and document capabilities.
- [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B): newer multimodal alternative and runtime requirements.
- [olmOCR 2](https://arxiv.org/abs/2510.19817): verifiable content/order tests for OCR training.
- [LayoutLMv3](https://arxiv.org/abs/2204.08387): joint text/image/layout representations.
- [Uni-MuMER](https://arxiv.org/abs/2505.23566): task-specific handwritten math adaptation.
- [MathWriting](https://github.com/google-research/google-research/blob/master/mathwriting/README.md): external handwritten-expression data.
- [OmniDocBench](https://github.com/opendatalab/OmniDocBench): component-aware parsing evaluation.
- [CDM](https://github.com/opendatalab/UniMERNet/blob/main/cdm/README.md): rendered formula matching.
- [DocLayNet](https://arxiv.org/abs/2206.01062): evidence that layout domain diversity matters; not handwriting validation for our pipeline.

Local evidence: `docs/PROJECT_STATEMENT.md`, `docs/RECONSTRUCTION_REVIEW.md`,
`findings/01_dataset.md`, `findings/04_recognition_finetuning.md`,
`logs/train_clean.log`, `data/splits.json`, saved Surya tags, and the recognition,
outline, rendering and evaluation source code at commit `bf7e21e`.
