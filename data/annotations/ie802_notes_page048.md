Only works for $g_i(\cdot)$ is concave

[Diagram: A hatched infeasible region with three circled points on its boundary, arrow: "travel 2 sides of corner point and reach till the edge of infeasible region then draw a cut."]

→ Not a valid cut as it cuts feasible red [region]

- This works for high dim.
  3D → 2 constraints → move 3 direction to find points → draw hyperplane that intersect sphere
- N dim → N direction → N points

Provided constraint is concave if works:
$$x^TQ'x\leq b_i$$
if $Q$ is PD → it is convex
if $Q$ is ND → concave

If neither PD nor ND: indefinite symmetric matrix can be decomposed to difference of 2 terms, using eigen value decomp.

**DCF:** $x^T(Q'^+-Q'^-)x\leq b_1$ &nbsp; ($Q'^+$: PD, $Q'^-$: ND) ← diff of convex fn

also as: $x^TQ'^+x-w\leq b_1 \to$ convex
concave: $w-x^TQ'^-x\leq0$

Tangent → convex
Intersection points → concave
- In practical using simplex of intersection points → one is prone
→ many solvers do not use it unless $Q\to$ diagonal..
