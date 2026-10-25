## Convex MINLO Case (Pure Binary)

$$\min c^Tx+d^Ty$$
$$g_i(x,y)\leq0 \quad i=1,\dots,p$$
$$x\in\mathbb{R}^n, \; y\in\{0,1\}^p \rightarrow \text{continuous}$$

① Solve NLP relaxation ($\Rightarrow$ get $\hat{x},\hat{y}$ → round of $\Rightarrow$ you can also solve MIP relaxation)

② min $\sum_{i=1}^{p}|y_i-\text{round}(y_i)|$
st $g_i(x,y)\leq0$, $0\leq y\leq1$

$$\Leftrightarrow \min\sum|y_i-\text{round}(y_i)| \; \Leftrightarrow \min\sum|\nabla\text{inequalities at }(\hat{x},\hat{y})|$$
$$0\leq y\leq1$$

MLP $\Rightarrow \vdots \; \vdots$
$\forall i\in\{1,\dots,p\}$

$$y\in\{0,1\}^p$$

**Non-convex MINLO Case (Pure Binary)**

$\Rightarrow$ Leave it...

---

## RINS Heuristic (Relaxed-Induced Neighborhood Search) $\rightarrow$ Improvement

**Convex MINLO:** Let $(\hat{x},\hat{y})$ be known solution of MINLO

[Diagram: A tree with root node branching into several child nodes, labeled "node" at the bottom.]

① Solve NLP relaxation of that node $\rightarrow (\hat{x},\hat{y})$, $\hat{y}\notin\{0,1\}^p$ (if majority of equal $\Rightarrow$ randomly fix)
search nbhd of it

② comp. $\hat{y}$ and $\tilde{y}$ $\rightarrow$ all those same $\rightarrow$ fix it

③ Solve the smaller MINLO

> don't solve fully but time limits, ex. 5 sec., and some other parameters.