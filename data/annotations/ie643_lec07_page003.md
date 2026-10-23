**Supervised learning:** $D = \{(x^i, y^i)\}_{i=1}^{N}$

$$X \ni x^i \in \mathbb{R}^d$$
$$Y \ni y^i \in \{+1, -1\}$$

$h: X \rightarrow Y$, MLP weights

train a multilayered perceptron to find $h_{MLP}$

$$\min E = \sum_{i=1}^{N} e(y^i, \hat{y}^i)$$

minimization is over weights of MLP.

[Diagram: A wavy error-surface plot over axes $w_1, w_2$ with a marked local minimum.]

**local minimum**, **NP-hard.**
