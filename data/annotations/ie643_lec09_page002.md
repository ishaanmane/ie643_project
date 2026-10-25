## Recap

$$\frac{\partial e}{\partial w_{ij}^l} = \frac{\partial e}{\partial z_i^l} \underbrace{\left(\frac{\partial z_i^l}{\partial w_{ij}^l}\right)}_{a_j^{l-1}}$$

$$\rightarrow \frac{\partial e}{\partial a_i^l} \cdot \phi'(z_i^l)$$

$$\frac{\partial e}{\partial a_i^l} = \sum \frac{\partial e}{\partial z_m^{l+1}} \cdot \left(\frac{\partial z_m^{l+1}}{\partial a_i^l}\right)_{w_{mi}^{l+1}}$$

$$\frac{\partial e}{\partial a_i^l} = \sum \frac{\partial e}{\partial a_m^{l+1}} \phi'(z_m^{l+1}) w_{mi}^l$$
