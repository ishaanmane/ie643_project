[Diagram: Inputs $x_1, x_2$ connect to two layer-1 neurons via weights $p, q$ (into 1st neuron, with bias $b_1$ via input "1") and $r, s$ (into 2nd neuron, with bias $b_2$).]

$1^{st}$ neuron $\rightarrow z_1^1 = px_1 + qx_2$ (neuron id + $b_1$)
$$a_1^1 = \text{ReLU}(z_1^1)$$

$2^{nd}$ neuron $\rightarrow z_2^1 = rx_1 + sx_2 + b_2$
$$a_2^1 = \text{ReLU}(z_2^1)$$
