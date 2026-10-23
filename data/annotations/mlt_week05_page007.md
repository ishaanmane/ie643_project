# Geometric Representation of Linear Regression

$$w^* = (XX^T)^+Xy$$

How can we interpret this geometrically?

Let $d=2$, $n=3$: $x_1,x_2,x_3$ (height, $f_1$), $y_1,y_2,y_3$ (weight, $f_2$)

There is an entire subspace or 2d plane which is the span of $f_1$ & $f_2$.

[Diagram: 3D axes with vectors $f_1 \in \mathbb{R}^3$, $f_2 \in \mathbb{R}^3$ spanning a yellow-shaded plane, $y \in \mathbb{R}^3$ pointing off the plane, and a dotted projection onto the plane labeled $\alpha_1^*f_1+\alpha_2^*f_2$.]

Any point in this plane is the linear combination of $f_1$ & $f_2$. There might be a special point on this plane which has the min. distance to the label 'y'.

Let the point be: $\alpha_1^*f_1+\alpha_2^*f_2 = \begin{bmatrix}|&|\\f_1&f_2\\|&|\end{bmatrix}\begin{bmatrix}\alpha_1^*\\\alpha_2^*\end{bmatrix} = [X^T\alpha^*]$

[Diagram: A right triangle with $y$ as hypotenuse, $X^T\alpha^*$ as the base, and $(y-X^T\alpha^*)$ as the vertical error leg.]
