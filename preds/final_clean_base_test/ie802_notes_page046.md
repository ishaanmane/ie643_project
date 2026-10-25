```markdown
# Topics to be discussed:

- Intersection Cut
- Cut for non-convex quadratics
- Heuristics

## Intersection Cut:

$\min \quad c^T y$

$Ay \leq b$

$y \in Z^p$

### Diagram: Intersection of feasible region

#### (1) Solve LP relaxation:
Where we will be at corner.

#### (2) If we drop other constraints which are not active, we end up with only 2 constraints.
[Diagram: Feasible region with two constraints]

#### (3) If we look at integer points present, it is translation of cone.
This is relaxation of original set.

We can chop off some points by looking at cone.

[Diagram: Cone and feasible region]

#### Diagram: Disjunction as all points on one of these sides
Leak out for original problem too.

#### Diagram: Feasible half band line
All into below or above.

We reach from corner to corner of point and line.

Intersection of tiny region does not have any feasible point.
```
