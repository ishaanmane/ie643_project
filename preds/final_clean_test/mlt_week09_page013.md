$$= \sum_{i=1}^{n} \left[ -x_i + y_i x_i + x_i \frac{e}{1+e^{-w^T x_i}} \right]$$

$$= \sum_{i=1}^{n} \left[ y_i x_i - x_i \left( \frac{1}{1+e^{-w^T x_i}} \right) \right]$$

$$\nabla \log L(w) = \sum_{i=1}^{n} \left[ x_i \left( y_i - \frac{1}{1+e^{-w^T x_i}} \right) \right]$$

**Gradient update rule**

$$w_{t+1} = w_t + \eta_t \nabla \log L(w)$$
$$= w_t + \eta_t \left( \sum_{i=1}^{n} \left[ x_i (y_i - \frac{1}{1+e^{-w_t^T x_i}}) \right] \right)$$

[Diagram: A green box containing $x_i$, an arrow to $y_i$, an arrow to $\theta_i \in \mathbb{R}^d$, an arrow back to the green box via $g(w_t^T x_i)$, with a label $\{0,1\}$ near $y_i$.]

## Regularized Version

$$\min_w \sum_{i=1}^{n} \left[ \log(1+e^{-w^T x_i}) + y_i x_i (1-y_i) \right] + \frac{\lambda}{2} \|w\|^2$$

cross validate hyperparameters. Regularized.