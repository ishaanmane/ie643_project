we scale the vector $\begin{bmatrix}w_1\\w_2\end{bmatrix}$ to get to the point closest to $\begin{bmatrix}x_1\\x_2\end{bmatrix}$.

$\therefore$ Our projection vector is:

$$\left(\frac{x_1w_1+x_2w_2}{w_1^2+w_2^2}\right)\begin{bmatrix}w_1\\w_2\end{bmatrix}$$

[Diagram: Two vectors from the origin, one shorter and one longer along the same direction, illustrating scaling toward a target point.]

The numerator is just the dot/inner product of the two vectors $x$ & $w$.
The denominator is just the length$^2$($\begin{bmatrix}w_1\\w_2\end{bmatrix}$).

$\therefore$ For higher dimensions the projection vector is:

$$c^* \rightarrow \left(\frac{x^Tw}{\|w\|_2^2}\right)w \qquad \text{($L_2$ norm)}$$

$$x \rightarrow \begin{bmatrix}x_1\\\vdots\\x_k\end{bmatrix} \qquad w \rightarrow \begin{bmatrix}w_1\\\vdots\\w_k\end{bmatrix} \qquad x^T \rightarrow \begin{bmatrix}x_1 & \cdots & x_k\end{bmatrix}$$

## Note

Can always pick $w$ such that length($\begin{bmatrix}w_1\\\vdots\\w_k\end{bmatrix}$) = 1

$\Rightarrow$ Projection vector = $(x^Tw)w$
