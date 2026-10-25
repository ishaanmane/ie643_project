```markdown
# Bayesian Modeling for Linear Regression

- **Need a prior on \( w \)**, i.e., \( P(w) \in \mathbb{R}^d \)

  - **Likelihood**: \( y|x \sim N(w^T x, \sigma^2 I) \)
    - For simplicity, can use \( \sigma^2 \) as well.
  
  - **A choice of priors**: \( w \sim N(0, \sigma^2 I) \)
    - Covariance matrix:
      $$
      \begin{bmatrix}
      \sigma^2 & \\
      & \ddots & \sigma^2 \\
      & & \sigma^2
      \end{bmatrix}
      $$

- We know,
  $$
  P\left[w/\{(x_1, y_1), \ldots, (x_n, y_n)\}\right] \propto P\left[\frac{(x_1, y_1)}{w}, \ldots, \frac{(x_n, y_n)}{w}\right] \cdot P(w)
  $$
  $$
  \propto \prod_{i=1}^{n} e^{-\frac{(y_i - w^T x_i)^2}{2}} \prod_{i=1}^{d} e^{-\frac{(w_i - 0)^2}{2\sigma^2}}
  $$
  $$
  \propto \prod_{i=1}^{n} e^{-\frac{(y_i - w^T x_i)^2}{2}} e^{-\frac{\sum_{i=1}^{d} w_i^2}{2\sigma^2}}
  $$
  $$
  = e^{-\frac{\|w\|^2}{2\sigma^2}}
  $$

- **MAP Estimation**:
  $$
  \hat{w}_{MAP} = \max_w \sum_{i=1}^{n} -\frac{(y_i - w^T x_i)^2}{2} - \frac{\|w\|^2}{2\sigma^2}
  $$
  $$
  = \min_w \sum_{i=1}^{n} \frac{(y_i - w^T x_i)^2}{2} + \frac{\|w\|^2}{2\sigma^2}
  $$

- Take gradient, set it to 0 & solve for \( \hat{w}_{MAP} \)
```