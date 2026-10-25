# Understanding the Perceptron Update Rule

If mistake, then $w^{t+1} = w^t + x_iy_i$

**Mistake 1** | **Mistake 2**
---|---
Predicted: +1, $\text{sign}(w^{tT}x_i)\geq0$; Actual: -1, $y_i=-1$ | Predicted: -1, $\text{sign}(w^{tT}x_i)<0$; Actual: +1, $y_i=+1$

$$w^{t+1}=w^t+x_iy_i$$
$$(w^{t+1})^Tx_i = (w^t+x_iy_i)^Tx_i = \underbrace{w^{tT}x_i}_{\geq0} + \underbrace{\underbrace{y_i}_{-1}\underbrace{\|x_i\|^2}_{>0}}_{\text{Negative}}$$
$$(w^{t+1})^Tx_i = \underbrace{w^{tT}x_i}_{<0} + \underbrace{\underbrace{y_i}_{+1}\|x_i\|^2}_{>0}$$

The update rule pushes $w$ in the right direction for $x_i$

**Example 1:** $w^{new} = w^{old} + x\underbrace{(1)}_{y}$

[Diagram: Scatter plot with green (+1) and red (-1) points, a dashed separating line, vectors $w^{old}$ and $w^{new}$, and a circled green point $x$.]

[Diagram: Scatter plot after the update, with $w^{old}$ and $w^{new}$, the shifted orange boundary, circled point $x$, and circled green points labeled "new errors".]

- Fixing $w$ for one $x$, might affect decision for other data points.
