```markdown
# Logistic Regression

## Probability of y = 1 given x

$$
P(y=1|x) = \frac{1}{1+e^{-w^Tx}}
$$

### Dataset

Dataset: $\{(x_1, y_1), \ldots, (x_n, y_n)\}$

## Finding w: Maximum Likelihood

### Likelihood Function

$$
L(w; Data) = \prod_{i=1}^{n} g(w^T x_i)^{y_i} (1 - g(w^T x_i))^{(1-y_i)}
$$

### Log-Likelihood Function

$$
\log L(w; Data) = \sum_{i=1}^{n} y_i \log(g(w^T x_i)) + (1-y_i) \log(1-g(w^T x_i))
$$

$$
= \sum_{i=1}^{n} y_i \log\left(\frac{1}{1+e^{-w^T x_i}}\right) + (1-y_i) \log\left(\frac{e^{-w^T x_i}}{1+e^{-w^T x_i}}\right)
$$

### Simplified Log-Likelihood Function

$$
\log L(w) = \sum_{i=1}^{n} \left[(1-y_i)(-w^T x_i) - \log(1+e^{-w^T x_i})\right]
$$

### Optimization Goal

Maximize:

$$
\max_w \sum_{i=1}^{n} (1-y_i)(-w^T x_i) - \log(1+e^{-w^T x_i})
$$

## No Closed Form Expression

Can perform gradient descent (ascent)

### Gradient of Log-Likelihood Function

$$
\nabla \log L(w) = \left[(1-y_i)(-x_i) - \left(\frac{e^{-w^T x_i}}{1+e^{-w^T x_i}}\right)(-x_i)\right]
$$

$$
= \left[-x_i + y_i x_i + x_i \frac{e^{-w^T x_i}}{1+e^{-w^T x_i}}\right]
$$

## Page Footer

Week 9 Page 12
```