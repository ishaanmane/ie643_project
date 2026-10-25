# Understanding the Perceptron Update Rule

If mistake, then $w^{t+1} = w^t + x_iy_i$

**Mistake 1**
Predicted: +1 $\quad \text{sign}(w^T x_i) \geq 0$
Actual: -1 $\quad y_i = -1$

$$w^{t+1} = w^t + x_iy_i$$
$$(w^{t+1})^Tx_i = (w^t+x_iy_i)^Tx_i = w^Tx_i + y_i\|x_i\|^2 > 0 \quad \text{(Negative)}$$

**Mistake 2**
Predicted: -1 $\quad \text{sign}(w^T x_i) < 0$
Actual: +1 $\quad y_i = +1$

$$(w^{t+1})^Tx_i = w^Tx_i + y_i\|x_i\|^2 < 0 \quad (>0)$$

The update rule pushes $w$ in the right direction for $x_i$.

**Example 1:** $w^{new} = w^{old} + x_i(y_i)$

[Diagram: A scatter plot with a dashed decision boundary, a point $x_i$ marked, and the new updated weight vector $w^{new}$ pointing in the correct direction.]

$\rightarrow$ [Diagram: The same scatter plot with the original weight $w^{old}$, the new weight $w^{new}$, and a new set of errors marked around the updated boundary.]

- Fixing $w$ for one $x$, might affect decision for other data points.