```markdown
# Finding Good Upper Bounds

## Minimizing Problem
\[
\min_{(x,y)} \quad f(x,y) \leq 0 \quad i=1,2,\dots m
\]
\[ x \in \mathbb{R}^n \]
\[ y \in \mathbb{Z}^p \]

## Goal
The goal is to find a primal solution not dual.

## Heuristic Approach
- **Upper Bound**: Find a feasible point as fast as possible with the lowest objective value.
- **Good Upper Bound**: 
  - **Pause the timer easily**.
  - **Give a good solution in limited time**.

## Gurobi Heuristics
Gurobi may have 60-80 heuristics.

### Heuristics
#### Steading Heuristics
- Don't need a feasible point to start.
- Try to construct a solution from scratch.

#### Improvement Heuristics
- Start with a given feasible solution.
- Find better solutions.

## MINLOs
### Today's Class
- Heuristic for unanchored models.
- For models with many feasible solutions.
- For models with few solutions (difficult task).

## Another Way to Classify Heuristics
### General Purpose (Structure Independent)
- Class Specific (only Quadratic, Continuum Non-Convex Quadratic, Convex MIQP, Conic Integer Models).
- Application Specific (Portfolio Optimization, Power Flow Problems, Cutting Stock VRP, Packing, Quadratic Assignment).

```
```