## Backpropagation (Recap)

$$\frac{\partial e}{\partial w_{ij}^l} = \frac{\partial e}{\partial z_i^l} \cdot \left(\frac{\partial z_i^l}{\partial w_{ij}^l}\right)$$

$$= \left(\frac{\partial e}{\partial a_i^{l-1}} \cdot a_j^{l-1}\right) \cdot \phi'(z_i^l)$$

$$\frac{\partial e}{\partial a_i^l} = \sum_m \frac{\partial e}{\partial z_m^{l+1}} \cdot \left(\frac{\partial z_m^{l+1}}{\partial a_i^l}\right)$$

$$= \sum_m \frac{\partial e}{\partial a_m^{l+1}} \phi'(z_m^l) w_{mi}^{l+1}$$