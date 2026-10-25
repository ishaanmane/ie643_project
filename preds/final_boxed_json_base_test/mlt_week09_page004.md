```markdown
# We need more careful argument for convergence

## Example 2

### Diagram: Linearly Separable Dataset

- $(\begin{bmatrix} 0 \\ -1 \end{bmatrix}, -1)$
- $(\begin{bmatrix} 0 \\ 0 \end{bmatrix}, +1)$
- $(\begin{bmatrix} 0 \\ 1 \end{bmatrix}, +1)$

### Question:
Is this a linearly separable dataset?

### Answer:
There is.

### Diagram: Linear Separation

- $(\begin{bmatrix} 1 \\ -1 \end{bmatrix}, -1)$
- $(\begin{bmatrix} 0 \\ 0 \end{bmatrix}, +1)$
- $(\begin{bmatrix} 0 \\ 1 \end{bmatrix}, +1)$

### Question:
Is there a $\omega \in \mathbb{R}^2$ such that $w_i^T x_i > 0 \Rightarrow y_i = +1$ and $w_i^T x_i < 0 \Rightarrow y_i = -1$?

### Answer:
There is.

### Diagram: Perceptron Update

- $(\begin{bmatrix} 0 \\ 0 \end{bmatrix})$
- $(\begin{bmatrix} 0 \\ 1 \end{bmatrix})$
- $(\begin{bmatrix} 1 \\ 0 \end{bmatrix})$

### Equations:

$\omega = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$

$\omega^T x_1 = 0$

$\omega^T x_2 = 0$

$\hat{y}_1 = +1$

$\hat{y}_2 = +1$

$\omega' = \omega + x_3 y_3$

$\omega' = \begin{bmatrix} 0 \\ 0 \end{bmatrix} + \begin{bmatrix} 1 \\ -1 \end{bmatrix}$
```