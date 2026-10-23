## Projection

[Diagram: A line through the origin along direction $\begin{bmatrix}w_1\\w_2\end{bmatrix}$, a stray point $\begin{bmatrix}x_1\\x_2\end{bmatrix}$ off the line, and its projection $c\begin{bmatrix}w_1\\w_2\end{bmatrix}$ on the line, connected by a dotted line.]

The blue line is $\begin{bmatrix}w_1\\w_2\end{bmatrix}$ i.e. the scalar multiples of $\begin{bmatrix}w_1\\w_2\end{bmatrix}$.

$\begin{bmatrix}x_1\\x_2\end{bmatrix}$ is the stray point we want to project onto $\begin{bmatrix}w_1\\w_2\end{bmatrix}$.

$c \rightarrow$ constant. We want the error to be as small as possible. (we want to find such $c$ for which error length is minimum)

$$\min_c \; \text{length}^2(\text{error vector}) \rightarrow \begin{bmatrix}x_1 - cw_1 \\ x_2 - cw_2\end{bmatrix}$$

$$\min_c (x_1-cw_1)^2 + (x_2-cw_2)^2$$

(Taking the derivative wrt $c$ & setting it to 0 we get)

$$-2w_1(x_1-cw_1) - 2w_2(x_2-cw_2) = 0$$
$$w_1(x_1-cw_1) = w_2(cw_2-x_2)$$
$$x_1w_1 - cw_1^2 = cw_2^2 - x_2w_2$$
$$x_1w_1 + x_2w_2 = c(w_1^2+w_2^2)$$

$$c^* = \frac{x_1w_1+x_2w_2}{w_1^2+w_2^2} \quad \text{(scalar)}$$

It means how much should
