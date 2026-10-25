- We need more careful argument for convergence.

## Example 2

[Diagram: Three points on coordinate axes: green $(0,1)$ and $(0,-1)$ labeled +1, and red $(-1,1/2)$ labeled −1.]

 $\left(\begin{bmatrix}0\\1\end{bmatrix},+1\right)$, $\left(\begin{bmatrix}0\\-1\end{bmatrix},+1\right)$, $\left(\begin{bmatrix}-1\\1/2\end{bmatrix},-1\right)$

Is this a Linearly separable dataset?

Is there a $w\in\mathbb{R}^2$ s.t. $w^Tx_i\geq0 \Rightarrow y_i=+1$, $w^Tx_i<0 \Rightarrow y_i=-1$?

**There is** — [Diagram: the three points plotted with a vertical separating line through the origin and $w$ pointing right along the x-axis.]

---

[Diagram: The three points $x_1=\begin{bmatrix}0\\1\end{bmatrix}(+1)$, $x_2=\begin{bmatrix}0\\-1\end{bmatrix}(+1)$, $x_3=\begin{bmatrix}-1\\1/2\end{bmatrix}(-1)$ with candidate separator lines $w^1=\begin{bmatrix}1\\-1/2\end{bmatrix}$, $w^2=\begin{bmatrix}1\\1/2\end{bmatrix}$ rotating between them.]

## Perceptron

$$w^0=[0\;0]$$
$$w^{0T}x_1=0; \; \hat{y}_1=+1 \qquad w^{0T}x_2=0; \; \hat{y}_2=+1 \qquad w^{0T}x_3=0; \; \hat{y}_3=+1$$

$$w^1 = w^0 + x_3y_3 = \begin{bmatrix}0\\0\end{bmatrix} + \begin{bmatrix}-1\\1/2\end{bmatrix}\times-1$$
