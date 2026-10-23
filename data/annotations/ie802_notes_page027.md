$$\begin{bmatrix}x_{11}&x_{12}&x_{13}\\x_{21}&x_{22}&x_{23}\\x_{31}&x_{32}&x_{33}\end{bmatrix}\geq0 \to \text{for this principal leading minors, det}\geq0$$

**LP** vs **SDP**

LP: min $c^Tx$, $Ax=b$, $x\geq0$ — solve by simplex

SDP: min $\langle c,x\rangle=c_{11}x_{11}+c_{12}x_{12}+\dots c_{nn}x_{nn}$, $\langle A,X\rangle=b$, $X\geq0$ → solve by Interior Point method "Sam Burer" → cone, so convex

(Very diff...)

* Set $S$ is a cone if for every $x\in S$, $\lambda x\in S$ $\forall \lambda\geq0$

[Diagram: A shaded wedge region on $(x_1,x_2)$ axes representing the LP feasible cone.]

It is tight/perfect for all QCQPs with $q^{n^3}$ Variables.

SDP relaxation + secant inequalities + bilinear relaxation ← these includes $x$; For a much better lower bound... For settings $x$ and $X$:
$$\begin{bmatrix}1&x^T\\x&X_{n\times n}\end{bmatrix}\geq0$$
