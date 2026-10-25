only convex for $g(x)$ is concave

[Diagram: A shaded region with a corner point, arrows along its boundary, and a cut line drawn through it.]

$\rightarrow$ travel 2 sides of corner point and reach till the edge of infeasible region then draw a cut.

Not a valid cut as it cuts feasible red [egon hole]

- This works for high dim.
  - 3D $\rightarrow$ 2 constraints $\rightarrow$ move 3 direction to find points where hyperplane that intersect & plane
  - N dim $\rightarrow$ N direction $\rightarrow$ N points provided constraint is concave if we're

  If Q is PD it is convex
  if Q is ND -- concave

If neither PD nor ND

**DCP:** $x^T(Q^+ - Q^-)x \leq b$, $Q^+$ pos sem def, $Q^-$ neg sem def

also as, $x^TQ^+x - w \leq b$ $\rightarrow$ convex, concave, $w-x^TQ^-x \leq 0$

Tangent $\rightarrow$ convex, intersection point $\rightarrow$ concave

In practical using simplex of intersection point $\rightarrow$ cone plane $\Rightarrow$ many solvers do not use it unless $Q \rightarrow$ diagonal.