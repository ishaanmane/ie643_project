## Perceptron Training Algorithm

$$D = \{(x^i, y^i)\}_{i=1,2,3,\dots}$$

$$\tilde{w}^0 = \vec{0} \quad \text{(random vectors)}$$

for each round $t = 0, 1, 2, 3, \dots$
- receive $(x^t, y^t) \rightarrow (\tilde{x}^t, y^t)$
- $\hat{y}^t = \text{Perceptron}(\tilde{x}^t; \tilde{w}^t)$
- if $\hat{y}^t = y^t$: $\tilde{w}^{t+1} = \tilde{w}^t$, else $\tilde{w}^{t+1} = \tilde{w}^t + y^t \tilde{x}^t$

$$x^t \in \mathbb{R}^d, \quad w^t \in \mathbb{R}^d$$

$$\langle w, x \rangle - \theta \geq 0 \to +1; \quad < 0 \to -1$$
$$\langle \tilde{w}, \tilde{x} \rangle \geq 0 \to +1; \quad < 0 \to -1$$

$$\tilde{w} = \begin{bmatrix} \vec{w} \\ -\theta \end{bmatrix} \qquad \tilde{x} = \begin{bmatrix} \vec{x} \\ 1 \end{bmatrix}$$
