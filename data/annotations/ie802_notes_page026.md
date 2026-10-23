17-03-26

**SDP Relaxation:**

$$\text{min } q_{11}x_1^2+q_{12}x_1x_2+q_{21}x_2x_1+q_{13}x_1x_3+q_{14}x_1x_4+q_{22}x_2^2+\dots q_{nn}x_n^2 \quad (n^2 \text{ terms})$$

(P) st (Index 1) $a_{11}x_1^2+a_{12}x_1x_2+a_{13}x_1x_3+\dots a_{nn}x_n^2=b_1$
(Index 2) $a_{11}x_1^2+a_{12}x_1x_2+\dots a_{nn}x_n^2=b_2$
$\vdots$
(Index m) $a_{11}x_1^2+a_{12}x_1x_2+\dots a_{nn}x_n^2=b_m$
$$l\leq x\leq u$$

Make it linear by adding some variables:
$$\min q_{11}x_{11}+q_{12}x_{12}+\dots q_{22}x_{22}+\dots+q_{nn}x_{nn}$$
st $a_{11}^1x_{11}+a_{12}^1x_{12}+\dots a_{nn}^1x_{nn}=b_1$
$a_{11}^2x_{11}+a_{12}^2x_{12}+\dots a_{nn}^2x_{nn}=b_2$
$\vdots$
$a_{11}^mx_{11}+a_{12}^mx_{12}+\dots a_{nn}^mx_{nn}=b_m$

Non-linear part (I): $x_{11}=x_1x_1$, $x_{12}=x_1x_2$, $\vdots$, $x_{nn}=x_nx_n$
$$l\leq x\leq u$$

**Sharp's Result:** $X=xx^T$ is same as $X\geq0$ PSD (call eigen values of $X\geq0$), rank($X$)=1

$(m+1)\times n^2 \to$ inputs → expressions

(I): $X=x\cdot x^T$
$$\begin{bmatrix}x_{11}&x_{12}&\dots&x_{1n}\\x_{21}&x_{22}&\dots&x_{2n}\\\vdots&&&\\x_{n1}&x_{n2}&\dots&x_{nn}\end{bmatrix}=\begin{bmatrix}x_1\\x_2\\\vdots\\x_n\end{bmatrix}[x_1\;x_2\;\dots\;x_n] = \begin{bmatrix}x_1^2&x_1x_2&\dots\\x_2x_1&x_2^2&\dots\\x_3x_1&x_3x_2&\dots\\\vdots&&\\x_nx_1&x_nx_2&\dots\end{bmatrix} \quad \text{each column is multiple of column 1, Rank 1}$$

(P) is same as $\dots$
$$\min q_{11}x_{11}+q_{12}x_{12}\dots q_{nn}x_{nn}$$
st $a_{11}^1x_{11}+a_{12}^1x_{12}\dots a_{nn}^1x_{nn}=b_1 \Big\}$ Linear constraints (through $b_m$)

$X=xx^T$ ] Quadratic constraints...
$\approx X\geq0 \to$ convex; rank($X$)=1 → drop this → make relaxation...
$\to$ Kla Semi-Definite Programming model, matrix is unknown, and it should be PSD
