# Train a Perceptron (Online Learning)

$$\mathcal{D} = \{(x^t, y^t)\}_{t=1, 2, 3, \dots}$$

- $\tilde{w}^0 = \vec{0}$
- For $t = 1, 2, 3, \dots$:
  - Receive a sample $(x^t, y^t) \in \mathcal{D}$
  - $\tilde{x}^t = \begin{bmatrix} x^t \\ 1 \end{bmatrix}$
  - $\hat{y}^t = \text{Perceptron}(\tilde{x}^t; \tilde{w}^t) \quad \text{(Prediction)}$

## Update Rule:

- **If** $\hat{y}^t == y^t$:
  - No update:
    $$\tilde{w}^{t+1} = \tilde{w}^t$$

- **Else**:
  > $$\tilde{w}^{t+1} = \tilde{w}^t + y^t \tilde{x}^t$$