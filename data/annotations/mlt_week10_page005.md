# Constrained Optimization

$$\min_w f(w) \leftarrow \text{objective function} \quad \text{such that } g(w)\leq0 \leftarrow \text{constraint function} \quad \text{(A)}$$

Lagrange Function: $L(w,\alpha) = f(w) + \alpha g(w)$

Fix any $w$ & consider
$$\max_{\alpha\geq0} L(w,\alpha) = \max_{\alpha\geq0} f(w)+\alpha g(w)$$

$$\max \text{ value of the function} = \begin{cases}\alpha\infty & \text{when } g(w)>0\\f(w) & \text{when } g(w)\leq0\end{cases}$$

[Diagram: A 2D region ($w_1,w_2$ axes) shaded yellow representing $\{w:g(w)\leq0\}$, with $f(w)$ marked at an interior point, and scattered points $x_2,x_3,x_4$ outside the region.]

$$\min_w\left[\max_{\alpha\geq0} f(w)+\alpha g(w)\right] \equiv \min_w f(w) \text{ s.t. } g(w)\leq0 \quad \text{minimum $w$ in the shaded region}$$
