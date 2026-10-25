$$= \sum_{i=1}^{n} \left[-x_i + y_i x_i + x_i \frac{e}{1+e^{-w^T x_i}}\right]$$

$$= \sum_{i=1}^{n} \left[y_i x_i - x_i \left(\frac{1}{1+e^{-w^T x_i}}\right)\right]$$

$$\nabla \log L(w) = \sum_{i=1}^{n} \left[x_i \left(y_i - \frac{1}{1+e^{-w^T x_i}}\right)\right]$$

## Gradient update rule,

$$w_{t+1} = w_t + \eta_t \nabla \log L(w) \in \mathbb{R}^d$$
$$= w_t + \eta_t \left(\sum_{i=1}^{n} \left[x_i (y_i - \frac{1}{1+e^{-w_t^T x_i}})\right]\right)$$

[Diagram: A chain of nodes — $x_i$, $y_i \in \{0,1\}$, $\theta_i$, $g(w_t^T x_i)$ — with an arrow from each $x_i$ to its corresponding $y_i$ node.]

$$\min_w \underbrace{\sum_{i=1}^{n} \left[\log(1+e^{w^T x_i}) + w_i^T x_i (1-y_i)\right]}_{\text{REGULARIZED VERSION}} + \underbrace{\frac{\lambda}{2}\|w\|^2}_{\text{Regularized}} \rightarrow \text{CROSS VALIDATE Hyperparameters}$$