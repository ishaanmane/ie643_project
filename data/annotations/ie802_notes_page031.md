24/03/26

Quadratic functions are 60% of solvers

Quadratic fn: $\min x^TQ_0x+a_0^Tx$
st $x^TQ_1x+a_1^Tx\leq b_1$
$\vdots$
$x^TQ_mx+a_m^Tx\leq b_m$
$l\leq x\leq u$

We can make it non-linear:
$$\min \langle Q_0,X\rangle+a_0^Tx$$
st $\langle Q_1,X\rangle+a_1^Tx\leq b_1$
$\langle Q_m,X\rangle+a_m^Tx\leq b_m$
$l\leq x\leq u$

$$X=xx^T$$
$n\times n$
rank of $X=1$
$X\geq0 \to$ convex

$$\begin{bmatrix}1&x^T\\x&X\end{bmatrix}\geq0 \leftarrow \text{convex}$$

Now model becomes linear, SD problem. SDP gives a lower bound to original problem.

- SDP takes time to solve → slow, so we try some other ideas:

**Idea 1)** $\min x^TQ_0x+a_0^Tx$
st $Ax\leq b$
$l\leq x\leq u$

rewrite $\to \min x^T(Q_0+KI)x+a_0^Tx-K\cdot x^TIx$

If we pick $K$ big enough than most -ve eigen value of $Q_0$, the problem will be more convex.

Let $\sigma_{min}$ = minimum eigen value of $Q_0$ (or) most -ve eigen value.

Then $K\geq|\sigma_{min}|$

$$\min x^T(Q_0+KI)x+a_0^Tx-\sum_{i=1}^{n}Kx_i^2 \to \text{we don't need bilinear constraints}$$
$$Ax\leq b$$
$$l\leq x\leq b$$

→ Not always faster than original problem
