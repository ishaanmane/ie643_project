[Diagram: two boomerang/cone shaped sketches.]

Things get complicated, just adding a new bound: "Conv($S_1\cap S_2$)" — doable but not simple.

$x_1\cdot x_2$ is not convex expression, but when we draw it, it is convex.

How to reformulate this so the expression will also be convex.

[Diagram: A decreasing hyperbola-like curve in $(x_1,x_2)$ with shaded region above it, labeled "we can validate $x\geq1, y\geq1$".]

lot of the convex set, but just by looking at constraint $x_1\cdot x_2$ which is not convex, we cannot say everything is non convex.

**Reformulation:**
$$x_1\geq\frac{40}{x_2} \quad \text{(or)} \quad \frac{40}{x_2}-x_1\leq0 \leftarrow \text{convex function}$$

All we have to do it by taking tangents all way curve.

[Diagram: A decreasing hyperbola with several tangent lines drawn along it.]

$$x_1x_2\leq40, \quad 0\leq x_1\leq10, \quad 0\leq x_2\leq10$$

[Diagram: A shaded quadrilateral wedge region with a red curve labeled "Convex hull" along its upper-right edge.]

If we do $w_1\leq40$, $w_1=x_1x_2 \leftarrow$ this will give a floor relaxation. Not always things get simpler.
