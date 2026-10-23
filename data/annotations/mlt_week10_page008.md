$$\boxed{w^* = \sum_{i=1}^{n}\alpha_i(x_iy_i)}$$

$$w_\alpha^* = Xy\alpha$$

$$X = \begin{bmatrix}|&|&&|\\x_1&x_2&\cdots&x_n\\|&|&&|\end{bmatrix}, \quad y=\begin{bmatrix}y_1&&0\\&\ddots&\\0&&y_n\end{bmatrix}, \quad \alpha=\begin{bmatrix}\alpha_1\\\vdots\\\alpha_n\end{bmatrix}$$

Substituting $w_\alpha^*$ into $L(w,\alpha)$ & simplifying,
$$= \alpha^T\mathbb{1} - \frac{1}{2}(Xy\alpha)^T(Xy\alpha)$$

**PRIMAL**
$$\min_w \frac{1}{2}\|w\|^2 \; \text{s.t. } (w^Tx_i)y_i\geq1$$

**DUAL PROBLEM**
$$\max_{\alpha\geq0} \alpha^T\mathbb{1} - \frac{1}{2}\alpha^Ty^TX^TXy\alpha$$

Both will give the same solution.

Advantage of dual problem?
- Dimension of dual problem is $\mathbb{R}^n$ & that of primal is $\mathbb{R}^d$
- Dual constraints are easier
