```markdown
# Gradient Descent for Logistic Regression

## Loss Function and Gradient Update Rule

The loss function \( L(\mathbf{w}) \) for logistic regression can be expressed as:

\[
L(\mathbf{w}) = -\sum_{i=1}^{n} \left( y_i \log \left( \frac{1}{1 + e^{-\mathbf{w}^T \mathbf{x}_i}} \right) + (1 - y_i) \log \left( 1 - \frac{1}{1 + e^{-\mathbf{w}^T \mathbf{x}_i}} \right) \right)
\]

The gradient update rule for the weights \( \mathbf{w} \) is given by:

\[
\mathbf{w}_{t+1} = \mathbf{w}_t + \eta_t \nabla L(\mathbf{w})
\]

Where:
- \( \mathbf{w}_t \) is the weight vector at time step \( t \).
- \( \eta_t \) is the learning rate at time step \( t \).
- \( \nabla L(\mathbf{w}) \) is the gradient of the loss function with respect to \( \mathbf{w} \).

The gradient \( \nabla L(\mathbf{w}) \) can be computed as:

\[
\nabla L(\mathbf{w}) = \sum_{i=1}^{n} \left( x_i \left( y_i - \frac{1}{1 + e^{-\mathbf{w}^T \mathbf{x}_i}} \right) \right)
\]

### Regularized Version

To prevent overfitting, we can add a regularization term to the loss function:

\[
L(\mathbf{w}) = \sum_{i=1}^{n} \left[ y_i \log \left( \frac{1}{1 + e^{-\mathbf{w}^T \mathbf{x}_i}} \right) + (1 - y_i) \log \left( 1 - \frac{1}{1 + e^{-\mathbf{w}^T \mathbf{x}_i}} \right) \right] + \frac{\lambda}{2} \|\mathbf{w}\|^2
\]

Where:
- \( \lambda \) is the regularization parameter.
- \( \|\mathbf{w}\|^2 \) is the squared Euclidean norm of the weight vector.

This regularized version helps in controlling the complexity of the model by penalizing large values of the weights.
```