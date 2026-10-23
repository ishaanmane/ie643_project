$$\frac{\partial e}{\partial a_i^l} = \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial a_m^{l+1}} \cdot \phi'(z_m^{l+1}) \cdot w_{mi}^{l+1}$$

$$\frac{\partial e}{\partial a_i^l} = \begin{bmatrix} w_{1i}^{l+1} & w_{2i}^{l+1} & \cdots & w_{N_{l+1}\, i}^{l+1} \end{bmatrix} \begin{bmatrix} \frac{\partial e}{\partial a_1^{l+1}} \phi'(z_1^{l+1}) \\ \frac{\partial e}{\partial a_2^{l+1}} \phi'(z_2^{l+1}) \\ \vdots \\ \frac{\partial e}{\partial a_{N_{l+1}}^{l+1}} \phi'(z_{N_{l+1}}^{l+1}) \end{bmatrix}$$

$$= \begin{bmatrix} \frac{\partial e}{\partial a_1^l} \\ \frac{\partial e}{\partial a_2^l} \\ \vdots \\ \frac{\partial e}{\partial a_{N_l}^l} \end{bmatrix}$$
