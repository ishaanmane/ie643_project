$$e: Y \times Y \rightarrow [0, \infty)$$

$$e(y^i, \hat{y}^i), \quad y_i == \hat{y}_i \rightarrow 0$$

true label $\quad \text{MLP}(x^i) \quad y_i \neq \hat{y}_i$

**Error/loss** accumulated over all $N$ training samples:

$$\min_{\text{weights}} \sum_{i=1}^{N} e(y^i, \hat{y}^i)$$

$\rightarrow$ objective of training a MLP
