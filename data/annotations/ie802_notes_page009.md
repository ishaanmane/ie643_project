at $\begin{bmatrix}0\\0\end{bmatrix} \to 0+[0\;{-1}]\begin{bmatrix}x_1-0\\w_1-0\end{bmatrix}\leq0$

$$w\geq0$$

for upper bound we can: $\boxed{w_1\leq10x_1}$ — This depends on bounds

Secant was not needed in Convex MINLP

We solve (P) 🔵. We relax the programme:

**LP relaxation**
$$\text{Min } x_1+2x_2+3x_3-\cdots$$
$$3x_2+x_3-x_4\cdots$$

Secant $\{w_1\leq10x_1$
Tangent $\{w_1\geq0, \; w_1\geq\cdots, \; w_1\geq\cdots$

$w_2\geq0$
$w_2\leq10x_2$

**Solve LP relaxation:**
- if infeasible $\Rightarrow$ (P) infeasible
- if the LP optimal point $(\hat{x},\hat{w})$ satisfies all constraints of (P), then $(\hat{x},\hat{w})$ is optimal to (P).
- LP relaxation is unbounded $\to$ [Complaint to the modeller] $-1\leq x_1\leq1$, $\frac{1}{x_1}$
- $(\hat{x},\hat{w})$ does not satisfy all non-linear constraints of (P), we have 2 cases in this style.
