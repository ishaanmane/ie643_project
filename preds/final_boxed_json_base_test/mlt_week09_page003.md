```markdown
# Understanding the Perceptron Update Rule

If mistake, then \( \omega^{t+1} = \omega^t + x_i y_i \)

## Mistake 1

Predicted: +1 \( \text{sign}(w^T x_i) \geq 0 \)
Actual: -1 \( y_i = -1 \)

## Mistake 2

Predicted: -1 \( \text{sign}(w^T x_i) < 0 \)
Actual: +1 \( y_i = +1 \)

\[
\omega^{t+1} = \omega^t + x_i y_i
\]

\[
(\omega^{t+1})^T x_i = (\omega^t + x_i y_i)^T x_i
\]

\[
= w^T x_i + y_i \| x_i \|^2
\]

\[
> 0
\]

The update rule pushes \( \omega \) in the right direction for \( x_i \).

### Example 1:

\( w_{\text{new}} = w_{\text{old}} + x_i \frac{y_i}{\| x_i \|} \)

[Diagram: Two-dimensional scatter plot with data points and a decision boundary]

Fixing \( w \) for one \( x_i \) might affect decision for other data points.
```