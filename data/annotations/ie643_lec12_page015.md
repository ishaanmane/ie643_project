$$X = \begin{bmatrix} \uparrow & \uparrow & & \uparrow \\ x^1 & x^2 & \cdots & x^S \\ \downarrow & \downarrow & & \downarrow \end{bmatrix}_{n \times S}$$

$$A^TA \, B^* \, XX^T = A^T Y X^T$$
$$\boxed{A^TA \, B^* \, \Sigma_{xx} = A^T \Sigma_{yx}}$$

$XX^T$ = feature covariance matrix ($n \times n$ matrix)

$$XX^T = \sum_{s=1}^{S} x^s(x^s)^T, \qquad YX^T = \sum_{s=1}^{S} y^s(x^s)^T$$
$$XY^T = \sum_{s=1}^{S} x^s(y^s)^T$$

Assume: $\Sigma_{xx}$ is invertible, $A$ is full rank $\Rightarrow A^TA$ is also inv.
