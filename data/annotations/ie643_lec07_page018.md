$$\frac{\partial e}{\partial z_i^l} = \frac{\partial e}{\partial a_i^l} \left(\frac{\partial a_i^l}{\partial z_i^l}\right) = \frac{\partial e}{\partial a_i^l} \cdot \phi'(z_i^l)$$

$$\frac{\partial e}{\partial a_i^l} = \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial z_m^{l+1}} \left(\frac{\partial z_m^{l+1}}{\partial a_i^l}\right) = \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial z_m^{l+1}} \cdot w_{mi}^{l+1}$$

[Diagram: $i^{th}$ neuron in layer $l$ (activation $a_i^l$) connecting forward to multiple neurons in layer $l+1$ (activations $z_m^{l+1}, a_m^{l+1}$).]
