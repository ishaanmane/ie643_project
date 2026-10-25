```markdown
# Understanding the Perceptron Update Rule

If mistake, then $\omega^{t+1} = \omega^t + x_i y_i$

## Mistake 1
- Predicted: +1
- Actual: -1
- $y_i = -1$

$$
\begin{aligned}
w^{t+1} &= w^t + x_i y_i \\
(w^{t+1})^T x_i &= (w^t + x_i y_i)^T x_i \\
&= w^T x_i + y_i \|x_i\|^2 \\
&\geq 0
\end{aligned}
$$

## Mistake 2
- Predicted: -1
- Actual: +1
- $y_i = +1$

$$
\begin{aligned}
(w^{t+1})^T x_i &= w^T x_i + y_i \|x_i\|^2 \\
&< 0
\end{aligned}
$$

The update rule pushes $w$ in the right direction for $x_i$.

### Example 1:
$$
w_{new} = w_{old} + x_i \frac{y_i}{y_i}
$$

[Diagram: Two-dimensional scatter plot showing data points with different labels (+1 and -1). The original weight vector is shown, along with the new weight vector after updating based on a specific point.]

Fixing $w$ for one $x$, might affect decision for other data points.
```
