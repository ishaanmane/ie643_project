- We need more careful argument for convergence.

## Example 2

[Diagram: A line through the origin with slope -1, labeled $\omega$, separating two groups of points — $(0,1)$, $(1,0)$ on one side ($y=+1$) and $(0,-1)$, $(-1,0)$ on the other ($y=-1$).]

Is this a linearly separable dataset?

$$\begin{bmatrix}0\\1\end{bmatrix}, +1 \qquad \begin{bmatrix}0\\-1\end{bmatrix}, +1 \qquad \begin{bmatrix}-1\\0\end{bmatrix}, -1$$

Is there a WER^2 st. $w^Tx_i>0 \Rightarrow y_i=+1$, $w^Tx_i<0 \Rightarrow y_i=-1$

**There is**

[Diagram: Same line through the origin, now with a point $(1,-1)$ on the "wrong" side ($y=-1$) and $(0,-1)$ on the correct side ($y=+1$).]

## Perceptron

[Diagram: A dot at $(0,1)$ labeled $x_1$, another at $(0,-1)$ labeled $x_2$, both with arrows to $\begin{bmatrix}1\\0\end{bmatrix}$ labeled $w^2$. A separate dot at $(1,0)$ labeled $x_3$ with an arrow to $\begin{bmatrix}-1\\0\end{bmatrix}$ labeled $w^4$.]

$$w^0 = \begin{bmatrix}0&0\end{bmatrix}$$
$$w^0T x_1 = 0, \; w^0T x_2 = 0, \; w^0T x_3 = 0, \; \hat{y}_1 = +1, \; \hat{y}_2 = +1, \; \hat{y}_3 = +1$$

$$w^1 = w^0 + x_3y_3 = \begin{bmatrix}0\\0\end{bmatrix} + \begin{bmatrix}-1\\0\end{bmatrix}x^{-1}$$