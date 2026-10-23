# Bayesian Modeling for linear regression

Need a prior on $w$, i.e., $P(w) \in \mathbb{R}^d$

Likelihood: $y/x \sim N(w^Tx, 1)$ ↳ for simplicity, can use $\sigma^2$ as well

A choice of Prior: $w \sim N(0,\gamma^2I)$ $\begin{bmatrix}\gamma^2&&\\&\ddots&\\&&\gamma^2\end{bmatrix}$ covariance matrix

We know,
$$P[w/\{(x_1,y_1),\dots,(x_n,y_n)\}] \propto P[(x_1,y_1),\dots,(x_n,y_n)/w]\cdot P(w)$$

$$\propto \left[\prod_{i=1}^{n}e^{-\frac{(y_i-w^Tx_i)^2}{2}}\right]\left[\prod_{i=1}^{d}e^{-\frac{(w_i-0)^2}{2\gamma^2}}\right]$$

$$\propto \left[\prod_{i=1}^{n}e^{-\frac{(y_i-w^Tx_i)^2}{2}}\right]\left[e^{\frac{1}{2\gamma^2}\left(-\sum_{i=1}^{d}w_i^2\right)}\right] = \left[e^{-\frac{\|w\|^2}{2\gamma^2}}\right]$$

$$\hat{w}_{MAP} = \max_w \sum_{i=1}^{n}-\frac{(y_i-w^Tx_i)^2}{2} - \frac{\|w\|^2}{2\gamma^2}$$

$$= \left(\min_w \sum_{i=1}^{n}\frac{(y_i-w^Tx_i)^2}{2} + \frac{\|w\|^2}{2\gamma^2}\right) f(w)$$

Take gradient, set it to 0 & solve for $\hat{w}_{MAP}$
