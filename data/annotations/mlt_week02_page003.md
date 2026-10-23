$$w_k = X\alpha_k \quad \text{for some } \alpha_k \in \mathbb{R}$$

$$\begin{bmatrix} | & & | \\ x_1 & \cdots & x_n \\ | & & | \end{bmatrix}\begin{bmatrix}\alpha_{k_1} \\ \vdots \\ \alpha_{k_n}\end{bmatrix} = \sum_{i=1}^{n}x_i\alpha_{k_i}$$

Now how to get $\alpha_k$ which does not require order of $d^3$ computations?

we know $Cw_k = \lambda_kw_k$

$$\left(\frac{1}{n}XX^T\right)X\alpha_k = \lambda_kX\alpha_k$$
$$(XX^T)X\alpha_k = n\lambda_kX\alpha_k$$

multiplying both sides by $X^T$ we get,

$$X^T((XX^T)X\alpha_k) = X^T(n\lambda_kX\alpha_k)$$
$$(X^TX)(X^TX)\alpha_k = n\lambda_k(X^TX)\alpha_k$$

Let $(X^TX) = P$

$$\therefore P^2\alpha_k = n\lambda_kP\alpha_k$$

If we can find $\alpha_k$ that satisfies,

$X \in \mathbb{R}^{d\times n}$, $X^TX \in \mathbb{R}^{n\times n}$
