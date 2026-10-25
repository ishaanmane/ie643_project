only convex for $g(x)$ is concave

[Diagram: A shaded region with a cut through it, illustrating the idea of traveling 2 sides of a corner point and cutting all the edge of infeasible region then draw a cut.]

Not a valid cut as it cuts feasible set [egon holes]

- This works for high dim.
  - 3D $\rightarrow$ 2 constraints $\rightarrow$ move 3 direction to find points $\rightarrow$ draw hyperplane that intersect & plane
  - N dim $\rightarrow$ N direction $\rightarrow$ N points provided constraint is concave if work

$$x^TQ'x\leq b_1 \quad \text{if } Q \text{ is PD it is convex}$$
$$\quad \text{if } Q \text{ is ND} \rightarrow \text{conex}$$

If neither P or ND

**DCP:** $x^T(Q'^+-Q'^-)\eta\leq b_1$
$\downarrow$ diff of convex fn

in $\quad$ ND

also as,
$$x^TQ'^+\eta-w\leq b_1 \rightarrow \text{convex}$$
concave, $\quad w-x^TQ'^-\eta\leq0$

Tangent $\rightarrow$ convex
Intersection point $\rightarrow$ concave

In practical using simplex of intersection point $\rightarrow$ canon plane $\Rightarrow$ many solvers do not use it unless $Q\rightarrow$ diagonal..