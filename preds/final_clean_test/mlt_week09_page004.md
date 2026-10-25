We need more careful argument for convergence.

## Example 2

[Diagram: A line through the origin with a point $(\begin{bmatrix}1\\1/2\end{bmatrix},-1)$ on one side labeled $+1$, and $(\begin{bmatrix}-1\\0\end{bmatrix},+1)$, $(\begin{bmatrix}0\\-1\end{bmatrix},+1)$ on the other side.]

Is this a linearly separable dataset?

$$\left\{\begin{bmatrix}0\\1\end{bmatrix},+1 \; ; \; \begin{bmatrix}0\\-1\end{bmatrix},+1 \; ; \; \begin{bmatrix}-1\\1/2\end{bmatrix},-1\right\}$$

Is there a $w\in\mathbb{R}^2$ st $w^Tx_i>0\Rightarrow y_i=+1$, $w^Tx_i<0\Rightarrow y_i=-1$?

**There is**

[Diagram: Same line through the origin, but now with a point $(\begin{bmatrix}1\\1/2\end{bmatrix},-1)$ on the "wrong" side (below the line) labeled $+1$, and $(\begin{bmatrix}-1\\0\end{bmatrix},+1)$, $(\begin{bmatrix}0\\-1\end{bmatrix},+1)$ still on the "correct" side above the line.]

---

[Diagram: A scatter plot of points $\begin{bmatrix}0\\1\end{bmatrix}$, $\begin{bmatrix}-1\\1/2\end{bmatrix}$, $\begin{bmatrix}-1\\-1\end{bmatrix}$, $\begin{bmatrix}1\\-1\end{bmatrix}$, all labeled $+1$. A separating line through the origin is shown, with an arrow from $\begin{bmatrix}-1\\1/2\end{bmatrix}$ to $\begin{bmatrix}1\\1/2\end{bmatrix}=w^*$, and another arrow from $\begin{bmatrix}-1\\-1\end{bmatrix}$ to $\begin{bmatrix}1\\-1\end{bmatrix}=w^*$.]

**Perceptron**

$$w^0 = \begin{bmatrix}0\\0\end{bmatrix}, \quad w^0{}^T x_1 = 0, \quad w^0{}^T x_2 = 0, \quad w^0{}^T x_3 = 0, \quad \hat{y}_1 = +1, \quad \hat{y}_2 = +1, \quad \hat{y}_3 = +1$$

$$w^1 = w^0 + x_3 y_3 = \begin{bmatrix}0\\0\end{bmatrix} + \begin{bmatrix}-1\\1/2\end{bmatrix} \times -1$$