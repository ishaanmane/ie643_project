$$x_1^2+x_2^2\leq100y_1$$
$$-10y_1\leq x_1\leq10y_1, \quad \text{tighter}$$
$$-10y_1\leq x_2\leq10y_1$$
$$y_1\in\{0,1\}$$

Relaxation 2 $\leq$ Relaxation-1

- When $y_1\in\{0,1\}$ → Model 1 and model 2 have same feasible region
- When $0\leq y_1\leq1$ then are they same? (Variable)

$y_1=1/2 \Rightarrow x_1=?, x_2=?$

③ $x_1^2+x_2^2\leq100y_1^2$ → strictly tighter → but no more convex
$\vdots$
$y_1=1/2$, $x_1=5$, $x_2=5$ → Not in relaxation③

④ $\sqrt{x_1^2+x_2^2}\leq10y_1$ ← convex; not allowed b/c $y_1\in\{0,1\}$ always $+ve$

→ No derivative @ (0,0) problem

**Defn:** Let $g(x_1,x_2,x_3\dots x_n)$ be a convex function. Then its perspective is defined as the fn:
$$\bar{g}(x_1,x_2\dots x_n,t) = \begin{cases}tg\left(\frac{x_1}{t},\frac{x_2}{t},\dots,\frac{x_n}{t}\right) & \text{when } t\neq0\\0 & \text{when } t=0\end{cases}$$

**Use:** Given constraint $g(x_1,x_2,x_3\dots x_n)\leq0$; tighten it to $y_1g\left(\frac{x_1}{y_1},\frac{x_2}{y_1}\dots\frac{x_n}{y_1}\right)\leq0$

$$y_1l_i \leq x_i \leq y_1u_i \quad l_i\leq x_2\leq u_2y_1$$

[Diagram: A pentagon-like directed graph with 5 nodes labeled ①-⑤ connected by arrows, illustrating some kind of network/ordering relation, faint and undecipherable in detail.]
