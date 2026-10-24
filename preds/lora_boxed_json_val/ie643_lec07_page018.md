$$\frac{\partial e}{\partial z_i^l} = \left(\frac{\partial a_i^l}{\partial z_i^l}\right) \left(\frac{\partial e}{\partial a_i^l}\right) = \frac{\partial e}{\partial a_i^l} \cdot \phi'(z_i^l)$$

$$\frac{\partial e}{\partial a_i^l} = \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial z_m^{l+1}} \cdot \frac{\partial z_m^{l+1}}{\partial a_i^l}$$

[Diagram: A neuron $a_i^l$ (layer $l$) connects via two edges to neurons $z_m^{l+1}$ and $a_m^{l+1}$ (layer $l+1$).]

$$\frac{\partial z_m^{l+1}}{\partial a_i^l} = \sum_{i=1}^{N_{l+1}} \frac{\partial e}{\partial z_m^{l+1}} \cdot w_{mi}^{l+1}$$