## Gradient of a fn at a point $x$

$$\nabla f(x) = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_d} \end{bmatrix}$$

$$f'(x;u) = \langle \nabla f(x), u \rangle$$

$$u = -\frac{\nabla f(x)}{\|\nabla f(x)\|} = -\|\nabla f(x)\|^2$$

If $\nabla f(x)$ ≠ zero vector:
$$f'(x;u) = \langle \nabla f(x), -\nabla f(x) \rangle$$