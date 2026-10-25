$$w^1 = w^0 + x_3y_3 = \begin{bmatrix}0\\0\end{bmatrix} + \begin{bmatrix}-1/2\\1/2\end{bmatrix}\times1$$

$$w^2 = w^1 + x_1y_1 = \begin{bmatrix}-1/2\\1/2\end{bmatrix} + \begin{bmatrix}0\\1\end{bmatrix}\times1$$

$$w^2 = \begin{bmatrix}1\\1/2\end{bmatrix}$$

$$w^3 = w^2 + x_2y_2 = \begin{bmatrix}1\\1/2\end{bmatrix} + \begin{bmatrix}0\\-1\end{bmatrix}\times1$$

$$w^3 = \begin{bmatrix}1\\-1/2\end{bmatrix} = w^1$$

We see that we are right back where we started. The algorithm is unable to provide a $w$ which can correctly classify all the data points correctly. It just won't converge. Let's modify our assumption.

## Assumption

**Linear Separability with $\delta$-Margin**

A Dataset $\{(x_1,y_1),\dots(x_n,y_n)\}$ is Linearly Separable with $\delta$-margin if $\exists W\in\mathbb{R}^d$ st $(W^Tx_i)y_i\geq\delta\;\forall i$, some $\delta>0$

[Diagram: A separating hyperplane $w$ between two classes of points — green and yellow — each with a shaded margin region around it ($\{x:w^Tx\geq\delta\}$ and $\{x:w^Tx=-\delta\}$) — no points lie on the gap between these regions.]