```markdown
# Bayesian Modeling for Linear Regression

- **Need a prior on \( w \)**, i.e., \( P(w) \in \mathbb{R}^d \)

## Likelihood

\( y|x \sim N(w^T x, 1) \)  
For simplicity, can use \( \sigma^2 \) as well.

### Choice of Priors

\( w \sim N(0, \sigma^2 I) \)  
Covariance matrix

## We Know

\[ P[w / \{(x_1, y_1), \ldots, (x_n, y_n)\}] \propto P[(x_1, y_1), \ldots, (x_n, y_n) / w] \cdot P(w) \]

\[
\propto \prod_{i=1}^{n} e^{-\frac{(y_i - w^T x_i)^2}{2}} \prod_{i=1}^{d} e^{-\frac{(w_i - 0)^2}{2\sigma^2}}
\]

\[
\propto \prod_{i=1}^{n} e^{-\frac{(y_i - w^T x_i)^2}{2}} e^{\frac{1}{2\sigma^2} \left(-\sum_{i=1}^{d} w_i^2\right)} = e^{-\frac{||w||^2}{2\sigma^2}}
\]

## MAP Estimation

\[
\hat{w}_{MAP} = \max_w \sum_{i=1}^{n} -\frac{(y_i - w^T x_i)^2}{2} - \frac{||w||^2}{2\sigma^2}
\]

\[
= \min_w \sum_{i=1}^{n} \frac{(y_i - w^T x_i)^2}{2} + \frac{||w||^2}{2\sigma^2} + f(w)
\]

Take gradient, set it to 0 & solve for \( \hat{w}_{MAP} \)
```