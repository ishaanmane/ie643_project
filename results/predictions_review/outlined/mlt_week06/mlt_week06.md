---
title: "MLT Week 6"
geometry: margin=2cm
papersize: letter
fontsize: 11pt
mainfont: DejaVu Serif
header-includes:
  - \usepackage{float}
  - \floatplacement{figure}{H}
  - \usepackage{fvextra}
  - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,breakanywhere,commandchars=\\\{\}}
---


<!-- page: mlt_week06_page001 -->

# Goodness of Maximum Likelihood Estimator for Linear Regression

We observed that $w^* = \hat{w}_{ML}^{(XX^T)^+XY}$ when noise follows zero mean Gaussian distribution.

Now we want a way to understand how good $\hat{w}_{ML}$ is in estimating $w$.


```latex
= E\left[\|\hat{w}_{ML}-w\|^2\right] \quad \text{(Expected value of the norm of estimator & $w\in\mathbb{R}^d$, over randomness in $y$)}
```

*Warning: equation could not be typeset; shown as written.*

$$= \sigma^2 \cdot \text{trace}\left[(XX^T)^+\right]$$

$\rightarrow$ The goodness of the estimator is not just by the noise but by how the features are related to each other.
$\rightarrow$ We cannot touch $\sigma^2$ as it is given but we def. can fool around with the features to get a better estimator with lesser mean squared error.

<!-- page: mlt_week06_page002 -->

# Cross-validation for minimizing MSE

$$\text{trace}[(XX^T)^{-1}] \quad [\text{sum of diagonal entries}] \quad \text{also} \; [\text{sum of eigenvalues of matrix}]$$

Let the Eigenvalues of $XX^T$ be $\{\lambda_1,\dots,\lambda_d\}$

$\therefore$ Eigenvalues of $(XX^T)^{-1}: \{\frac{1}{\lambda_1},\dots,\frac{1}{\lambda_d}\}$

Mean Squared Error ($\hat{w}_{ML}$) = $E[\|\hat{w}_{ML}-w\|^2]$
= $\sigma^2 \sum_{i=1}^{d} \frac{1}{\lambda_i}$

For some matrix $A$, let eigenvalues be $\{\lambda_1,\dots,\lambda_d\}$

Then what are the eigenvalues of $(A+\lambda I)$? = $\{(A_1+\lambda),\dots,(A_d+\lambda)\}$

$$\in \mathbb{R}_{+ve}, \qquad \in \mathbb{R}_d^{d\times d}$$

$$\text{trace}(XX^T+\lambda I)^{-1} = \left(\sum_{i=1}^{d} \frac{1}{\lambda_i+\lambda}\right)$$

We want to decrease MSE by reducing the value of trace. How do we find this $\lambda \in \mathbb{R}_+$?

By the method of cross validation

![A horizontal line divided into two parts labeled "training set" (left) and "validation set" (right).](figures/mlt_week06_page002_b11.png){width=55.0000%}

<!-- page: mlt_week06_page003 -->

# Training Set vs Validation Set

- Train on training set & check for errors on validation set
- Pick $\lambda$ which gives least error

How to decide the best way to divide the data?

**K-fold cross validation**

*[Diagram: A row of boxes labeled $F_1, F_2, \dots, F_k$, each representing a fold.]*

- Train on folds = $\{f_1, \dots f_{i-1}, f_{i+1}, \dots, f_k\}$
- Validate on $f_i$
- Pick $\lambda$ which gives least avg error

---

$$\hat{w}_{new} = (XX^T + \lambda I)^{-1}Xy$$

<!-- page: mlt_week06_page004 -->

# Bayesian Modeling for linear regression

- Need a prior on $w$, i.e., $P(w) \in \mathbb{R}^d$

Likelihood: $y/x \sim N(w^Tx, 1)$ (for simplicity, can use $\sigma^2$ as well)

A choice of priors: $w \sim N(0, \sigma^2 I)$ — covariance matrix $\begin{bmatrix}\sigma^2 & & \\ & \ddots & \\ & & \sigma^2\end{bmatrix}$

We know,
$$P[w/\{(x_1,y_1),\dots,(x_n,y_n)\}] \propto P[(x_1,y_1),\dots,(x_n,y_n)/w] \cdot P(w)$$
$$\propto \left[\prod_{i=1}^{n} e^{-\frac{(y_i-w^Tx_i)^2}{2}}\right] \left[\prod_{i=1}^{d} e^{-\frac{(w_i-\theta)^2}{2\sigma^2}}\right]$$
$$\propto \left[\prod_{i=1}^{n} e^{-\frac{(y_i-w^Tx_i)^2}{2}}\right] e^{-\frac{1}{2\sigma^2}\left(\sum_{i=1}^{d} w_i^2\right)} = e^{-\frac{\|w\|^2}{2\sigma^2}}$$

$$\hat{w}_{MAP} = \max_w \sum_{i=1}^{n} -\frac{(y_i-w^Tx_i)^2}{2} - \frac{\|w\|^2}{2\sigma^2}$$
$$= \min_w \sum_{i=1}^{n} \frac{(y_i-w^Tx_i)^2}{2} + \frac{\|w\|^2}{2\sigma^2} \quad f(w)$$

Take gradient, set it to 0 & solve for $\hat{w}_{MAP}$

<!-- page: mlt_week06_page005 -->

$$\nabla f(w) = (XX^T)w - XY + \frac{w}{\sigma^2}$$

$$\min_{w} w - \left[XX^T + \frac{\sigma^2 I}{\sigma^2}\right]^{-1}XY$$

<!-- page: mlt_week06_page006 -->

# Ridge Regression

$$\hat{w}_R = \arg_{w} \min_{l> \text{Ridge}} \sum_{i=1}^{n}(w^Tx_i-y_i)^2 + \lambda \|w\|^2$$

Loss $\quad$ Regularizer
