Convergence of perceptron in the presence of potentially infinite samples
$\rightarrow$ no weight change after some finite rounds.

## Linear Separability Assumption

$$D = \{(x^i, y^i)\}_{i=1,2,3,\dots}, \quad x^i \in \mathbb{R}^d, y^i \in \{+1,-1\}$$

Then $D$ is **linearly separable** if there exist a non-zero $w^* \in \mathbb{R}^d$ and a scalar $\gamma > 0$ s.t.

$$\langle w^*, x^t \rangle > \gamma \text{ if } y^t = +1$$
$$\langle w^*, x^t \rangle < -\gamma \text{ if } y^t = -1$$
$$y^t \langle w^*, x^t \rangle > \gamma$$
