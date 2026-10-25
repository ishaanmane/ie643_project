## Error gradients computation: (Backpropagation of error grads from $L, L-1, L-2, \dots, l^{th}$ layer)

$$\nabla_{W^l} e = \text{Diag}(\phi'(z^l)) \cdot \delta^l \cdot (a^{l-1})^T$$

connects $l^{th}$ layer neurons from $(l-1)^{th}$ layer neurons

$$\delta^l = \begin{bmatrix} \partial e/\partial a_1^l \\ \partial e/\partial a_2^l \\ \vdots \\ \partial e/\partial a_{N_l}^l \end{bmatrix} = (W^{l+1})^T \, \text{Diag}(\phi'(z^{l+1})) \, \delta^{l+1}$$
