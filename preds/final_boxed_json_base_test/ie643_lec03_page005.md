```markdown
# Train a Perceptron:

## Online Learning

$\mathcal{D} = \left\{(x^t, y^t)\right\}$

$\rightarrow \tilde{w}^0 = \overrightarrow{0}$

$t = 1, 2, 3, \ldots$

## Update Rule:

If $\hat{y}^t == y^t$:
- No update
- $\tilde{w}^{t+1} = \tilde{w}^t$

Else:
- $\tilde{w}^{t+1} = \tilde{w}^t + y^t x^t$

## Receive a Sample $(x^t, y^t) \in \mathcal{D}$

$\rightarrow \tilde{x}^t = \begin{bmatrix} x^t \\ 1 \end{bmatrix}$

$\rightarrow \hat{y}^t = \text{Perceptron}(\tilde{x}^t, \tilde{w}^t)$ [Prediction]
```