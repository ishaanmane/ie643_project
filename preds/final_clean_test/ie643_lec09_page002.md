## Backward Pass (Recall)

$$\frac{\partial e}{\partial w_{ij}^l} = \frac{\partial e}{\partial z_i^l} \cdot \left(\frac{\partial z_i^l}{\partial w_{ij}^l}\right)$$

[Diagram: A chain of nodes $a_j^{l-1}$ feeding into $z_i^l$, which feeds into $a_i^l$.]

$$\frac{\partial e}{\partial a_i^l} = \sum_m \frac{\partial e}{\partial a_m^{l+1}} \cdot \left(\frac{\partial z_m^{l+1}}{\partial a_i^l}\right)$$

$$\frac{\partial e}{\partial a_i^l} = \sum_m \frac{\partial e}{\partial a_m^{l+1}} \phi'(z_m^{l+1}) w_{mi}^l$$