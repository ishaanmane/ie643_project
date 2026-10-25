---
title: "Lecture notes"
geometry: margin=2cm
papersize: letter
fontsize: 11pt
mainfont: DejaVu Serif
header-includes:
  - \usepackage{float}
  - \floatplacement{figure}{H}
  - \usepackage{fvextra}
  - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,breakanywhere,commandchars=\\\{\}}
  - \usepackage{cancel}
---


<!-- page: upload_notes_page001 -->

## Recap.

**Representing digital images**

**Grayscale:**

![A grid of pixels with one circled, labeled "pixel".](figures/upload_notes_page001_b5.png){width=30.2656%}

$$I: \{1,2\dots r\} \times \{1,\dots c\} \longrightarrow \{0,1,\dots 255\}$$

- pixel $\rightarrow$ pixel intensity $\rightarrow$ grayscale level $\in \{0,1,2\dots 255\}$

$$[0,1]$$

0 — black, 255 — white

<!-- page: upload_notes_page002 -->

![A grid of pixels labeled "red intensity" mapping `\{0,1,\dots255\} \to \[0,1\]` (not typeset).](figures/upload_notes_page002_b1-b2-b4.png){width=37.0513%}

$$R, G, B \quad \text{"pixel values"}$$

$$I(x,y) \to (R,G,B)$$

$$I: \{1,2\dots r\} \times \{1,\dots c\} \to \{0,1,\dots 255\}^3$$

<!-- page: upload_notes_page003 -->

# 1. Point processing

![A grid $I$ (left) transforms via an arrow into a grid $I'$ with one pixel highlighted red.](figures/upload_notes_page003_b2.png){width=55.0000%}

$$I'(x,y) = f(I(x,y))$$

# 2. Neighbourhood processing:

![A grid $I$ (left) around a pixel has a circle drawn around it, transforming via an arrow into a grid $I'$ with the same pixel highlighted red.](figures/upload_notes_page003_b4.png){width=55.0000%}

$$I'(x,y) = f(I(N(x,y)))$$

<!-- page: upload_notes_page004 -->

$$I'(x,y) = \sum_{i} \sum_{j} H(i,j) \cdot I(x(i),y(j))$$

![A grid of pixels from an image $I$ at $(x,y)$ (num rows x num cols $\rightarrow$ pixel resolution), connected via a curved arrow to a smaller filter/kernel grid.](figures/upload_notes_page004_b2.png){width=41.8198%}

Correlation $\rightarrow$ Convolution

![A second grid of pixels from another image, connected via a curved arrow to "Class 3".](figures/upload_notes_page004_b4.png){width=30.9198%}

filter / kernel || learnable in NN.

<!-- page: upload_notes_page005 -->

![A 2D grid of pixels (rows, cols) — "col1", "col2", ..., "colM" — feeding into a column vector of pixel values ($N=4$, circled "100").](figures/upload_notes_page005_b5.png){width=30.7898%}

$$z = \sum_j w_j x_j$$
$$a = \phi(z)$$

![A 5x5 grid with a red-highlighted 3x3 sub-grid, labeled "5x5".](figures/upload_notes_page005_b3-b9.png){width=55.0000%}

Striding (cols + rows)

$$\underbrace{w_1}_{w_1}, \underbrace{w_2}_{w_2}, \underbrace{w_3}_{w_3}$$

$$z = \sum_i w_i p(x(i), y(i))$$
$$a = \phi(z)$$

<!-- page: upload_notes_page006 -->

## Local rot. fields.

![A grid over a hand shape, with several colored boxes (red, green, purple) highlighting local regions, labeled "Conv. feat. map".](figures/upload_notes_page006_b2.png){width=19.9840%}

$$\vdots$$

**equivariant to transformations in orig. input**

![Two identical hand shapes, one rotated slightly relative to the other, labeled "rotations / zoom operations".](figures/upload_notes_page006_b7-b8.png){width=55.0000%}

<!-- page: upload_notes_page007 -->

![A grid of 3x3 pixel patches (input feature map) feeding into separate 3x3 filter kernels, each producing a single output channel — "Channels of output conv. feat map".](figures/upload_notes_page007_b1-b2-b3-b4-b5-b6-b7-b10-b8-b9-b11-b12.png){width=55.0000%}

num of filters

<!-- page: upload_notes_page008 -->

![A single filter with 3 channels, labeled "Single channel map".](figures/upload_notes_page008_b1-b2.png){width=30.6225%}

$$h_i \times w_i \quad (\text{kernel size}, \text{stride}, \text{padding}) \qquad h_0 \times w_0$$

![A 16x16 input grid (labeled 16) being convolved with several 5x5 filters ($f_1, f_2, \dots$) — each producing an output grid of size 8x8.](figures/upload_notes_page008_b3.png){width=43.9774%}

<!-- page: upload_notes_page009 -->

5x5x8 channel (video based conv)

12 such filters → 12 channel output

![A 4x4 grid of 12 channels feeding into a 30-channel layer.](figures/upload_notes_page009_b2-b3-b5-b6.png){width=55.0000%}

4x4x12 → 30

<!-- page: upload_notes_page010 -->

$$\frac{\partial e}{\partial w_f^l} = \delta^{l+1}$$

![A 5x5 box labeled "LeNet" feeding into a chain of boxes.](figures/upload_notes_page010_b3.png){width=37.4995%}

Max-pooling, Avg-pool, Min-pool, Mixed-pool, frac-pool, dynamic pooling

![A 2x2 grid of red squares (pooling region) over a larger grid, with arrows connecting each red square's max value to the output neuron.](figures/upload_notes_page010_b5-b6.png){width=55.0000%}

# Original source pages

Original scans for checking transcription and diagrams.

![Original source page 1](sources/source_001.jpg){width=90.0000%}

![Original source page 2](sources/source_002.jpg){width=90.0000%}

![Original source page 3](sources/source_003.jpg){width=90.0000%}

![Original source page 4](sources/source_004.jpg){width=90.0000%}

![Original source page 5](sources/source_005.jpg){width=90.0000%}

![Original source page 6](sources/source_006.jpg){width=90.0000%}

![Original source page 7](sources/source_007.jpg){width=90.0000%}

![Original source page 8](sources/source_008.jpg){width=90.0000%}

![Original source page 9](sources/source_009.jpg){width=90.0000%}

![Original source page 10](sources/source_010.jpg){width=90.0000%}
