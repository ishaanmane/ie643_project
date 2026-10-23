$$P\alpha_k = (n\lambda_k)\alpha_k$$

$\hookrightarrow$ Eigen equation as we need to find an $(\alpha_k)$ such that satisfies this equation OR scales $(P\alpha_k)$ by $(n\lambda_k)$

We know, $w_k = X\alpha_k$
$$w_k^Tw_k = (X\alpha_k)^T(X\alpha_k) = \alpha_k^T(X^TX)\alpha_k$$
$$1 = \alpha_k^TP\alpha_k$$

Set $\alpha_k = \dfrac{\beta_k}{\sqrt{n\lambda_k}}$, now: (1) $P\alpha_k = (n\lambda_k)\alpha_k$ (2) $\alpha_k^TP\alpha_k = 1$

$$= \frac{\beta_k^TP\beta_k}{n\lambda_k} = \frac{n\lambda_k}{n\lambda_k} = 1$$

## Algorithm

Input: $\{x_1, \dots, x_n\} \in \mathbb{R}^d$ $[d \gg n]$

- Step 1: compute $k = X^TX$, $k \in \mathbb{R}^{n\times n}$
- Step 2: compute eigendecomposition of $k$; eigenvectors: $\{\beta_1, \dots, \beta_\ell\}$ corresponding to
