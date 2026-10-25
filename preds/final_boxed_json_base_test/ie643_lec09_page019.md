```markdown
# Partial Derivatives and Residuals

The handwritten notes appear to be discussing partial derivatives and residuals in the context of a linear regression model.

## Partial Derivatives

The left-hand side of the equation represents the partial derivatives of the error function \( e \) with respect to each parameter \( a_i \):

\[
\frac{\partial e}{\partial a_1}, \quad \frac{\partial e}{\partial a_2}, \quad \ldots, \quad \frac{\partial e}{\partial a_c}
\]

These partial derivatives are summed up:

\[
\sum_{i=1}^{c} \frac{\partial e}{\partial a_i}
\]

## Residuals

The right-hand side of the equation represents the residuals:

\[
\hat{y}_1 - y_1, \quad \hat{y}_2 - y_2, \quad \ldots, \quad \hat{y}_c - y_c
\]

This suggests that the partial derivatives of the error function with respect to the parameters are equal to the residuals.

## Summary

The equation indicates that the sum of the partial derivatives of the error function with respect to the parameters equals the vector of residuals:
\[
\sum_{i=1}^{c} \frac{\partial e}{\partial a_i} = \begin{bmatrix} \hat{y}_1 - y_1 \\ \hat{y}_2 - y_2 \\ \vdots \\ \hat{y}_c - y_c \end{bmatrix}
\]
```