[Diagram: A chain of neurons — input layer neuron → $j^{th}$ neuron in layer $l-1$ → $i^{th}$ neuron in layer $l$.]

$i^{th}$ neuron in layer $l$, $j^{th}$ neuron in layer $l-1$: $w_{ij}^l$

$$\frac{\partial e}{\partial w_{ij}^l} = \frac{\partial e}{\partial z_i^l} \cdot \boxed{\frac{\partial z_i^l}{\partial w_{ij}^l}}$$

forward chain rule:
$$z_i^l = \sum_{k=1}^{N_{l-1}} w_{ik}^l a_k^{l-1}$$
$$a_i^l = \phi(z_i^l)$$
$$= \frac{\partial e}{\partial z_i^l} a_j^{l-1}$$