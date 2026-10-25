## Topics to be discussed:

- Intersection Cuts
- Cut for non-convex quadratics
- Heuristics

## Intersection Cuts:

$$\min c^Ty \quad Ay \leq b \quad y \in \mathbb{Z}^p$$

[Diagram: A polygon with vertices marked by "x"s, containing a red dot labeled "corner point".]

**(1) Solve LP relaxation** where we will be at corners.

**(2) If we drop other constraints which are not active, we end up only 2 constraints.**
[Diagram: A region with several "x" points inside, a few marked by arrows, and a shaded cone region — "we still get some points".]

**(3) If we look at integer points present, it is translation of cone. This is relaxation of original set.**

we can chop off some points by looking at cone.

[Diagram: A region with "x" points, a red dot at an intersection, a line through the origin, and an arrow pointing to a point outside the cone — "yield cut for original problem too."]

we create a disjunction as all points on one of these sides.

[Diagram: A region with "x" points, a red dot at an intersection, a line through the origin, and a red line through the origin — "cut by plane".]

Intersection of this region does not have any feasible points.