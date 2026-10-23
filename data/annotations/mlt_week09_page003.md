# Understanding the Perceptron Update Rule

If mistake, then $w^{t+1} = w^t + x_iy_i$

**Mistake 1** | **Mistake 2**
---|---
Predicted: +1, $\text{sign}(w^{tT}x_i)\geq0$; Actual: -1, $y_i=-1$ | Predicted: -1, $\text{sign}(w^{tT}x_i)<0$; Actual: +1, $y_i=+1$

$$w^{t+1}=w^t+x_iy_i$$
$$(w^{t+1})^Tx_i = (w^t+x_iy_i)^Tx_i = w^{tT}x_i + y_i\|x_i\|^2$$
(left case: $\geq0$ term plus $-1\cdot\|x_i\|^2$, negative)  (right case: $<0$ term plus $+1\cdot\|x_i\|^2$, positive)

The update rule pushes $w$ in the right direction for $x_i$

**Example 1:** $w^{new} = w^{old} + x\left(\frac{1}{y}\right)$

[Diagram: Two scatter plots with green (+1) and red (-1) points and a dashed separating line. Left: $w^{old}$ vector shown, a misclassified red point circled. Right: after update, $w^{new}$ points differently, the boundary has shifted, and a "new errors" region is circled — fixing one point may misclassify others.]

- Fixing $w$ for one $x$, might affect decision for other data points.
