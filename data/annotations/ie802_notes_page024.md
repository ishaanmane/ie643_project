16-03-26

$$\text{min } f(x,y)$$
$$\text{st } g_i(x,y)\leq0$$
$$x\in\mathbb{R}^n, \; y\in\mathbb{Z}^p$$

[Diagram: A large irregular region with scattered "x" points, a red line labeled "valid inequality" cutting a wrong region marked "wrong", another red line labeled "valid inequality" tightening near a circled optimal point, labeled "Good stop" and "Convex Relaxation" and "sum of relaxation → tighten it".]

*** A linear inequality $d^Tx+h^Ty\leq k$ is a **cutting plane** for $S$, if it is valid for $S$ and cuts off some given point, not in $S$.

How to find good cuts: lots of analysis. We have to find good cut.

**Integer Linear Program:**

General purpose cuts $\Big\{$ Gomory mixed integer cut, Split cut, Lift and project cuts, Reduced split cut $\Big\}$

Problem specific: Knapsack Cuts, Clique cuts, Flow cover, comb inequalities for TSP

[Diagram: A polygon region with scattered "x" points, several cutting lines drawn through it converging near a circled point labeled "optimal cut" with an arrow "cut".]

valid inequality → not disturbing feasible points

Given a model,
$$P \begin{cases}\text{Min } f(x,y)\\g_i(x,y)\leq0, \; i=1,2\dots m\\x\in\mathbb{R}^n, \; y\in\mathbb{Z}^n\end{cases}$$

* The set $S=\{(x,y): x\in\mathbb{R}^n, y\in\mathbb{Z}^p, g_i(x,y)\leq0, i=1,2\dots m\}$ is called feasible region of $P$

* An inequality $h(x,y)\leq0$ is said to be valid for $S$ if all points of $S$ satisfies $h(x,y)\leq0$ ***
