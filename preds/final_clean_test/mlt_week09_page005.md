$$w^1 = w^0 + x_3y_3 = \begin{bmatrix}0\\0\end{bmatrix}+\begin{bmatrix}-1\\1/2\end{bmatrix}\times1 = \begin{bmatrix}-1\\1/2\end{bmatrix}$$

$$w^2 = w^1+x_1y_1 = \begin{bmatrix}-1/2\\1/2\end{bmatrix}+\begin{bmatrix}0\\1\end{bmatrix}\cdot1 = \begin{bmatrix}-1/2\\1/2\end{bmatrix}$$

$$w^3 = w^2+x_2y_2 = \begin{bmatrix}1\\0\end{bmatrix}+\begin{bmatrix}0\\1\end{bmatrix}\cdot1 = \begin{bmatrix}1\\1\end{bmatrix}$$

$$w^3 = \begin{bmatrix}1\\-1/2\end{bmatrix} = w^1$$

We see that we are right back where we started. The algorithm is unable to provide a $w$ which can correctly classify all the data points correctly. It just won't converge. Let's modify our assumption.

---

## Assumption

**Linear Separability with $\delta$-Margin**

[Diagram: Two overlapping green and yellow regions separated by a margin band, labeled $\{x:w^Tx\geq\gamma\}$ and $\{x:w^Tx\leq-\gamma\}$, with a separating line $w$ through the origin, and a shaded gap between them.]

A dataset $\{(x_1,y_1),\dots(x_n,y_n)\}$ is linearly separable with $\gamma$-margin if $\exists w\in\mathbb{R}^d$ st $(w^Tx_i)y_i\geq\gamma\; \forall i$, some $\gamma>0$.