06/04/26

**Topics to be discussed:**
- Intersection Cuts
- Cuts for non-convex quadratics
- Heuristics

**Intersection Cuts:**

$$\min c^Ty$$
$$Ay\leq b$$
$$y\in\mathbb{Z}^p$$

[Diagram: A hexagonal region with scattered "x" integer points, one vertex circled and labeled "corner point".]

(1) Solve LP relaxation, where we will be at corner

(2) If we drop other constraints which are not active, we end up only 2 constraints. [Diagram: scattered x points with two crossing lines meeting at a point labeled "we still get same point".]

(3) If we look at integer points present, it is translation of cone. This is relaxation of original set.

- We can chop off some points by looking at cone.

[Diagram: scattered x points with two crossing lines and a horizontal line through a circled point, labeled "valid cut for original problem too", "how to get these cuts".]

we create a disjunction as all points on one of these sides

[Diagram: scattered x and + points with two red diagonal lines converging near a circled point.]

look at the points, No feasible b/w hand lines, all int → below or above
- we reach from corner to corner of point red lines.

Interior of this region does not have any feasible points

**Cutting plane**
