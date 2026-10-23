algorithm

Let's consider the following dataset:

[Diagram: A line through the origin with points $x_1$ and $x_2$ marked, their projections $(x_1^Tw)w$ and $(x_2^Tw)w$ shown on the line via dashed connectors.]

Let's suppose we collect the proxies. $w$ is any arbitrary line. $\{x_1^Tw, x_2^Tw, \dots, x_n^Tw\}$

$$\text{Average} = \frac{1}{n}\sum_{i=1}^{n}(x_i^Tw) = \left(\frac{1}{n}\sum_{i=1}^{n}x_i\right)^Tw = 0^T\cdot w \; [\text{for a centered dataset}] = 0$$

$$\text{Variance} = \frac{1}{n}\sum_{i=1}^{n}(x_i^Tw - \text{mean})^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i^Tw)^2$$

**Conclusion:** Error minimization on centered data $\Leftrightarrow$ Variance maximisation

## Geometrical representation

[Diagram: Two scatter plots of height/weight-like data. Left: original axes (height centered, weight centered) with two rotated axes $\frac{-\sqrt{2}}{1/\sqrt{2}}$ and $\frac{1/\sqrt{2}}{1/\sqrt{2}}$ shown, labeled "height gives some information about weight." Right: data plotted against rotated axes $\frac{-\text{height}+\text{weight}}{\sqrt{2}}$ and $\frac{\text{height}+\text{weight}}{\sqrt{2}}$, labeled "$(h+w)/\sqrt{2}$ does not give any information about $\frac{w-h}{\sqrt{2}}$."]
