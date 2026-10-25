## Finding good upper bounds:

$$\min f(x,y) \quad s.t. x_i \leq 0, i=1,2\dots m, \quad x \in \mathbb{R}^n, y \in \mathbb{Z}^p$$

* **Upper bound** → find a feasible point as fast as possible, as low obj. value as possible (Bimodal heuristic)

Good upper bound:
- Bound the tree easily
- Give a good solution in limited time

* Gurobi may have 60-70 heuristics.

**Heuristics**
- Starting Heuristics (Don't need a feasible point to start)
  - Try to construct a soln from scratch
- Improvement Heuristics (Start with given a feasible soln → find better solns)

**MINLOS:**

Todays class $\hookrightarrow$ Heuristic for unchained models
$\hookrightarrow$ ... for model with many feasible solutions.
$\hookrightarrow$ ... for models with few solutions (difficult task)

> another way to classify

**Heuristic**
- General purpose (structure independent)
- Class specific (only Quadratic, Contin. NonConvex Quadrat., Conv. MIQP, Conic integer models)
- App. Specific (Portfolio opt., power flow problems, cutting stock, VRP, packing, Quad. assignment..)