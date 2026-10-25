## Supervised learning

$$D = \{(x^i, y^i)\}_{i=1}^{N}$$

$$X \ni x^i \in \mathbb{R}^q$$
$$Y \ni y^i \in \{+1, -1\}$$

$$h: X \rightarrow Y$$

MLP weights

train a multilayered perceptron to find $h_{\text{MLP}}$

$$\min E = \sum_{i=1}^{N} e(y^i, \hat{y}^i)$$

[Diagram: A bowl-shaped error function curve with a local minimum marked at a point $(w_1, w_2)$ — "NP-hard."]

local minimum

minimization is over weights of MLP