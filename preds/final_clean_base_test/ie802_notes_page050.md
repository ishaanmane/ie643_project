```markdown
# Finding Good Upper Bounds

## Minimization Problem
\[
\min_{x,y} f(x,y)
\]
Subject to:
\[
g_i(x,y) \leq 0, \quad i=1,2,\ldots,m
\]
\[
x \in \mathbb{R}^n
\]
\[
y \in \mathbb{Z}^p
\]

### Heuristics
- **Upper Bound**: Find a feasible point as fast as possible.
- **Good Upper Bound**:
  - **Prune the tree easily**
  - **Give a good solution in limited time**

*Chirobi may have 60-80 heuristics.*

## Heuristics
- **Steading Heuristics** (Don't need a feasible point to start)
  - Try to construct a solution from scratch
- **Improvement Heuristics** (Start with given a feasible solution, find better solutions)

## MINLOs
- **Heuristic for Unconstrained Models**
  - For models with many feasible solutions.
  - For models with few solutions (difficult task).

## Another Way to Classify Heuristics
- **General Purpose** (Structure Independent)
- **Class Specific** (Only Quadratic, Contin. NonConvex Quadratic, Conv. MIQP, Conic Integer Models)
- **Application Specific** (Portfolio Optimization, Power Flow Problems, Cutting Stock, VRP, Packing, Quad Assignment)
```

This structured Markdown preserves the original content, including mathematical expressions in LaTeX format, headings, bullet points, and the logical flow of the lecture notes.