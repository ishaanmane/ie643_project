# 06 · Interface (Notes2PDF)

- Upload page: PDF, HEIC/HEIF (iPhone), JPG, PNG, WebP, BMP, TIFF; up to 20 pages and 25 MiB.
  Downloads: PDF, Markdown, editable bundle, conversion report. Private access key; files deleted
  after 24 h. Tests: 25 interface + 13 renderer, passing.
- **Speed:** models load on the first upload (about a minute), stay on the GPU while used, and are
  unloaded after 15 idle minutes. Surya runs with a 35% GPU share so both models fit (about 13 of
  16 GB); diagram detection runs at the same time as text recognition. Before: every upload
  restarted both models.
- **Public link:** Tailscale Funnel, a fixed `https://notes2pdf.<tailnet>.ts.net` address instead of
  a random trycloudflare link (still available as an option).
- UI built by another assistant, reviewed: kept the design, renamed to Notes2PDF, plain wording,
  pipeline steps on the page, model status in the footer; outdated deployment docs removed.
- Limits and extreme cases (e.g. a 30-page PDF under 25 MiB is accepted, then stopped before any
  model runs): [../docs/REPORT_NOTES.md](../docs/REPORT_NOTES.md).
- **Verified on the GPU** with the final adapter (real uploads, PDFs downloaded). Problems found
  and fixed while testing: Tailscale Funnel needed a one-time approval (now shown by the
  launcher) and its relay was too slow for downloads (~3 KB/s), so Cloudflare is used for the
  demo; a stopped server left its Surya vLLM process holding port 8001 and 5 GB (stopping now
  unloads the models); text like `↓ = ∑` broke the PDF through the symbol fallback (now XeTeX
  character classes); a `<!-- page -->` marker was printed on uploads; 5.7 MB PDFs from
  full-size appendix pages (now 1600 px, about 5x smaller).
