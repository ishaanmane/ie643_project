# Goodness of Maximum Likelihood Estimator for Linear Regression

We observed that $w^* = \hat{w}_{ML}^{(XX^T)^+XY}$ when noise follows zero mean Gaussian distribution.

Now we want a way to understand how good $\hat{w}_{ML}$ is in estimating $w$.

$$= E\left[\|\hat{w}_{ML}-w\|^2\right] \quad \text{(Expected value of the norm of estimator & $w\in\mathbb{R}^d$, over randomness in $y$)}$$
$$= \sigma^2 \cdot \text{trace}\left[(XX^T)^+\right]$$

$\rightarrow$ The goodness of the estimator is not just by the noise but by how the features are related to each other.
$\rightarrow$ We cannot touch $\sigma^2$ as it is given but we def. can fool around with the features to get a better estimator with lesser mean squared error.