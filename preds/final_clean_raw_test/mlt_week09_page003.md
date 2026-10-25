# Understanding the Perceptron Update Rule

If mistake, then $w^{t+1} = w^t + x_i y_i$

## Mistake 1
Predicted: +1 $\quad \text{sign}(w^T x_i) \geq 0$
Actual: -1 $\quad y_i = -1$

$$w^{t+1} = w^t + x_i y_i$$
$$(w^{t+1})^T x_i = (w^t + x_i y_i)^T x_i = w^T x_i + y_i \|x_i\|^2 \geq 0 \; (>0) \rightarrow \text{Negative}$$

## Mistake 2
Predicted: -1 $\quad \text{sign}(w^T x_i) < 0$
Actual: +1 $\quad y_i = +1$

$$(w^{t+1})^T x_i = w^T x_i + y_i \|x_i\|^2 < 0 \; (>0)$$

The update rule pushes $w$ in the right direction for $x_i$.

**Example 1:** $w^{\text{new}} = w^{\text{old}} + x_i(y_i)$

[Diagram: A scatter plot of red and green points with an initial separating line $w^{old}$ (dashed) and a new separating line $w^{new}$ (solid), both passing through the origin, with a small orange arrow showing the update direction.]

Fixing $w$ for one $x_i$ might affect decision for other data points.