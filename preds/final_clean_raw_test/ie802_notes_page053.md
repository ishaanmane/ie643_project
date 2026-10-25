# Heuristics for MINLO

## Initial Construction Heuristic

- Feasibility Pump (expensive)
- RINS
- Local Branching
- Rounding (Sophisticated)

**MILP Case:** (Pure binary)
$$\min c^Tx \quad Ax \leq b \quad x \in \{0,1\}^n$$

① Solve the LP:
$$\min c^Tx \quad Ax \leq b \quad 0 \leq x \leq 1$$
$\Rightarrow \hat{x}$

If fractional $\rightarrow$ round it to nearest integer $\Rightarrow$ Not always good

Simple rounding of $\hat{x} = \begin{bmatrix} \lfloor x_1 \rfloor \text{ if } x_1 < 0.5 \\ \vdots \\ \lfloor x_n \rfloor \text{ on } [x_i] \end{bmatrix} \Rightarrow \min \|x-\hat{x}\|_1$

$$\min_{x \in \{0,1\}^n} \|Ax-b\|_1 \; \text{and} \; 0 \leq x \leq 1$$

② $\min \sum_{i=1}^{n}|x_i-\hat{x}_i|$ — rounding of ($\hat{x}$) $\rightarrow$ LP relaxation soln

$$\min \left(|x_1-0|+|x_2-0|+|x_3-0|+|x_4-0|+|x_5-1|+|x_6-0|\right) \; \text{st} \; Ax \leq b, \; 0 \leq x \leq 1$$

Q8: $\hat{x} = \begin{bmatrix}0.1\\0.4\\0.6\\0.8\\0.1\end{bmatrix}$, sound($\hat{x}$) = $\begin{bmatrix}0\\0\\0\\0\\0\end{bmatrix}$

If wanted 0 and 1 odd

If $\hat{x} = \begin{bmatrix}0.1\\0.9\\0.1\\0\\0\end{bmatrix}$, again round off gives same soln $\rightarrow$ we have to stop heuristic and flip some variables.