per data point. They do not fall on the same line.

What we can do is used 2 representatives & consider each data point as a linear combination of these representatives.

Reps: $\left\{ \begin{bmatrix}1\\0\end{bmatrix}, \begin{bmatrix}0\\1\end{bmatrix} \right\}$   Coeffs: $\{(5,-5), (1,1), (7,7), (5,6), (10,10)\}$

$$x_3 = 10\begin{bmatrix}1\\0\end{bmatrix} + 10\begin{bmatrix}0\\1\end{bmatrix} = \begin{bmatrix}10\\10\end{bmatrix}$$
$$x_5 = 5\begin{bmatrix}1\\0\end{bmatrix} + 6\begin{bmatrix}0\\1\end{bmatrix} = \begin{bmatrix}5\\6\end{bmatrix}$$

This is not a good idea as the number of data points to store the coefficients has increased.

Now we are faced with the dilemma of having to give up either:
(a) exact reconstruction
(b) increasing the no. of representatives.

> The solution now is to somehow find the proxy for $x_5 = \begin{bmatrix}5\\6\end{bmatrix}$ along the line.

Now who can "pretend" to be the proxy of $x_5$ along the line?
$\rightarrow$ Projection of $x_5$ onto the violet line.
