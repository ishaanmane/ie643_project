$$4x_1x_2\geq4$$
$$x_1+x_2\geq0$$

$\hookrightarrow (x_1+x_2)^2 \geq 4+(x_1-x_2)^2$, also SOCP

**Fujie & Kojima:**

① Let (P) be a QCQP
② Let (P) have an SOCP convex relaxation of the form

$$\min x^TB_0x+b_0^Tx$$
$x\in\mathbb{R}^n$
st $x^TB_1x+b_1^Tx\leq\beta_1$
(Convex QCQP) $x^TB_2x+b_2^Tx\leq\beta_2$
$\vdots$
$x^TB_kx+b_k^Tx\leq\beta_k$

Then the SDP

(SDP) $\min \langle B_0,X\rangle+b_0^Tx$
st $\langle B_1,X\rangle+b_1^Tx\leq\beta_1$
$\vdots$
$\langle B_k,X\rangle+b_k^Tx\leq\beta_k$, $l\leq x\leq u$

has same optimal value as convex QCQP.

$$X-xx^T\geq0 \Leftrightarrow \begin{bmatrix}1&x^T\\x&X\end{bmatrix}\geq0 \quad \text{same}$$
