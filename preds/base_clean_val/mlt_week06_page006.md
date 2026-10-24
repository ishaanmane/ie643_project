```markdown
# Ridge Regression

The objective of Ridge Regression is to find the optimal weights $\hat{\omega}_R$ that minimize the sum of the loss function and a regularization term.

$$
\hat{\omega}_R = \arg\min_{\omega} \left( \sum_{i=1}^{n} (\omega^T x_i - y_i)^2 + \lambda ||\omega||^2 \right)
$$

- **Loss**: The first part of the equation represents the loss function, which measures the discrepancy between the predicted values ($\omega^T x_i$) and the actual values ($y_i$).
- **Regularizer**: The second part, $\lambda ||\omega||^2$, is the regularization term. It penalizes large values of $\omega$ to prevent overfitting by shrinking the coefficients towards zero.

This formulation balances fitting the data well (loss minimization) with keeping the model simple (regularization).

[Diagram: Flowchart showing the optimization process from data input to the final optimized weights $\hat{\omega}_R$.]
```