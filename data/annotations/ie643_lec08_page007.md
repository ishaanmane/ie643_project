$$= \frac{\partial e}{\partial a_i^l} \cdot \phi'(z_i^l) \cdot a_j^{l-1}$$

[Diagram: $i^{th}$ neuron of layer $l$ connects forward to several neurons of layer $l+1$ (activations $z_1^{l+1}, a_1^{l+1}$; $z_2^{l+1}, a_2^{l+1}$; ...; $z_{N_{l+1}}^{l+1}, a_{N_{l+1}}^{l+1}$).]

$$\frac{\partial e}{\partial a_i^l} = \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial z_m^{l+1}} \cdot \frac{\partial z_m^{l+1}}{\partial a_i^l} = \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial z_m^{l+1}} \cdot w_{mi}^{l+1}$$

$$= \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial a_m^{l+1}} \cdot \frac{\partial a_m^{l+1}}{\partial z_m^{l+1}} \cdot w_{mi}^{l+1}$$

$$z_m^{l+1} = \sum_{k=1}^{N_l} w_{mk}^{l+1} a_k^{l}$$
