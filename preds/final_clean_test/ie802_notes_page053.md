# Heuristics for MINLO

## Initial Construction Heuristic

- Feasibility Pump (expensive)
- Rounding (sophisticated)
- Branching
- Local Branching

## MZLP Case: (Pure Binary)

$$\min c^T x \quad Ax \leq b \quad x \in \{0,1\}^n$$

**① Solve the LP**

$$\min c^T x \quad Ax \leq b \quad 0 \leq x \leq 1 \quad \Rightarrow \hat{x}$$

$\hookrightarrow$ If fractional $\rightarrow$ round it to nearest integer

$\hookrightarrow$ Not always works

Simple rounding of $\hat{x} = \begin{bmatrix} \lceil x_1 \rceil & \text{if } x_1 < 0.5 \\ \vdots \\ \lceil x_k \rceil & \text{on } \lceil x_k \rceil \end{bmatrix}$

$$\min \|x - \hat{x}\|_1, \quad x \in \{0,1\}^n, \; Ax \leq b$$

This will always give integers but hard...

**②** $\min_{i=1}^{n} |x_i - \hat{x}_i|$

$$Ax \leq b, \quad 0 \leq x \leq 1 \quad \Rightarrow \hat{x} \to \text{LP relaxation soln}$$

ex: $\hat{x} = \begin{bmatrix} 0 \\ 0.4 \\ 0.6 \\ 0.8 \\ 0.2 \end{bmatrix}$, sound($\hat{x}$) = $\begin{bmatrix} 0 \\ 0 \\ 1 \\ 1 \\ 0 \end{bmatrix}$

$\hookrightarrow$ not working, too bad

becomes: $\min |x_1-0| + |x_2-0| + |x_3-1| + |x_4-1| + |x_5-1| + |x_6-0|$

st $Ax \leq b$, $0 \leq x \leq 1$

$$\min x_1+(1-x_2)+x_3+(1-x_4)+(1-x_5)+x_6$$

st $Ax \leq b$, $0 \leq x \leq 1$

$\star$ if $\hat{x} = \begin{bmatrix} 0.1 \\ 0.9 \\ 0 \\ 0 \\ 0 \end{bmatrix}$, again round off gives same gain $\rightarrow$ we have to stop heuristic and flip some variables.