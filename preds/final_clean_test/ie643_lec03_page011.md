## Linear separability assumption:

$$D = \{(x^t, y^t)\}_{t=1,2,\dots} \quad (x^t \in \mathbb{R}^d, y^t \in \{+1,-1\})$$

is called linearly separable if there exists a non-zero $\underline{w^*} \in \mathbb{R}^d$ and $\gamma > 0$ such that:

$$y^t \leq w^*, x^t \geq \gamma \implies \langle w^*, x^t \rangle > \gamma \text{ if } y^t = +1$$
$$\langle w^*, x^t \rangle < -\gamma \text{ if } y^t = -1$$