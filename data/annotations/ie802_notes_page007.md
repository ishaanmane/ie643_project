**Transform the constraint.**

min $x_1+2x_2+3x_3-x_4$

$w_1=x_1^2$, $w_2=x_2^2$, $w_3=x_3^2$, $w_4=x_4^2$, $w_5=x_5^2$

$$w_1+w_2-w_3-w_4+w_5=7$$
$$3x_2+x_3-x_4+3x_5=1$$
$$0\leq x_i\leq10, \; i=1,2\dots5$$

[Diagram: A bowl-shaped curve $w_1$ vs $x_1$ (parabola $w_1=x_1^2$), with the region between the curve and its chord from $(0,0)$ to $(10,100)$ shaded — "relaxation" — labeled "equation of line".]

Relaxation: $x_1^2\leq w_1$, $0\leq x_1\leq10$, $\text{i}=1,2\dots5$; $w_2\geq x_2^2$, $0\leq x_2\leq10$, adds 5 times.

[Diagram: A large irregular blob shape labeled $S$ with a smooth convex-hull outline around it, both shaded.]
