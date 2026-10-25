## Computation of sample-based gradient

$$\hat{y}^j = \phi(W^L \phi(W^{L-1} \phi(W^2 \phi(W^1 x^j)) \cdots))$$

$$\nabla e(y^j, \hat{y}^j) \rightarrow w^1, w^2, w^3, \dots, w^L$$

auto-differentiation