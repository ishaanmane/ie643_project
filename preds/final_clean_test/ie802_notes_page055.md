## Local Branching (Improvement)

Let $(\hat{x}, \hat{y})$ be a known solution, $\hat{y} \in \mathbb{Z}^{n_1}$

[Diagram: A branching tree — root splits into two children, each of which splits further, one branch ending at a node labeled "not useful" with $y=6$, violating cardinality constraint.]

$$p \sum_{i=1}^{n_1} y_i - \hat{y}_1 \leq 5 \quad \text{(cardinality constraint)}$$

**LOCAL JUMP:** Solving LPs takes too long.

**Idiot Crash:**

$$\min c^T x, Ax \leq b, x \in \mathbb{Z}^p$$

$$\min \sum w_i(b_i - a_i y)^+$$

**Initial Construction:**

$$2y_1 + y_2 - y_3 \leq 7 \rightarrow y_1 \text{ should be small}$$
$$-y_1 + 2y_2 + y_3 \geq 9 \rightarrow y_1 \text{ should be small}$$

$$y_2 + y_0 + y_4 = 5$$
$$y_3 - y_4 + y_6 \leq 8$$
$$0 \leq y \leq 10$$

set $y=0$