# Recognition experiments (final split, current images and Surya boxes)

All runs: Qwen2.5-VL-7B, 4-bit QLoRA rank 16, lr 1e-4, 3 epochs, 303 training pages, images up to
1M pixels, best epoch by validation loss. Scores from `05_evaluation/evaluate.py` (`metrics.py`).
Lower is better for CER, NED, text CER; higher for the rest; length ratio ideal 1.0.

- **clean**: preprocessed page + instruction.
- **boxed_json**: page with Surya boxes drawn + instruction + the boxes as JSON (Qwen grounding format).

| | clean | boxed_json |
|---|---|---|
| Validation loss (epochs 1 / 2 / 3) | 0.484 / 0.432 / 0.429 | - / - / 0.428 |
| Training time, peak GPU memory | 53 min, 10.8 GB | 61 min, 13.1 GB |
| Needs Surya before recognition | no | yes |

### val (31 pages)

| Run | CER | corpus CER | NED | text CER | token F1 | BLEU-4 | eq strict | eq F1 (norm.) | eq edit | diagram count acc. | heading recall | length ratio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zero-shot (clean prompt) | 0.761 | 1.130 | 0.587 | 0.879 | 0.595 | 0.362 | 0.040 | 0.117 | 0.365 | 0.645 | 0.846 | 3.252 |
| Zero-shot (boxed_json prompt) | 0.700 | 0.787 | 0.547 | 0.887 | 0.610 | 0.418 | 0.053 | 0.132 | 0.304 | 0.677 | 0.846 | 1.740 |
| Fine-tuned clean | 0.331 | 0.341 | 0.315 | 0.307 | 0.838 | 0.728 | 0.198 | 0.437 | 0.809 | 0.806 | 0.846 | 1.030 |
| Fine-tuned boxed_json | 0.314 | 0.326 | 0.304 | 0.296 | 0.855 | 0.717 | 0.237 | 0.435 | 0.790 | 0.839 | 0.846 | 0.953 |

NED 95% CI: clean 0.247-0.390, boxed_json 0.244-0.368
Paired, boxed_json - clean (NED): -0.011 (95% CI -0.036 to +0.013); boxed_json better on 17 pages, worse on 13

NED by source (clean / boxed_json): ie643 0.309 / 0.306, mlt 0.244 / 0.232, ie802 0.515 / 0.470, hlcs 0.067 / 0.040

### test (76 pages)

| Run | CER | corpus CER | NED | text CER | token F1 | BLEU-4 | eq strict | eq F1 (norm.) | eq edit | diagram count acc. | heading recall | length ratio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zero-shot (clean prompt) | 0.730 | 0.915 | 0.596 | 0.774 | 0.623 | 0.407 | 0.011 | 0.143 | 0.336 | 0.737 | 0.645 | 1.772 |
| Zero-shot (boxed_json prompt) | 0.653 | 0.779 | 0.545 | 0.719 | 0.638 | 0.430 | 0.016 | 0.124 | 0.277 | 0.711 | 0.677 | 1.539 |
| Fine-tuned clean | 0.325 | 0.332 | 0.311 | 0.227 | 0.855 | 0.707 | 0.137 | 0.338 | 0.703 | 0.882 | 0.710 | 0.982 |
| Fine-tuned boxed_json | 0.330 | 0.347 | 0.313 | 0.253 | 0.858 | 0.690 | 0.160 | 0.324 | 0.686 | 0.882 | 0.710 | 0.981 |

NED 95% CI: clean 0.275-0.348, boxed_json 0.272-0.353
Paired, boxed_json - clean (NED): +0.001 (95% CI -0.019 to +0.020); boxed_json better on 32 pages, worse on 39

NED by source (clean / boxed_json): ie643 0.331 / 0.316, mlt 0.300 / 0.307, ie802 0.327 / 0.377, hlcs 0.170 / 0.132

## Conclusion

Fine-tuning roughly halves every error measure against zero-shot, for both variants. Between the
two variants there is **no measurable difference**: on test the paired NED difference is +0.001
(95% CI -0.019 to +0.020), with boxed_json better on 32 pages and worse on 39; on validation -0.011
(CI -0.036 to +0.013). **clean is kept** as the final model: same accuracy, no Surya step before
recognition, 15% faster training and 2.3 GB less GPU memory. (The first boxed_json attempt ran out
of GPU memory and was re-run with `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`.)
