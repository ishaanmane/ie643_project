```markdown
# Convexity and Concavity

## Only Convex for Q(x) is Concave

- Travel 2 sides of convex point and watch all the edges of infeasible region then draw a cut.
- Not a valid cut as it cuts feasible red [region below]

### This works for high dim.

- **3D → 2 constraints**
  - Move 3 directions to find points → show hyperplane that intersects plane
- **N dim → N directions → N points**

Provided constraint is convex if both:
- If Q is PD (Positive Definite) it is convex
- If Q is PD it is convex

If neither P or NO:

- **Diff of Convex Fn**:
  - $x^T(A^+ - A^-) \leq b$
  - In AND

Also as,
- $x^T A^+ x - w \leq b$ → convex
- $w - x^T A^- x \leq 0$ → concave

Tangent → convex
Intersection point → concave

In practical using simplex of intersection point → convex plane
→ many solvers do not use it unless Q → diagonal.
```
