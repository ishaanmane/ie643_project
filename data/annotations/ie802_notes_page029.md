*** $\sqrt{x_2^2+x_3^2+\dots+x_n^2}\leq x_1$, $x_1\geq0$ $\Big\}$ n-dim cone

$$* \; \sqrt{(x_2-1)^2+(3x_3-6)^2+x_4^2+\dots x_n^2} \leq x_1$$

$$x_1x_2\geq1 \to \text{not convex}$$
$$x_1x_2\geq0 \to \text{now convex}$$

→ use this

$$4x_1x_2\geq4$$
$$x_1x_2\geq0$$

$$(x_1+x_2)^2-(x_1-x_2)^2\geq4 \Leftrightarrow (x_1+x_2)\geq\sqrt{2^2+(x_1-x_2)^2}$$

(Transformed cone)

② If $Q$ is not PSD? → SDP slow, so less solvers: SeDuMi, MOSEK, CvxOpt

- If $Q_1$ has 1 -ve eigenvalue and some non-vity property, then it can be modeled as SOCP

**Ex:** $-x_1^2+x_2^2+x_3^2\leq0$, $x_1\geq0$ → 2nd order cone with one -ve eigen value

$$x_2^2+x_3^2\leq x_1^2 \to \text{non convex}$$

[Diagram: A double-cone (bowtie/hourglass) shape shaded, showing the non-convex region.]

$$x_2^2+x_3^2-x_1^2\leq0$$
$$\begin{bmatrix}-1&0\\0&1\end{bmatrix}$$

$$x_2^2+x_3^2-x_1^2\leq0, \; x_1\geq0 \to \text{convex whether it looks non-convex}$$
