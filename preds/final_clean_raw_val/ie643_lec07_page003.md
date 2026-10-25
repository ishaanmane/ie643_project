## Supervised learning

$$D = \{(x^i,y^i)\}_{i=1}^{N}$$
$$x \ni x^i \in \mathbb{R}^d$$
$$y \ni y^i \in \{+1,-1\}$$

$h$: MLP weights $\quad X \rightarrow Y$

train a multilayered perceptron to find $h_{MLP}$

$$\min E = \sum_{i=1}^{N} e(y^i,\hat{y}^i)$$

[Diagram: A wavy error vs weight curve with a local minimum marked at $w_1$, $w_2$, labeled "NP-hard" and "local minimum".]

minimization is over **weights of MLP**