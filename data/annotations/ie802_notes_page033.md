If we have some linear constraints
$$\min x^TQ_0x+a_0^Tx$$
$$l\leq x\leq u \to n \text{ dimension}$$
$$\{Gx\leq b\} \to k \text{ dimension}$$

$$(h_1-g_1^Tx)\geq0$$
$$(x_1-l_1)\geq0$$
$$-h_1l_1-x_1g_1^Tx+h_1x_1+l_1g_1^Tx\geq0$$
&nbsp;&nbsp;&nbsp;&nbsp;→ quadratic so rewrite as
$$x_1\sum g_{1j}x_j$$
$$=\sum g_{1j}x_{1j} \qquad x_{12}\geq(u_1u_2-x_1u_2-x_2u_1)$$

We can do lot of these,
$$3x_{12}-x_{23}+p\cdot x\leq s_1$$
$$3(x_1u_2+x_2u_1-u_1u_2)-(\cdots)+p\cdot x\leq s_1$$

We can multiply again with other constraints and do one more round of RLT
$$(x_{12}+u_1u_2-x_1u_2-x_2u_1\geq0)$$
$$x_3-l_3\geq0$$
$$x_{12}\cdot x_3 = x_{1,2,3}$$

More RLT more cutting. But we don't know will it converge. But we know it will make tighter.

- It was used initially for binary variables

$$\min c^Tx$$
$$Ax\leq b$$
$$x\in\{0,1\}^n$$

$$x_1+5x_2+x_3\leq1$$
$$x_1\geq0$$

→ $x_1(x_1+5x_2+x_3-1)\leq0$
$$x_{11}+5x_{12}+x_{13}-x_1\leq0$$
$$x_{12}\leq x_1$$
$$x_{12}\leq x_2$$
$$x_{12}\geq x_1+x_2-1$$

- multiply constraints with each other
- new model has lot of constraints
- No need of branch and bound, but in binary case we can get convex hull.
