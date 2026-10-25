- We need more careful argument for convergence.

## Example 2

[Diagram: A line through $(\begin{bmatrix}0\\1\end{bmatrix}, -1)$ and $(\begin{bmatrix}0\\-1\end{bmatrix}, +1)$, with a point $(\begin{bmatrix}0\\0\end{bmatrix})$ at the origin labeled "$+1$", another point $(\begin{bmatrix}-1\\1/2\end{bmatrix})$ below it labeled "$+1$", and a point $(\begin{bmatrix}-1\\-1/2\end{bmatrix})$ above it labeled "$+1$".]

Is this a linearly separable dataset?

$$\left\{\begin{bmatrix}0\\0\end{bmatrix}, +1 \; ; \; \begin{bmatrix}0\\-1\end{bmatrix}, +1 \; ; \; \begin{bmatrix}-1\\1/2\end{bmatrix}, -1\right\}$$

Is there a $w \in \mathbb{R}^2$ st $w^Tx_i > 0 \Rightarrow y_i = +1$, $w^Tx_i < 0 \Rightarrow y_i = -$?

**There is**

[Diagram: A line through $(\begin{bmatrix}0\\1\end{bmatrix}, -1)$ and $(\begin{bmatrix}0\\-1\end{bmatrix}, +1)$, with a point $(\begin{bmatrix}0\\0\end{bmatrix})$ at the origin labeled "$+1$", another point $(\begin{bmatrix}-1\\1/2\end{bmatrix})$ below it labeled "$+1$", and a point $(\begin{bmatrix}-1\\-1/2\end{bmatrix})$ above it labeled "$+1$". A vector $w$ pointing rightward is shown.]

## Perceptron

[Diagram: A dot at $(0,0)$ labeled "$+1$" with two lines radiating from it — one through $(1,1)$ labeled "$+1$" and one through $(1,-1)$ labeled "$-1$". A dot at $(1,1)$ labeled "$+1$" and a dot at $(1,-1)$ labeled "$-1$" are shown near the origin.]

$$w^0 = \begin{bmatrix}0 \\ 0\end{bmatrix}, \quad w^0x_1 = 0, \quad w^0x_2 = 0$$
$$\hat{y}_1 = +1, \quad \hat{y}_2 = -$$

$$w^1 = w^0 + x_3y_3 = \begin{bmatrix}0 \\ 0\end{bmatrix} + \begin{bmatrix}-1\end{bmatrix} \times -1$$

$$w^1x_3 = 0, \quad \hat{y}_3 = +1$$