# Gaussian Naive Bayes

$$\text{Data}: \{(x_1,y_1),\dots,(x_n,y_n)\}, \quad x_i\in\mathbb{R}^d, \; y_i\in\{0,1\}$$

**Goal:** Come up with a generative model when your features are real numbers.

## The Generative Story

[Diagram: A box $p$ branches to $y=1$ and $y=0$, each producing an elliptical Gaussian contour cloud centered at $\mu_1$ (green) and $\mu_0$ (red) respectively, both with the same tilt/shape.]

$$x/y=1 \sim N(\mu_1,\Sigma) \qquad x/y=0 \sim N(\mu_0,\Sigma)$$

covariances are the same

**Parameters:** $\{p\}, \{\mu_0,\mu_1\}, \{\Sigma\}$

---

## Maximum Likelihood Estimates

$$\hat{p} = \frac{1}{n}\sum_{i=1}^{n}y_i \leftarrow \text{Fraction of points labelled as 1}$$

$$\hat{\mu}_k = \frac{\sum_{i=1}^{n}\mathbb{1}(y_i=k)\cdot x_i}{\sum_{i=1}^{n}\mathbb{1}(y_i=k)} \leftarrow \text{sample mean of data points labelled } k$$
