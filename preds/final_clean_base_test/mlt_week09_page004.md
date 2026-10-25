```markdown
# Example 2

We need more careful argument for convergence.

## Diagram: Linearly Separable Dataset

The dataset is linearly separable if there exists a hyperplane that can separate the two classes (+1 and -1) without any overlap. In this case:

- $\left(\begin{bmatrix}0\\0\end{bmatrix}, +1\right)$
- $\left(\begin{bmatrix}-1\\0\end{bmatrix}, +1\right)$
- $\left(\begin{bmatrix}-1\\1/2\end{bmatrix}, -1\right)$

There is a vector $\omega \in \mathbb{R}^2$ such that:
- If $\omega^\top x_i > 0$, then $y_i = +1$
- If $\omega^\top x_i < 0$, then $y_i = -1$

## Diagram: Perceptron Update

In the perceptron algorithm, the weight vector $\omega$ is updated based on the misclassified data point. The update rule is:

$$
\omega' = \omega + x_i y_i
$$

Where:
- $\omega = \begin{bmatrix}0 & 0\end{bmatrix}$
- $x_3 = \begin{bmatrix}-1\\1/2\end{bmatrix}$
- $y_3 = +1$

Thus, after updating with $x_3$ and $y_3$, the new weight vector becomes:

$$
\omega' = \begin{bmatrix}0 & 0\end{bmatrix} + \begin{bmatrix}-1\\1/2\end{bmatrix} = \begin{bmatrix}-1\\1/2\end{bmatrix}
$$

This process continues until convergence.
```