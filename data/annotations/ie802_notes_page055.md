**Local Branching (Improvement)**

Let $(\hat{x},\hat{y})$ be a known solution, $y\in\{0,1\}^p$

[Diagram: A branch-and-bound tree with several nodes, one node circled and connected to two children, one labeled "$\geq6$" and marked "not useful".]

$$\sum_{i=1}^{p}|y_i-\hat{y}_i|\leq5$$

→ cardinality constraint

**Local Jump:** solving LPs takes too long
**Idiot Crash:** Initial / construction

$$\min \bcancel{c^Tx}$$
$$Ay\leq b$$
$$y\in\mathbb{Z}^p$$

$$\min \sum w_i(b_i-Ay)^+$$

$$3y_1+y_2-y_3\leq7 \to y_1 \text{ should be small}$$
$$-y_1+2y_2+y_3\geq9 \to y_1 \text{ should be small}$$
$$y_2+y_3+y_4=5$$
$$y_3-y_4+y_6\leq8$$
$$0\leq y\leq10$$

set $y_1=0$
