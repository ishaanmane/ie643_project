Finding good upper bounds:

$$\min_{(x,y)} \quad g_i(x,y) \leq 0, \; i=1,2,\dots m$$
$$x \in \mathbb{R}^n, \quad y \in \mathbb{Z}^p$$

* Upper bound → find a feasible point as fast as possible, as low obj. value as possible $\rightarrow$ Primal heuristic

**Good upper bound**
$\hookrightarrow$ Prune the tree easily
$\hookrightarrow$ Give a good solution in limited time

* Chvatal may have 60-80 heuristics...

## Heuristics

$\hookrightarrow$ Starting Heuristics (Don't need a feasible point to start) $\hookrightarrow$ Try to construct a soln from scratch
$\hookrightarrow$ Improvement Heuristics (start with given a feasible soln $\hookrightarrow$ find better solns)

**MINLOs**

Today's class $\hookrightarrow$ Heuristic for unanchained models
$\hookrightarrow$ - for model with many feasible solutions.
$\hookrightarrow$ - for models with few solutions (difficult task)

> another way to classify

Heuristic $\hookrightarrow$ General purpose (structure independent)
$\hookrightarrow$ Class specific (only Quadratic, Contin. NonConvex Quadratic, conv. MIQP, conic integer models)
$\hookrightarrow$ Imp. $\hookrightarrow$ Application Specific (portfolio opt., power flow problems, cutting stock, VRP, packing, Quad. assignment...)