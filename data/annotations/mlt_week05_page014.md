# Probabilistic View of Linear Regression

$$\{(x_1,y_1),\dots(x_n,y_n)\}$$
$$y/x \sim w^Tx + \epsilon \leftarrow \text{noise } [N(0,\sigma^2)]$$
↳ unknown but fixed $\in \mathbb{R}^d$

- We can now view this whole thing as an estimation problem.
- We will try to estimate the parameter 'w' using "Maximum Likelihood"

$$L(w; x_1,\dots,x_n; y_1,\dots,y_n) = \prod_{i=1}^{n} e^{-\frac{(w^Tx_i-y_i)^2}{2\sigma^2}} \cdot \frac{1}{\sigma\sqrt{2\pi}}$$

$$\log L(w;\dots) = \sum_{i=1}^{n} -\frac{(w^Tx_i-y_i)^2}{2\sigma^2} \cdot \frac{1}{\sigma\sqrt{2\pi}} \quad \text{irrelevant as these are constants}$$

$$\max_w \sum_{i=1}^{n}-(w^Tx_i-y_i)^2 \quad \text{or} \quad \min_w \sum_{i=1}^{n}(w^Tx_i-y_i)^2$$

we've encountered this before. This is the exact linear regression problem with squared error
