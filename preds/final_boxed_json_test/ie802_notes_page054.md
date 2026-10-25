# Convex MINLO Case (Pure Binary)

$$\min c^Tx+d^T\gamma$$
$$B(x,\gamma)\leq0$$
$$x\in\mathbb{R}^n, \quad \gamma\in\{0,1\}^p$$

$\rightarrow$ continuous

① Solve NLP relaxation $\Rightarrow$ get $\hat{x},\hat{\gamma}$ → round of $\hat{x},\hat{\gamma}$

② min $\sum_{i=1}^{p}|y_i-\text{round}(\hat{y}_i)|$

st $g_i(x,\gamma)\leq0$, $0\leq y\leq1$

$\hookrightarrow$ MIP $\Rightarrow \begin{bmatrix}\vdots\\\vdots\\\vdots\end{bmatrix}$, $\forall\in\{0,1\}^p$

**You can also solve MILP relaxation**

$$\min\sum|\gamma_i-\text{round}(\hat{\gamma}_i)|$$
st $\nabla$ inequalities at $(\hat{x},\hat{\gamma})$, $0\leq y\leq1$

---

# Non-convex MINLO Case (Pure Binary)

$\hookrightarrow$ Leave it...

## RINS Heuristic (Relaxed - Induced Nbd Search) → Improvement

**Convex MINLO:** Let $(\hat{x},\hat{\gamma})$ be known solution of MINLO.

[Diagram: A tree with root node branching into two child nodes, each of which branches further.]

① Solve NLP relaxation of that node $\Rightarrow (\hat{x},\hat{\gamma})$, $\hat{\gamma}\notin\mathbb{Z}^p$ → search nbd of it

② comp. $\hat{x}$ and $\hat{\gamma}$ → all these same $\rightarrow$ fix it

③ Solve the smallest MINLO

$\hookrightarrow$ don't solve fully but time limits ex. 5 sec., not limited and some other parameters.

$\hookrightarrow$ if majority of equal, randomly fix ($\hat{\gamma}_i=\bar{\gamma}_i$)