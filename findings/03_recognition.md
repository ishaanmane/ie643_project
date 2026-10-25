# 03 · Recognition (Qwen2.5-VL-7B, 4-bit QLoRA)

Full table: [../results/recognition_experiments.md](../results/recognition_experiments.md).

- Setup: LoRA rank 16 on all attention and MLP projections (47.6M trainable, 0.57%), lr 1e-4
  cosine, 3 epochs, batch 1 x 8, images up to 1M pixels, loss on the answer only, best epoch by
  validation loss. RTX 5060 Ti 16 GB.
- **Fine-tuning halves the errors** (test, 76 pages): corpus CER 0.915 -> 0.332, NED 0.596 -> 0.311,
  token F1 0.623 -> 0.855, normalised equation F1 0.143 -> 0.338, equation edit score 0.336 -> 0.703.
  Better on 74 of 76 pages. The zero-shot model also writes 1.5-3x too much text.
- By source (test NED, clean): HumynLabs 0.170, digital ink 0.300, IE802 notebook 0.327,
  chalkboard 0.331.
- **clean vs boxed_json** (boxes drawn + JSON layout in the prompt): no measurable difference.
  Test paired NED +0.001 (95% CI -0.019 to +0.020), 32 pages better / 39 worse; val -0.011
  (CI -0.036 to +0.013). **clean is the final model**: no Surya step before recognition, training
  53 vs 61 min, peak memory 10.8 vs 13.1 GB.
- Validation loss: clean 0.484 / 0.432 / 0.429; boxed_json ends at 0.428.
- Problems met: boxed_json ran out of GPU memory from fragmentation on the first attempt; fixed
  with `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`. Old predictions would have been reused
  silently by the resumable predictor; runs are now isolated by name and never overwrite an adapter.
- Adapter: `runs/final_clean/final_adapter` on the GPU machine (not in git; to be backed up).
