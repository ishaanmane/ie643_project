# Fonts

Merriweather (Sorkin Type, SIL Open Font License 1.1) for the reconstructed PDFs.
Fetch once (GPU machine), from the repo root:

```bash
for s in Regular Bold Italic BoldItalic; do curl -fsSL -o 04_reconstruction/fonts/Merriweather-$s.ttf https://github.com/SorkinType/Merriweather/raw/master/fonts/ttf/Merriweather-$s.ttf; done
curl -fsSL -o 04_reconstruction/fonts/OFL.txt https://github.com/SorkinType/Merriweather/raw/master/OFL.txt
```

Without these files the renderer falls back to an installed Merriweather, then DejaVu Serif.
