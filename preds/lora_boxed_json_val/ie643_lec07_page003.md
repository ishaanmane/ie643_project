## Supervised learning

$$D = \{(x^i, y^i)\}_{i=1}^{N}, \quad x^i \ni x^i \in \mathbb{R}^q, \quad y^i \ni y^i \in \{+1,-1\}$$

$$h: X \rightarrow Y, \quad h \text{ MLP weights}$$

train a multilayered perceptron to find $h_{MLP}$

$$\min E = \sum_{i=1}^{N} e(y^i, \hat{y}^i)$$

[Diagram: A wavy error curve vs weight plot with a local minimum marked at a point $(w_1, w_2)$, labeled "NP-hard."]

local minimum
minimization is over weights of MLP