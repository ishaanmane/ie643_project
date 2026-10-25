**Topics to be discussed:**
- Intersection Cuts
- Cuts for non-convex quadratics
- Heuristics

## Intersection Cuts:

$$\min c^Ty \quad A y \leq b, \quad y \in \mathbb{Z}^p$$

[Diagram: A polygon with vertices marked by "x"s, one of which is labeled "corner point".]

**(1) Solve LP relaxation where we will be at corner**

**(2) If we drop other constraints which are not active, we end up only 2 constraints.**
[Diagram: A set of points with a line through them, labeled "we still get same point".]

**(3) If we look at integer points present, it is translation of cone. This is relaxation of original set.**

We can chop off some points by looking at cone.

[Diagram: A set of points with a cone drawn around them, and an arrow from the origin to a point on the boundary of the cone, labeled "valid cut for original problem too".]

"has to get these cuts" — we create a disjunction as all points on one of these sides.

[Diagram: A set of points with a red line drawn through them, cutting off a region that does not have any feasible point.]

Interior of this region does not have any feasible point.