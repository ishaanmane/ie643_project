## Convex MINLO Case (Pure Binary)

$$\min c^Tx+d^Ty$$
$$g_i(x,y)\leq0 \quad i=1,\dots,p$$
$$x\in\mathbb{R}^n, \quad y\in\{0,1\}^p \rightarrow \text{continuous}$$

① Solve NLP relaxation $\Rightarrow$ get $\hat{x},\hat{y}$ → round of $\Rightarrow$ you can also solve MILP relaxation

② min $\sum_{i=1}^{p}|y^i-\text{round}(\hat{y}^i)|$
st $g_i(x,y)\leq0$, $0\leq y\leq1$

$\Leftrightarrow$ MIP: $\min\sum|y^i-\text{round}(y^i)|$
st $\nabla$ inequalities at $(\hat{x},\hat{y})$, $0\leq y\leq1$

$$\Rightarrow \begin{bmatrix}\vdots\\\vdots\\\vdots\end{bmatrix}, \qquad y\in\{0,1\}^p$$

**Non-convex MINLO Case (Pure Binary)**

$\Rightarrow$ Leave it...

---

## RINS Heuristic (Relaxed-Induced Nbd Search) → Improvement

**Convex MINLO:** Let $(\hat{x},\hat{y})$ be known solution of MINLO

[Diagram: A tree with root node branching into two children, each of which branches further.]

① Solve NLP relaxation of that node $\Rightarrow (\hat{x},\hat{y})$, $\hat{y}\notin\mathbb{Z}^p$ → if majority of equal, randomly fix ($\hat{y}_i=\bar{y}_i$)

② comp. $\hat{y}$ and $\bar{y}$ → all those same → fix it

③ Solve the smallest MINLO → don't solve fully but time limits, ex. 5 sec., and some other parameters.