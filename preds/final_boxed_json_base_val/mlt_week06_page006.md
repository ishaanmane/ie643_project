```markdown
# Ridge Regression

$\hat{\omega}_{R} = \arg\min_{w} \sum_{i=1}^{n} (\omega^T x_i - y_i)^2 + \lambda ||\omega||^2$

## Loss
## Regularizer
```

The equation is presented as:

$\hat{\omega}_{R} = \arg\min_{w} \sum_{i=1}^{n} (\omega^T x_i - y_i)^2 + \lambda ||\omega||^2$

Where:
- $\hat{\omega}_{R}$ represents the optimal weight vector for Ridge Regression.
- The loss function is the sum of squared errors between the predicted values ($\omega^T x_i$) and the actual values ($y_i$).
- The regularizer term $\lambda ||\omega||^2$ penalizes large weights to prevent overfitting.

The page footer indicates "Week 6 Page 6".