# 05 · Evaluation metrics

Details and commands: [../05_evaluation/README.md](../05_evaluation/README.md).

- Kept from development: page CER / WER (capped), text-only CER, strict equation match.
- Added, following Nougat and OmniDocBench: corpus CER, NED, token precision / recall / F1
  (hallucination vs omission), BLEU-4, length ratio; normalised equation precision / recall / F1
  and equation edit score; diagram count accuracy; heading recall; 95% bootstrap intervals and a
  paired bootstrap between two systems.
- **Strict equation match understates the model**: 0.137 strict vs 0.338 normalised F1 and 0.703
  edit score on test. Most "misses" are notation differences (`\le` vs `\leq`, `\left(`, spacing).
- 76 test pages is small: intervals are about +-0.04 on NED, so differences under that need the
  paired test.
- Not used: CDM (rendered-formula matching; needs its own toolchain) and LLM judges (not
  reproducible). TEDS not needed (14 tables in 410 pages).
