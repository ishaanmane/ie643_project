$$x_1 + x_2 = 4 \Rightarrow \vec{w} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$

$$\langle \begin{bmatrix} w_1 \\ w_2 \end{bmatrix}, \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \rangle = 4 = 0$$

$$\text{sign}(z) = +1, z \geq 0$$
$$= -1, \text{otherwise}$$

$$\vec{\tilde{w}} = \vec{w} + y \vec{\tilde{x}}$$
$$= \begin{bmatrix} 1 \\ 1 \\ -4 \end{bmatrix} \quad (x,y) \rightarrow ((2,1),+1)$$
$$\vec{\tilde{x}} = \begin{bmatrix} 2 \\ 1 \\ 1 \end{bmatrix}$$

$$\vec{\tilde{w}} = \begin{bmatrix} 1 \\ -4 \end{bmatrix} + \begin{bmatrix} 2 \\ 1 \end{bmatrix}$$

$$\text{Perceptron}(\vec{\tilde{x}}) = \text{sign}(\langle \vec{\tilde{w}}, \vec{\tilde{x}} \rangle) = -1$$