$$\min x^TQx+c^Tx$$
$$0\leq x\leq1 \longrightarrow \text{No integer}$$

→ introduce $n^2$ variables

$$\min \sum Q_{ij}x_{ij}+\sum Q_{ii}y_i+\sum c_ix_i$$
$$x_{ij}=x_ix_j \; \forall ij$$
$$y_i=x_i^2 \; \forall i$$
$$0\leq x_i\leq1$$

→ In case of only boolean $x\in\{0,1\}$

Padberg's triangle inequalities

$$\min \sum Q_{ij}x_{ij}+\sum c_ix_i$$
st $x_{ij}=x_ix_j$
$$x_i\in\{0,1\} \; \forall i$$

Convex hull of $\Phi$ is same as convex hull of $x_{ij}=x_ix_j$, $0\leq x_i\leq1$

Result by Burer and Letchford..
