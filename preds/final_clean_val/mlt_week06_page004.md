# Bayesian Modeling for linear regression

- Need a prior on $w$, i.e., $P(w) \in \mathbb{R}^d$

Likelihood: $y/x \sim N(w^Tx, 1)$ (for simplicity, can use $\sigma^2$ as well)

A choice of priors: $w \sim N(0, \sigma^2 I)$ — covariance matrix

$$\begin{bmatrix} \sigma^2 \\ \vdots \\ \sigma^2 \end{bmatrix}$$

We know,
$$P[w/\{(x_1,y_1),\dots,(x_n,y_n)\}] \propto P[(x_1,y_1),\dots,(x_n,y_n)/w] \cdot P(w)$$

$$\propto \left[\prod_{i=1}^{n} e^{-\frac{(y_i-w^Tx_i)^2}{2}}\right] \left[\prod_{i=1}^{d} e^{-\frac{(w_i-\mu)^2}{2\sigma^2}}\right]$$

$$\propto \left[\prod_{i=1}^{n} e^{-\frac{(y_i-w^Tx_i)^2}{2}}\right] e^{\frac{1}{2\sigma^2}\left(\sum_{i=1}^{d} w_i^2\right)} = e^{-\frac{\|w\|^2}{2\sigma^2}}$$

$$\hat{w}_{MAP} = \max_w \sum_{i=1}^{n} -\frac{(y_i-w^Tx_i)^2}{2} - \frac{\|w\|^2}{2\sigma^2}$$

$$= \min_w \sum_{i=1}^{n} \frac{(y_i-w^Tx_i)^2}{2} + \frac{\|w\|^2}{2\sigma^2} \quad f(w)$$

Take gradient, set it to 0 & solve for $\hat{w}_{MAP}$