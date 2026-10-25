$$\frac{\partial e}{\partial z^l_i} = \frac{\partial e}{\partial a^l_i} \left(\frac{\partial a^l_i}{\partial z^l_i}\right) = \frac{\partial e}{\partial a^l_i} \cdot \phi'(z^l_i)$$

$$\frac{\partial e}{\partial a^l_i} = \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial z^{l+1}_m} \cdot \left(\frac{\partial z^{l+1}_m}{\partial a^l_i}\right) = \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial z^{l+1}_m} \cdot w^{l+1}_{m,i}$$

[Diagram: A neuron $a^l_i$ (layer $l$ input) feeding into multiple neurons of layer $l+1$, labeled $z_m^{l+1}$ and $a_m^{l+1}$.]