**DC Formulations** → difference of convex formulations

If $Q$ is big and non-convex → we can't solve

**RLT** (bounds play big role)

General QCQP: $\min x^TQ_0x+a_0^Tx$
$$x^TQ_1x+a_1^Tx\leq b_1$$
$$\vdots$$
$$x^TQ_mx+a_m^Tx\leq b_m$$
$$l\leq x\leq u$$

We use: $X_{n\times n}=xx^T$, $x_{11}=x_1^2$, $x_{12}=x_1x_2$, $\vdots$, $x_{ij}=x_ix_j$ → relax b/b drawing boxes

This becomes $\min\langle Q_0,X\rangle+a_0^Tx$ → next page

**Bilinear Part:** $x_{12}=x_1x_2$
Bound factors → $\{l_1\leq x_1\leq u_1, \; l_2\leq x_2\leq u_2$

$$(x_1-l_1)\geq0$$
$$(x_2-l_2)\geq0$$
&nbsp;&nbsp;&nbsp;&nbsp; multiple: $(x_1-l_1)(x_2-l_2)\geq0$
$$x_1x_2\colon x_{12}+l_1l_2-x_1l_2-x_2l_1\geq0 \to \text{linear constraint}$$

Using $(u_1-x_1)\geq0$, $(u_2-x_2)\geq0$: $x_{12}+u_1u_2-x_1u_2-x_2u_1\geq0$ → called McCormick inequalities

Relaxation of linear:

try: $x_{11}=x_1^2$
$$(x_1-l_1)(x_1-l_1)\geq0$$
$$x_{11}-2l_1x_1+l_1^2\geq0$$
$$x_{11}\geq-l_1^2+2l_1x_1$$

we will set second for $(x_1-l_1)(u_1-x_1)\geq0$

[Diagram: A parabola $x_{11}=x_1^2$ shape.]
