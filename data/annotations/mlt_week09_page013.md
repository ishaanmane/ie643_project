$$= \sum_{i=1}^{n}\left[-x_i+y_ix_i+x_i\left(\frac{e^{-w^Tx_i}}{1+e^{-w^Tx_i}}\right)\right] = \sum_{i=1}^{n}\left[y_ix_i - x_i\left(\frac{1}{1+e^{-w^Tx_i}}\right)\right]$$

$$\nabla\log L(w) = \sum_{i=1}^{n}\left[x_i\left(y_i - \frac{1}{1+e^{-w^Tx_i}}\right)\right]$$

## Gradient update rule

$$w_{t+1} = w_t + \eta_t\nabla\log L(w) = w_t + \eta_t\left(\sum_{i=1}^{n}\left[x_i\left(y_i - g(w_t^Tx_i)\right)\right]\right)$$

$x_i\in\mathbb{R}^d$; $y_i\in\{0,1\}$; $\underbrace{y_i-g(w_t^Tx_i)}_{\Theta_i}$

---

## Regularized Version

$$\min_w \sum_{i=1}^{n}\left[\log(1+e^{-w^Tx_i}) + w^Tx_i(1-y_i)\right] + \frac{\lambda}{2}\|w\|^2 \quad \leftarrow \text{Regularizer}$$

Cross validate Hyperparameter $\lambda$
