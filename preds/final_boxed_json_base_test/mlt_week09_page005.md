```markdown
# Handwritten Lecture Note Page

## Linear Separability with ε-Margin

### Text Block 1
We see that we are right back where we started. The algorithm is unable to provide a w which can correctly classify all the data points correctly. It just won't converge. Let's modify our assumption.

### Assumption
Linear Separability with ε-Margin

### Text Block 2
A dataset $\{(x_i, y_i)\}$ is linearly separable with ε-margin if there exists some ε > 0 such that:
$$(w^T x_i) y_i \geqslant ε \quad \forall i$$

### Diagram: Linear Separability with ε-Margin
The gap can be very small but not zero. No points lie on the gap.

### Math Blocks
1. $$\omega^1 = \omega^0 + x_3 y_3 = \begin{bmatrix}0\\0\end{bmatrix} + \begin{bmatrix}-1/2\\1/2\end{bmatrix}^{-1} = \begin{bmatrix}1\\-1/2\end{bmatrix}$$
2. $$\omega^2 = \omega^1 + x_2 y_2 = \begin{bmatrix}1\\-1/2\end{bmatrix} + \begin{bmatrix}0\\1\end{bmatrix}^{-1} = \begin{bmatrix}1\\1/2\end{bmatrix}$$
3. $$\omega^3 = \omega^2 + x_1 y_1 = \begin{bmatrix}1\\1/2\end{bmatrix} + \begin{bmatrix}1\\-1/2\end{bmatrix} = \begin{bmatrix}1\\1/2\end{bmatrix}$$
```