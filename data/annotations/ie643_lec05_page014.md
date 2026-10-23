[Diagram: Neurons $a_1^{l-1}, a_2^{l-1}, \dots, a_{N_{l-1}}^{l-1}$ of layer $l-1$ all connect to the $i^{th}$ neuron of layer $l$.]

$$w_{i1}^l a_1^{l-1} + w_{i2}^l a_2^{l-1} + \cdots + w_{iN_{l-1}}^l a_{N_{l-1}}^{l-1}$$

$$z_i^l = \sum_{j=1}^{N_{l-1}} w_{ij}^l a_j^{l-1}$$

$$a_i^l = \phi(z_i^l)$$

$N_l$: number of neurons in layer $l$
