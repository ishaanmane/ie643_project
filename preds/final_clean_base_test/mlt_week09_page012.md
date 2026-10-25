```markdown
# Logistic Regression

The probability of the outcome \( y = 1 \) given input \( x \) is given by:

$$ P(y=1|x) = \frac{1}{1 + e^{-w^T x}} $$

For a dataset \( \{(x_1, y_1), \ldots, (x_n, y_n)\} \), we want to find the weights \( w \) that maximize the likelihood.

## Maximum Likelihood

To find \( w \), we use the maximum likelihood method:

$$ L(w; Data) = \prod_{i=1}^{n} g(w^T x_i)^{y_i} (1 - g(w^T x_i))^{(1-y_i)} $$

Taking the log of the likelihood function:

$$ \log L(w; Data) = \sum_{i=1}^{n} y_i \log(g(w^T x_i)) + (1 - y_i) \log(1 - g(w^T x_i)) $$

Simplifying further:

$$ \log L(w) = \sum_{i=1}^{n} y_i \log\left(\frac{1}{1 + e^{-w^T x_i}}\right) + (1 - y_i) \log\left(\frac{e^{-w^T x_i}}{1 + e^{-w^T x_i}}\right) $$

$$ \log L(w) = \sum_{i=1}^{n} \left[(1 - y_i)(-w^T x_i) - \log(1 + e^{-w^T x_i})\right] $$

The goal is to maximize:

$$ \max_w \sum_{i=1}^{n} (1 - y_i)(-w^T x_i) - \log(1 + e^{-w^T x_i}) $$

Since there is no closed-form expression for the optimal \( w \), gradient descent can be used instead.

## Gradient Descent

The gradient of the log-likelihood function with respect to \( w \):

$$ \nabla \log L(w) = \left[ (1 - y_i)(-x_i) - \left(\frac{e^{-w^T x_i}}{1 + e^{-w^T x_i}}\right)(-x_i) \right] $$

Simplifying:

$$ \nabla \log L(w) = \left[ -x_i + y_i x_i + x_i \frac{e^{-w^T x_i}}{1 + e^{-w^T x_i}} \right] $$

This gradient can be used to iteratively update the weights \( w \) until convergence.
```