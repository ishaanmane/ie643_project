$$\frac{\partial e}{\partial z_i^l} = \left(\frac{\partial a_i^l}{\partial z_i^l}\right) \cdot \phi'(z_i^l) = \frac{\partial e}{\partial a_i^l} \cdot \phi'(z_i^l)$$

[Diagram: A neuron $a_i^l$ (layer $l$) feeding into $N_{l+1}$ neurons of layer $l+1$, labeled $z_m^{l+1}, a_m^{l+1}$ ($m=1,\dots,N_{l+1}$).]

$$\frac{\partial e}{\partial a_i^l} = \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial z_m^{l+1}} \cdot \left(\frac{\partial z_m^{l+1}}{\partial a_i^l}\right) = \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial z_m^{l+1}} \cdot w_{mi}^{l+1}$$