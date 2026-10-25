$$\nabla_i e(y^i, \hat{y}^i) \rightarrow w^1, w^2, \dots, w^L$$

[Diagram: $j^{th}$ neuron in layer $l-1$ connects via weight $w_{ij}^l$ to $i^{th}$ neuron in layer $l$, which receives multiple inputs.]

$$z_i^l = \sum_{k=1}^{N_{l-1}} w_{ik}^l a_k^{l-1}, \qquad a_i^l = \phi(z_i^l)$$

$$\frac{\partial e}{\partial w_{ij}^l} = \frac{\partial e}{\partial z_i^l} \cdot \frac{\partial z_i^l}{\partial w_{ij}^l} = \frac{\partial e}{\partial z_i^l} \cdot a_j^{l-1} = \frac{\partial e}{\partial a_i^l} \cdot \frac{\partial a_i^l}{\partial z_i^l} \cdot a_j^{l-1}$$
