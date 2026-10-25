```markdown
# Gradient Descent for Logistic Regression

## Objective
The goal is to minimize the loss function using gradient descent.

## Loss Function
The loss function for logistic regression can be expressed as:

$$
L(\mathbf{w}) = \sum_{i=1}^{n} \left[ -y_i x_i + y_i w^T x_i + x_i \frac{e^{-w^T x_i}}{1 + e^{-w^T x_i}} \right]
$$

Simplifying the expression:

$$
L(\mathbf{w}) = \sum_{i=1}^{n} \left[ y_i x_i - x_i \left( \frac{1}{1 + e^{-w^T x_i}} \right) \right]
$$

Taking the derivative with respect to $\mathbf{w}$:

$$
\Delta \log L(\mathbf{w}) = \sum_{i=1}^{n} \left[ x_i \left( y_i - \frac{1}{1 + e^{-w^T x_i}} \right) \right]
$$

This derivative represents the gradient of the log-likelihood function.

## Gradient Update Rule
The update rule for the weights $\mathbf{w}$ at time step $t+1$ is given by:

$$
\mathbf{w}_{t+1} = \mathbf{w}_t + \eta_t \nabla \log L(\mathbf{w})
$$

Where:
- $\mathbf{w}_t \in \mathbb{R}^d$
- $\eta_t$ is the learning rate
- $\nabla \log L(\mathbf{w})$ is the gradient calculated above

In vector form:

$$
\mathbf{w}_{t+1} = \mathbf{w}_t + \eta_t \left( \sum_{i=1}^{n} \left[ x_i \left( y_i - \frac{1}{1 + e^{-w_t^T x_i}} \right) \right] \right)
$$

### Regularized Version
To prevent overfitting, we add a regularization term to the loss function:

$$
\min_{\mathbf{w}} \sum_{i=1}^{n} \left[ \log \left( 1 + e^{-w^T x_i} \right) + w_i (1 - y_i) \right] + \frac{\lambda}{2} ||\mathbf{w}||^2
$$

Here:
- $\lambda$ controls the strength of regularization
- The second term penalizes large values of $\mathbf{w}$

This formulation is known as the regularized logistic regression.
```