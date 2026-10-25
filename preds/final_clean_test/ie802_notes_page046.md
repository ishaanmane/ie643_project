**Topics to be discussed:**
- Intersection Cuts
- Cut for non-convex quadratics
- Heuristics

## Intersection Cuts:

$$\min c^Ty \quad A y \leq b \quad y \in \mathbb{Z}^p$$

[Diagram: A polygon with vertices marked by "x"s, one red dot labeled "corner point" at the bottom right.]

**(i) Solve LP relaxation where we will be at corner**

**(2) If we drop other constraints which are not active, we end up only 2 constraints.**
[Diagram: A cone with a few "x" points inside, some outside, and an arrow pointing to a point inside the cone labeled "we still get some points".]

**(3) If we look at integer points present, it is translation of cone. This is relaxation of original set.**

We can chop off some points by looking at cone.

[Diagram: A cone with several "x" points inside and a few outside, an arrow from a point inside the cone to another point outside labeled "yield cut for original problem too", with a note "has to get these cuts".]

We create a disjunction as all points on one of these sides leave out the points. No feasible lb hand line, all int $\rightarrow$ below or above.

- We reach from corner to corner, or point and line.

[Diagram: A region with a red cross through it, labeled "current plane", and a note "intersection of tiny region does not have any feasible point".]