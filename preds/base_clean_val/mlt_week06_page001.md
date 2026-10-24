```markdown
# Goodness of Maximum Likelihood Estimator for Linear Regression

We observed that $\hat{w}^* = \hat{w}_{ML}$ when noise follows zero mean Gaussian distribution.

Now we want a way to understand how good $\hat{w}_{ML}$ is in estimating $w$.

$$
\begin{aligned}
&= E\left[\|\hat{w}_{ML} - w\|^2\right] \\
&= \sigma^2 \cdot \text{trace}\left[(X X^T)^+\right]
\end{aligned}
$$

- The goodness of the estimator is not just by the noise but by how the features are related to each other.
- We cannot touch $\sigma^2$ as it is given but we definitely can fool around with the features to get a better estimator with lesser mean squared error.
```