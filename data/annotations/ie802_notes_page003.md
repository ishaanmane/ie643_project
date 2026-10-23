19/02/26

**Automatic Reformulation.**
$$\text{model-M} \; \downarrow \; \text{Reformulate} \; \text{model-}\hat{m}$$

**Perspective Reformulation -**
Motivation from linear models: e.g. model this relation (ex-Factory problem)

① $y_1=0 \Rightarrow x_1=0$
&nbsp;&nbsp;$y_1=1 \Rightarrow x_1\in[0,5]$

**Soln:** $0\leq x_1, \; x_1\leq5y_1 \;\; ***, \quad y_1\in\{0,1\}, \; x_1\in\mathbb{R}$

[Diagram: A 2D region ($x_1,x_2$ axes) — a shaded triangular wedge above a line from origin, with point $y_1=0,x_1=0,x_2=0$ marked at origin, illustrating the disjunctive feasible region.]

ex.② $y_1=0 \Rightarrow x_1=0$ and $x_2=0$
$\left.\begin{array}{l}y_1=1 \Rightarrow 3x_1+x_2\geq10\\-10\leq x_1\leq10\\-10\leq x_2\leq10\end{array}\right\}$ Disjunctive Programming

**Soln:**
$$-10y_1\leq x_1\leq10y_1$$
$$-10y_1\leq x_2\leq10y_1$$
$$\boxed{M(1-y_1)+3x_1+x_2\geq10} \leftarrow \text{very Big number} \approx1000$$
$$\boxed{y_1(3x_1+x_2)\geq10y_1} \to \text{Non-linear}$$

[Diagram: A shaded triangular region in $(y_1,x_1)$ space, "Tight LP relaxation" ***, followed by two more sketches of shaded triangular/quadrilateral relaxation regions, and a box: weaker LP relaxation — $-M\leq x_1$, $x_1\leq10y_1$, $y_1\in\{0,1\}$, $x_1\in[0,5]$ → we have to solve branches, "c(hoos)e M big".]

**model-①**: $x_1^2+x_2^2\leq100$, $-10y_1\leq x_1\leq10y_1$, $-10y_1\leq x_2\leq10y_1$, $y_1\in\{0,1\}$

**Ex ③**
$y_1=1 \Rightarrow \begin{cases}x_1^2+x_2^2\leq100\\-10\leq x_1,x_2\leq10\end{cases}$
$y_1=0 \Rightarrow x_1=x_2=0$
