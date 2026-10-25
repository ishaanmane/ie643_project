**Heuristics for MINLO** 13/04/26

**Initial / construction Heuristic**
- Feasibility Pump (expensive) → rounding (sophisticated)
- RINS
- Local Branching

**MILP Case:** (Pure binary)
$$\min c^Tx$$
$$Ax\leq b$$
$$x\in\{0,1\}^n$$

① Solve the LP: $\min c^Tx$, $Ax\leq b$, $0\leq x\leq1$ → $\bar{x}$

→ if fractional → round it to nearest integer → Not always work

Simple rounding of $\bar{x} = \begin{bmatrix}\lfloor x_1\rfloor \text{ if } x_1<0.5, \text{o.w. }\lceil x_1\rceil\\\vdots\\\lfloor x_i\rfloor \text{ or } \lceil x_i\rceil\end{bmatrix}$ $\Leftrightarrow$ $\min \|x-\bar{x}\|_1$, $x\in\{0,1\}^n$, $Ax\leq b$ → this will always give integer but hard..

② rounding of $\bar{x}$: $\min\sum_{i=1}^{n}|x_i-\bar{x}|$, $Ax\leq b$, $0\leq x\leq1$ // $\bar{x}\to$ LP relaxation soln

eg. $\bar{x}=\begin{bmatrix}0\\1\\0.4\\0.6\\0.8\\0.1\end{bmatrix}$, round($\bar{x}$)$=\begin{bmatrix}0\\1\\0\\1\\1\\0\end{bmatrix}$ if works → good

$$\min|x_1-0|+|x_2-1|+|x_3-0|+|x_4-1|+|x_5-1|+|x_6-0|$$
st $Ax\leq b$, $0\leq x\leq1$

not work then

becomes $\min x_1+(1-x_2)+x_3+(1-x_4)+(1-x_5)+x_6$
st $Ax\leq b$, $0\leq x\leq1$

if $\bar{x}=\begin{bmatrix}0.1\\0.9\\0\\1\\1\\0\end{bmatrix}$ → again round off gives same soln → we have to stop heuristic and flip some variables..
