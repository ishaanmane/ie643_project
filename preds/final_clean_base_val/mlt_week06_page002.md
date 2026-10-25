```markdown
# Cross-validation for minimizing MSE

The trace of $(XX^T)^{-1}$ is also the sum of the diagonal entries or the sum of the eigenvalues of the matrix.

Let the eigenvalues of $XX^T$ be $\{\lambda_1, \ldots, \lambda_d\}$. Therefore, the eigenvalues of $(XX^T)^{-1}$ are $\{\frac{1}{\lambda_1}, \ldots, \frac{1}{\lambda_d}\}$.

Mean Squared Error ($\hat{\omega}_{ML}$) = $E[\|\hat{\omega}_{ML} - \omega\|^2]$

= $\sigma^2 \sum_{i=1}^{d} \frac{1}{\lambda_i}$

For some matrix $A$, let the eigenvalues be $\{\lambda_1, \ldots, \lambda_d\}$. Then what are the eigenvalues of $(A + \lambda I)$? They are $\{\lambda_1 + \lambda, \ldots, \lambda_d + \lambda\}$.

$\in \mathbb{R}_{+ve}$

$\in \mathbb{R}^{d \times d}$

$\text{trace}\left((XX^T + \lambda I)^{-1}\right) = \left(\sum_{i=1}^{d} \frac{1}{\lambda_i + \lambda}\right)$

We want to decrease MSE by reducing the value of trace. How do we find this $\lambda \in \mathbb{R}_+$?

By the method of cross validation.

[Diagram: Training set and Validation set]

Week 6 Page 2
```