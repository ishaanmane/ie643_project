23-03-26

$$x\in\mathbb{R}^{n\times n} \text{ - variable}$$
$$\min \langle c,X\rangle = \sum\sum c_{ij}x_{ij}$$
$$\text{st } \langle A_i,X\rangle\leq b_i, \; i=1,2\dots m$$
$$\boxed{X\geq0} \leftarrow \text{convex constraint (+ve SD)}$$

[Diagram: 3D axes $x_1,x_2,x_3$ with a shaded wedge region labeled "Ice-cream cone, 2nd order cone in 3D".]

**equation:** $\sqrt{x_2^2+x_3^2}\leq x_1$, $x_1\geq0$

$$S=\{x\in\mathbb{R}^3: x_1\geq\sqrt{x_2^2+x_3^2}, \; x_1\geq0\}$$

If $\hat{x}\in S$, then $\lambda\hat{x}\in S \; \forall\lambda\geq0$

**QCQP** (Quadratic Constrained Quadratic Progs)
$$\min x^TQ_0x+a_0^Tx$$
(P) st $\boxed{x^TQ_1x+a_1^Tx\leq b_1}$
$$x^TQ_2x+a_2^Tx\leq b_2$$
$$\vdots$$
$$x^TQ_mx+a_m^Tx\leq b_m$$
$$l\leq x\leq u$$

① * If $Q_0,Q_1\dots Q_m$ are PSD then (P) is convex
* If not → do bnb, relaxation, cutting etc...

② The constraint [box]
*
