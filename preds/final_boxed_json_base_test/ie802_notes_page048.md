```markdown
# Convexity and Concavity

## Only convex for g(x) is concave

- Travel 2 sides of corner point and watch all the edges of infeasible region then draw a cut.

## Not a valid cut as it cuts feasible red [region inside]

### This works for high dim.

#### 3D → 2 constraints
- Move 3 direction to find points → show hyperplane that intersect plane

#### N dim → N direction → N points
- Provided constraint is convex if work
- If Q is PD it is convex
- If Q is ND it is concave

## If return P or NO

### DCF:
- Difference of convex fn

## Also as,
$$
x^T(A^{++} - A^{--})x \leq b
$$
- In
- ND

## Indefinite symmetric matrix can be decomposed to difference of two convex using eigen value decom.

## Tangent → convex
- Intersection point → concave

## In practical using simplex of intersection point → convex plane
- Many solvers do not use it unless Q → diagonal.
```