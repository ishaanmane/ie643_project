# Goodness of Maximum Likelihood Estimator for Linear Regression

We observed that $w^* = \hat{w}_{ML} = (XX^T)^+Xy$ when noise follows zero mean Gaussian distribution.

Now we want a way to understand how good $\hat{w}_{ML}$ is in estimating $w$.

$$= E\left[\|\hat{w}_{ML}-w\|^2\right] \quad \begin{pmatrix}\text{Expected value of the norm of}\\\text{estimator \& } w\in\mathbb{R}^d\end{pmatrix} \; [\text{over randomness in } y]$$

$$= \sigma^2 \cdot \text{trace}\left[(XX^T)^+\right]$$

- The goodness of the estimator is not just by the noise but by how the features are related to each other.
- We cannot touch $\sigma^2$ as it is given but we can fool around with the features to get a better estimator with lesser mean squared error.
