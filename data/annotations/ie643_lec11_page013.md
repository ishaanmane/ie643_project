$f: \mathbb{R}^d \to \mathbb{R}$ is called convex if:

i) $f(\lambda x_1 + (1-\lambda)x_2) \leq \lambda f(x_1) + (1-\lambda)f(x_2) \quad \forall x_1,x_2 \in \mathbb{R}^d, \; \forall \lambda \in [0,1]$

ii)
iii) $\nabla^2 f(z) \geq 0$ (positive semi-definite $\iff$ eigenvalues are non-negative)

$$\nabla^2 f(z) = \begin{bmatrix} \frac{\partial^2 f}{\partial z_1 \partial z_1} & \frac{\partial^2 f}{\partial z_1 \partial z_2} & \cdots & \frac{\partial^2 f}{\partial z_1 \partial z_d} \\ \vdots & & & \vdots \\ \frac{\partial^2 f}{\partial z_d \partial z_1} & \cdots & & \frac{\partial^2 f}{\partial z_d \partial z_d} \end{bmatrix}$$
