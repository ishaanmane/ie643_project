```markdown
# Lecture Notes on Convex Hulls and Linear Programming

## Initial Setup
- We can choose any convex point initially such that the disjunction should be cutting the convex point (on) the convex point should be into two disjunctions to cut-off.

## Case Analysis
- If the starting point is not a corner of feasible region but infeasible region.
  - This is both as all feasible points are within the cone.
    - Basic goal point
    - Cut off here can much deeper.

## Extending to Non-Convex Cases
- This idea can be extended to non-convex too.
  - $g_1(x,y) \leq 0$
  - Where $g_1$ is convex
    - Diagram: [Convex Set]
  - Suppose $S_1$ is concave
    - $m_1^2 - m_2^2 \leq -1$
    - Outside circle
      - We can chop off the palm.

## Linear Constraints
- Suppose we have some linear constraints.
- Since hand we linear concave
- We may get convex point if it is infeasible region then we are done.

## Valid Cuts
- If not like this start to remove to extreme region
  - How to show the cut is valid?
    - To prove the infeasible is empty (or)
    - Valid cut
      - Not useful

## Concave Region
- Since $S(\cdot)$ is concave
- The part which is infeasible is convex set, using this we can check there is nothing below it.
```
