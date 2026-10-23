[Diagram: Two neurons in layer $l-1$ ($j^{th}$ neuron, and one above it) connecting via weight $w_{ij}^l$ to the $i^{th}$ neuron in layer $l$.]

$i^{th}$ neuron in layer $l$. $j^{th}$ neuron in layer $l-1$.

**forward chain rule**

$$z_i^l = \sum_{k=1}^{N_{l-1}} w_{ik}^l a_k^{l-1}, \qquad a_i^l = \phi(z_i^l)$$

$$\frac{\partial e}{\partial w_{ij}^l} = \frac{\partial e}{\partial z_i^l} \left(\frac{\partial z_i^l}{\partial w_{ij}^l}\right) = \frac{\partial e}{\partial z_i^l} a_j^{l-1}$$
