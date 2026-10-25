```markdown
# Topics to be discussed:

- Intersection Cut
- Cut for non-convex quadratics
- Heuristics

## Intersection Cuts

$\min \quad c^T y$

$A y \leq b$

$y \in Z^p$

### (1) Solve LP relaxation

Where we will be at corners.

### (2) If we drop other constraints which are not active, we end up with only 2 constraints.

[Diagram: Two-dimensional space with two intersecting lines]

We still get some points.

### (3) If we look at integer points present, it is translation of cone.

This is relaxation of original set.

We can chop off some points by looking at cone.

[Diagram: Cone with points inside and outside]

We create a disjunction as all points on one of these sides.

[Diagram: Two lines intersecting, forming regions]

Intersection of these regions does not have any feasible points.

### Conclusion

No feasible line lies between or below or above.
```