$$e(y^i, \hat{y}^i) = KL(y^i, \hat{y}^i)$$

$KL = 0$ when $y^i \equiv \hat{y}^i$
$KL > 0$ when $y^i \neq \hat{y}^i$

$$\min_{\text{weights of NN}} \sum_{i=1}^{N} KL(y^i, \hat{y}^i)$$

$$\min_{\text{weights}} \sum_{i=1}^{N} CE(y^i, \hat{y}^i)$$

[Diagram: Arrows connecting "logistic regression" to $\mathbb{E}[y|X=\vec{x}]$ and "Bernoulli r.v" and "likelihood".]
