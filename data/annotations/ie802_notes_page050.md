**Finding good upper bounds:** 07-04

$$\min f(x,y)$$
$$g_i(x,y)\leq0, \; i=1,2\dots m$$
$$x\in\mathbb{R}^n$$
$$y\in\mathbb{Z}^p$$

bcz goal is to find primal soln not dual

* Upper bound → find a feasible point as fast as possible, as low obj. value as possible $\Big\}$ Primal heuristic

**Good upper bound**
- prune the tree early
- give a good solution in limited time

* Gurobi may have 60-70 heuristics..

**Heuristics**
- Starting Heuristics (Don't need a feasible point to start) — try to construct a soln from scratch → kla construction heuristics
- Improvement Heuristics (start with given a feasible soln → find better solns)

**MINLOs:**
Today's class:
- Heuristic for unconstrained models
- for model with many feasible solutions
- for models with few solutions (difficult task)

△ another way to classify

Heuristic → General purpose (structure independent)
→ Class specific (only Quadratic, Contin. Non Convex Quadratic.., Conv. MIQP, conic integer models)
Imp° → Application specific (Portfolio opti., power flow problems, cutting stock, VRP, packing, Quad. assignment..)
