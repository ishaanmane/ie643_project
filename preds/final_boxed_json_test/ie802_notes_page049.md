$$\min x^TQx + c^Tx \quad 0\leq x_i\leq1 \rightarrow \text{Noninteger}$$

$\hookrightarrow$ Introduce $y$ variables

$$\min \sum Q_{ij}x_ix_j + \sum Q_{ii}y_i + \sum c_ix_i$$

$$x_{ij}=x_1x_2 \; \forall ij, \qquad y_1=x_1^2 \; \forall i$$
$$0\leq x_i\leq1$$

$\hookrightarrow$ In case of only boolean $x \in \{0,1\}$, pads using triangle inequalities.

$$\min \sum Q_{ij}x_ix_j + \sum c_ix_i$$
st $x_{ij}=x_1x_2$
$$x_i \in \{0,1\} \; \forall i$$

convex hull of $\rightarrow$ is same as convex hull of $x_{ij}=x_1x_2$, $0\leq x_i^*\leq1$

Result by Burer and Letchford.