$$\min x^TQx + c^Tx \quad 0\leq x_i\leq1 \rightarrow \text{Noninteger}$$

$\hookrightarrow$ introduce IN variables

$$\min \sum Q_{12}x_{12}+\sum Q_{ii}y_i+\sum c_ix_i$$
$$x_{12}=x_1x_2 \; \forall i$$
$$y_i=x_i^2 \; \forall i$$
$$0\leq x_i\leq1$$

$\rightarrow$ in case of only boolean $x\in\{0,1\}$ — Padberg triangle inequality

$$\min \sum Q_{12}x_{12}+\sum c_ix_i$$
st $\quad x_{12}=x_1x_2$
$\qquad x_i\in\{0,1\}\;\forall i$

$\hookrightarrow$ convex hull of $\emptyset$ is same as convex hull of $x_{12}=x_1x_2$, $0\leq x_i\leq1$

Result by Burun and Letchford.