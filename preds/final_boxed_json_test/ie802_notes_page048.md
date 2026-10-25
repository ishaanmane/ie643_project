only convex for $\delta(x)$ is concave

[Diagram: A shaded region with a red line cutting through it, labeled "Not a valid cut as it cuts feasible set [egon model]."]

travel 2 sides of corner point and watch till the edge of infeasible region then draw a cut.

This works for high dim:
3D $\rightarrow$ 1 constraint $\rightarrow$ move 3 direction to find points $\rightarrow$ draw hyperplane that intersect & plane

- N dim $\rightarrow$ N direction $\rightarrow$ N points provided constraint is concave if work

$$x^TQ'x \leq b_1 \quad \text{if } Q \text{ is PD it is convex}$$
$$\quad \text{if } Q \text{ is ND} \rightarrow \text{concave}$$

If return P or ND

**DCF:** $\downarrow$ diff of convex fn

$$x^T(Q^{1+}-Q^{1-})x \leq b_1 \quad \text{P} \rightarrow \text{ND}$$

Indefinite symmetric matrix can be decomposed to difference of 2 psd using eigen value decomp.

also as,
$$x^TQ^{1+}x - w \leq b_1 \rightarrow \text{convex}$$
concave, $$w-x^TQ^{1-}x \leq 0$$

Tangent $\rightarrow$ convex
Intersection point $\rightarrow$ concave

In practical using simplex of intersection point $\rightarrow$ origin plane $\rightarrow$ many solvers do not use it unless $Q \rightarrow$ diagonal..