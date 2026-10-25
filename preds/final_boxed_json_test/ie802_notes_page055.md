## Local Branchings (Improvement)

Let $(\hat{x}, \hat{y})$ be a known solution

$$y \in \mathbb{Z}_{\geq 0}??$$

[Diagram: A tree — root splits into two children, each child splits further, one branch ends at $y=6$, labeled "not useful", with cardinality constraint $\sum_{i=1}^{p}|x_i-\hat{x}_i| \leq 5$.]

**P:** cardinality constraint

**G:** not useful

**LOCAL JUMP:** | **Idiot Crash:**
------------------|----------------------
$\min \quad Ax \leq b$ &nbsp;&nbsp;&nbsp;&nbsp; $y \in \mathbb{Z}^p$
$\min \sum w^i(y_i - a_i y)^+$

Solving LPs takes too long.

Initial construction:
$$2y_1+y_2-y_3 \leq 7 \rightarrow y_1 \text{ should be small}$$
$$-y_1+2y_2+y_3 \geq 9 \rightarrow y_1 \text{ should be small}$$
$$y_2+y_3+y_4 = 5$$
$$y_3-y_4+y_6 \leq 8$$
$$0 \leq y \leq 10$$

set $y=0$