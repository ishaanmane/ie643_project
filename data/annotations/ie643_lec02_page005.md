## Dataset Definition

$$D = \{(x^i, y^i)\}_{i=1}^{N}, \quad y^i \in \mathbb{R}$$

$$x^i \in \mathbb{R}^d = X$$

$y^i$ (label encodings):

- $y^i \in \{+1, -1\}$
- $y^i \in \{0, 1\}$
- $y^i \in \{1, 2, 3, \dots, K\}$

> $x^i$: email object in a suitable **feature space**

$$x^i = \begin{bmatrix} x_1^i \\ x_2^i \\ \vdots \\ x_d^i \end{bmatrix}$$

- $x_1^i \rightarrow$ to_multiple (**attribute**)
- $x_d^i \rightarrow$ num_chars
