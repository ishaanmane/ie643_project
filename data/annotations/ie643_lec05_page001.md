**Recap:**

[Diagram: A scatter of "+" and "−" points separated by a line, illustrating linear separability.]

## Linear Separability Assumption

$$D = \{(x^i, y^i)\}_{i=1,2,3,\dots}, \quad x^i \in \mathbb{R}^d, y^i \in \{+1,-1\}$$

there exists $w^* \in \mathbb{R}^d$ (non-zero), $\exists \, \gamma \in \mathbb{R}$

s.t. $\langle w^*, x^t \rangle > \gamma$ if $y^t = +1$
$\langle w^*, x^t \rangle < -\gamma$ if $y^t = -1$, $t = 1,2,3,\dots$

$$y^t \langle w^*, x^t \rangle > \gamma$$
