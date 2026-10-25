# Heuristics for MINLO

## Initial Construction Heuristic

- Feasibility Pump (expensive)
- Rounding (sophisticated) → Local Branching

**MILP Case:** (pure binary)

$$\min c^Tx \quad Ax \leq b \quad x \in \{0,1\}^n$$

① Solve the LP:
$$\min c^Tx \quad Ax \leq b \quad 0 \leq x \leq 1$$

$\hookrightarrow$ If fractional $\rightarrow$ round it to nearest integer $\hookrightarrow$ Not always good

Simple rounding of $\hat{x} = \begin{bmatrix}\lfloor x_1 \rfloor \\ \vdots \\ \lfloor x_n \rfloor\end{bmatrix}$ on $\lceil x_i \rceil$

② min $\sum_{i=1}^{n}|x_i-\hat{x}_i|$
$$Ax \leq b, \quad 0 \leq x \leq 1 \quad \Rightarrow \text{LP relaxation soln}$$

or: $\hat{x} = \begin{bmatrix}0\\0.4\\0.6\\0.4\\0.1\end{bmatrix}$, sound($\hat{x}$) = $\begin{bmatrix}0\\0\\1\\0\\0\end{bmatrix}$

become: st $Ax \leq b$, $0 \leq x \leq 1$

$$\min|x_1-0|+|x_2-1|+\cdots+x_5+1+x_6$$

If $\hat{x} = \begin{bmatrix}0.1\\0.9\\0\\0\\0\end{bmatrix}$, again round off gives same gain $\rightarrow$ we have to stop heuristic and flip some variables.