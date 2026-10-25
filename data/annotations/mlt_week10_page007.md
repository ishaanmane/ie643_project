# Formulating the Dual Problem

$$\min_w \frac{1}{2}\|w\|^2 \to f(w) \; [\text{Quadratic in } w]$$
$$\text{s.t. } (w^Tx_i)y_i\geq1 \; \forall i=1,\dots,n \; [\text{Linear in } w]$$
$$\underbrace{1-(w^Tx_i)y_i\leq0 \; \forall i=1,\dots,n}_{g(w)}$$

$$L(w,\alpha) = f(w)+\alpha g(w) = \frac{1}{2}\|w\|^2 + \sum_{i=1}^{n}\alpha_i(1-(w^Tx_i)y_i), \qquad \alpha=\begin{bmatrix}\alpha_1\\\alpha_2\\\vdots\\\alpha_n\end{bmatrix}$$

$$\min_w\max_{\alpha\geq0}\left[\frac{1}{2}\|w\|^2+\sum_{i=1}^{n}\alpha_i(1-(w^Tx_i)y_i)\right] \equiv \max_{\alpha\geq0}\min_w\left[\frac{1}{2}\|w\|^2+\sum_{i=1}^{n}(1-(w^Tx_i)y_i)\right]$$

Fix some $\alpha\geq0$,
$$\min_w\left[\frac{1}{2}\|w\|^2+\sum_{i=1}^{n}(1-(w^Tx_i)y_i)\right]$$

$$w_\alpha^* + \sum_{i=1}^{n}\alpha_i(-x_iy_i) = 0$$
