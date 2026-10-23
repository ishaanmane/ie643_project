# Kernel Regression

$$w^* = (XX^T)^+Xy$$

$w^*$ must lie on the span of the data points.

[Diagram: A green-shaded 2D plane in 3D space with several small black arrows radiating from the origin within the plane, a vector $\tilde{w}$ pointing to a point on the plane, and $w^*$ pointing above the plane with a dotted perpendicular connecting to $\tilde{w}$.]

$w^* \leftarrow$ it minimizes the sum of square errors.

2D plane in the 3D space where all our data points are lying on.

$$w^* = \tilde{w} + \tilde{w}_\perp$$
$$w^*x_i = (\tilde{w}+\tilde{w}_\perp)x_i = \tilde{w}x_i + \underbrace{\tilde{w}_\perp x_i}_{0 \text{ as orthogonal}}$$

$$\therefore \sum_{i=1}^{n}(w^*x_i-y_i) = \sum_{i=1}^{n}(\tilde{w}x_i-y_i)$$

$w^* = $ some linear combination of data points.
$w^* = X\alpha^*$ for some $\alpha^* \in \mathbb{R}^n$

But we know $w^* = (XX^T)^+Xy$

$$\therefore X\alpha^* = (XX^T)^+Xy$$
$$(XX^T)X\alpha^* = (XX^T)(XX^T)^+Xy$$
