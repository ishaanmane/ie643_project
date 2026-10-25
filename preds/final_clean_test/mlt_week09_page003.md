# Understanding the Perceptron Update Rule

If mistake, then $w^{t+1} = w^t + x_i y_i$

## Mistake 1
Predicted: +1, Actual: -1, $y_i = -1$
$$w^{t+1} = w^t + x_i y_i$$
$$(w^{t+1})^T x_i = (w^t + x_i y_i)^T x_i = w^T x_i + y_i \|x_i\|^2 \geq 0 \; (>0) \rightarrow \text{Negative}$$

## Mistake 2
Predicted: -1, Actual: +1, $y_i = +1$
$$(w^{t+1})^T x_i = w^T x_i + y_i \|x_i\|^2 < 0 \; (>0)$$

The update rule pushes $w$ in the right direction for $x_i$.

**Example 1:** $w^{new} = w^{old} + x_i \frac{y_i}{y}$

[Diagram: Two scatter plots of data points with a dashed decision boundary line, showing an initial misclassified point near the origin being corrected by the update rule, resulting in a new, more accurate boundary.]

- Fixing $w$ for one $x$, might affect decision for other data points.