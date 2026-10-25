# Optimizing the Error Function

Linear Regression: $\min_{w\in\mathbb{R}^d} \sum_{i=1}^{n}(w^Tx_i-y_i)^2$

In terms of matrices: $\min_{w\in\mathbb{R}^d} \|X^Tw-y\|^2$

$$X^T = \begin{bmatrix} -x_1- \\ -x_2- \\ \vdots \\ -x_n- \end{bmatrix} (n\times d), \quad w = \begin{bmatrix}\vdots\\w\\\vdots\end{bmatrix} (d\times1), \quad y = \begin{bmatrix}y_1\\\vdots\\y_n\end{bmatrix} (n\times d)$$

$$= \min_{w\in\mathbb{R}^d} (X^Tw-y)^T(X^Tw-y) \leftarrow \text{unconstrained quadratic (in $w$) optimization problem}$$

We can solve this optimisation problem by taking derivative (gradient) & setting it to 0.

$$f(w) = (X^Tw-y)^T(X^Tw-y)$$
$$\nabla f(w) = 2(XX^T)w - 2Xy = 0$$
$$\boxed{(XX^T)w^* = Xy}$$
$$w^* = (XX^T)^+Xy \quad \leftarrow \text{pseudoinverse}$$
