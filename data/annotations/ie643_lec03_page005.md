# Train a perceptron: (Online learning)

$$\mathcal{D} = \{(x^t, y^t)\}_{t=1, 2, 3, \dots}$$

- $\tilde{w}^0 = \vec{0}$
- $t = 0, 2, 3, \dots$:
  - receive a sample $(x^t, y^t) \in \mathcal{D}$
  - $\tilde{x}^t = \begin{bmatrix} x^t \\ 1 \end{bmatrix}$
  - $\hat{y}^t = \text{Perceptron}(\tilde{x}^t; \tilde{w}^t) \quad \text{(Prediction)}$

## Update rule:

- **if** $\hat{y}^t == y^t$:
  - no update:
    $$\tilde{w}^{t+1} = \tilde{w}^t$$

- **else**:
  > $$\tilde{w}^{t+1} = \tilde{w}^t + y^t \tilde{x}^t$$