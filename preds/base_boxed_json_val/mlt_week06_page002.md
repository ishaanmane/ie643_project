```markdown
# Cross-validation for minimizing MSE

## Trace of $(XX^T)^{-1}$

The trace of $(XX^T)^{-1}$ is also the sum of its diagonal entries or the sum of its eigenvalues.

### Eigenvalues of $XX^T$

Let the eigenvalues of $XX^T$ be $\{\lambda_1, \ldots, \lambda_d\}$.

Then the eigenvalues of $(XX^T)^{-1}$ are $\{\frac{1}{\lambda_1}, \ldots, \frac{1}{\lambda_d}\}$.

### Mean Squared Error ($\hat{\omega}_{ML}$)

Mean Squared Error ($\hat{\omega}_{ML}$) = $E\left[\|\hat{\omega}_{ML} - \omega\|^2\right]$

= $\sigma^2 \sum_{i=1}^{d} \frac{1}{\lambda_i}$

## Eigenvalues of $(A + \lambda I)$

For some matrix $A$, let eigenvalues be $\{\lambda_1, \ldots, \lambda_d\}$.

Then what are the eigenvalues of $(A + \lambda I)$? = $\{\lambda_1 + \lambda, \ldots, \lambda_d + \lambda\}$

## Trace of $(XX^T + \lambda I)^{-1}$

$\operatorname{trace}\left((XX^T + \lambda I)^{-1}\right) = \left(\sum_{i=1}^{d} \frac{1}{\lambda_i + \lambda}\right)$

## Reducing MSE by reducing trace

We want to decrease MSE by reducing the value of trace. How do we find this $\lambda \in \mathbb{R}_+$?

By the method of cross validation.

## Training Set and Validation Set

[Diagram: Training set and validation set]

Week 6 Page 2
```