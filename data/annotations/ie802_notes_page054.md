**Convex MINLO Case (Pure Binary)**

$$\min c^Tx+d^Ty$$
$$g_i(x,y)\leq0$$
$$x\in\mathbb{R}^n$$
$$y\in\{0,1\}^p \to \text{continuous}$$

① Solve NLP relaxation → get $\bar{x},\bar{y}$ → round off $\bar{y}$

⊛ You can also solve MILP relaxation

② $\min\sum_{i=1}^{p}|y_i-\text{round}(\bar{y})|$ ⇔ $\min\sum|y_i-\text{round}(y_i)|$
st $g_i(x,y)\leq0$, $0\leq y\leq1$ → st $\nabla$ inequalities at $(\bar{x},\bar{y})$, $0\leq y\leq1$

$\Leftrightarrow$ MILP $\{\vdots\}$, $y\in\{0,1\}^p$

**Non-convex MINLO Case (Pure Binary)** → Leave it...

**RINS Heuristic** (Relaxed-Induced Nbhd Search) → Improvement

Convex MILO: Let $(\hat{x},\hat{y})$ be known solution of MINLO

[Diagram: A branch-and-bound tree with several circle nodes, one node circled and labeled "here".]

① Solve NLP relaxation of that node → $(\bar{x},\bar{y})$, $\bar{y}\notin\mathbb{Z}^p$ → search nbhd of it → if majority of equal → randomly fix, $(\hat{y}_i=\bar{y}_i)$

② comp. $\hat{y}$ and $\bar{y}$ → all those same → fix it

③ Solve the smaller MINLO → don't solve fully (Node limit) put time limits ex. 5 sec.. and some other parameters..
