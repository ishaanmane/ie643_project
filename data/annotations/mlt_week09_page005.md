$$w^1 = \begin{bmatrix}0\\0\end{bmatrix} + \begin{bmatrix}1\\-1/2\end{bmatrix} = \begin{bmatrix}1\\-1/2\end{bmatrix}$$

$$w^2 = w^1 + x_1y_1 = \begin{bmatrix}1\\-1/2\end{bmatrix} + \begin{bmatrix}0\\1\end{bmatrix}\cdot1 = \begin{bmatrix}1\\1/2\end{bmatrix}$$

$$w^3 = w^2 + x_2y_2 = \begin{bmatrix}1\\1/2\end{bmatrix} + \begin{bmatrix}0\\-1\end{bmatrix}\times1 = \begin{bmatrix}1\\-1/2\end{bmatrix} = w^1$$

We see that we are right back where we started. The algorithm is unable to provide a $w$ which can correctly classify all the data points correctly. It just won't converge. Let's modify our assumption.

## Assumption: Linear Separability with $\gamma$-Margin

The gap can be very small but not zero. No points lie on the gap.

A Dataset $\{(x_1,y_1),\dots,(x_n,y_n)\}$ is Linearly Separable with $\gamma$-margin if $\exists w^*\in\mathbb{R}^d$ s.t. $(w^{*T}x_i)y_i\geq\gamma \; \forall i$, some $\gamma>0$

[Diagram: A green and yellow region cleanly separated by a margin band around a line through the origin, normal vector $w$, with the margin boundaries labeled $\{x:w^Tx=\gamma\}$, $\{x:w^Tx=0\}$, $\{x:w^Tx=-\gamma\}$.]
