Finding good upper bounds:

$$\min f(x,y) \quad \text{st. } g_i(x,y) \leq 0, i=1,2,\dots m$$
$$x \in \mathbb{R}^n, y \in \mathbb{Z}^p$$

* Upper bound → find a feasible point as fast as possible, as low obj. value as possible $\rightarrow$ **Primal Heuristic**

**Good upper bound**
- Prune the tree easily
- Give a good solution in limited time

* Churobi may have 60-80 heuristics...

## Heuristics

$\hookrightarrow$ Starting Heuristics (Don't need a feasible point to start) $\rightarrow$ Kla construction heuristics
$\hookrightarrow$ Try to construct a soln from scratch

$\hookrightarrow$ Improvement Heuristics (start with given a feasible soln $\hookrightarrow$ find better solns)

**MINLOs:**

$\hookrightarrow$ Heuristic for unanchored models
$\hookrightarrow$ For model with many feasible solutions.
$\hookrightarrow$ For models with few solutions (difficult task)

> another way to classify

Heuristic $\hookrightarrow$ General purpose (structure independent)
$\hookrightarrow$ Class specific (only Quadratic, Contin. NonConvex Q, Conv. MIQP, conic integer models)
$\hookrightarrow$ Application Specific (portfolio opt., power flow problems, cutting stock, VRP, packing, Quad. assignment..)

Imp.