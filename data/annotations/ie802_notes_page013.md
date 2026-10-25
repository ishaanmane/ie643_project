09-03-26

$$w_1=x_1^2, \; l_1\leq x_1\leq u_1$$

[Diagram: A parabola with a chord between $l_1$ and $u_1$ on the x-axis, showing the secant/tangent construction.]

$$w_1=\log x_1, \quad w_1=e^{x_1}, \quad w_1=x_1^3$$
$$\boxed{w_1=x_1\cdot x_2}$$
$$\log w_1 = \log x_1 + \log x_2$$
$$w_2=\log w_1, \quad w_4=\log x_2, \quad w_3=\log x_1$$

$$w_1=x_1\cdot x_2, \quad 0\leq x_1\leq1, \quad 0\leq x_2\leq1, \quad 0\leq w_1$$
$w_1\leq1 \to$ drop as convex; $w_1\leq x_1$; $w_1\leq x_2$ — Bilinear constraint

| $x_1$ | $x_2$ | $w_1$ |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1/2 | 0 |
| 1/2 | 1/2 | 1/4 |
| 1 | 0.8 | 0.8 |

$Z=x\cdot y$, $\{x\geq0,y\geq0\}$ → neither convex nor concave

| $x_1$ | $x_2$ | $w_1$ |
|---|---|---|
| 0 | 0 | 0 |
| 10 | 0 | 0 |
| 0 | 10 | 0 |

equation: From image, calculate plane that passes through this point $(0,1,0)$, $(1,0,0)$, $(1,1,1)$
$$w_1\geq x_1+x_2-1, \quad w_1\leq x_1, \quad w_1\leq x_2, \quad 0\leq w_1$$

New system: $1/2\leq x\leq4$: $(1/2,1/2,1/4)$, $(4,1/2,2)$, $(1/2,4,2)$
$$w_1\geq2x_1+2x_2-4$$
$$0\leq(2-x_1)(2-x_2)$$
$$4-2x_1-2x_2+x_1x_2\geq0$$
$$4-2x_1-2x_2+w_1\geq0 \to \text{linear constraint}$$

$Z=x*y \to$ trying to cover it: new: $-1\leq x_1\leq2$, $-1\leq x_2\leq2$, $-2\leq w_1\leq4$; ①$x_1\leq2$, ②$-1\leq x_1$, ③$x_2\leq2$, ④$-1\leq x_2$; ①×③ $0\leq2-x_1$, ③ $0\leq2-x_2$. Now multiply co(nstrain)ts.
