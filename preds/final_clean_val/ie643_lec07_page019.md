$$z^{l+1}_m = \sum_{k=1}^{N_l} w_{mk}^{l+1} a_k^l$$

$$\frac{\partial e}{\partial a_i^l} = \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial z_m^{l+1}} \cdot w_{mi}^{l+1}$$

$$= \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial a_m^{l+1}} \cdot \frac{\partial a_m^{l+1}}{\partial z_m^{l+1}} \cdot w_{mi}^{l+1}$$

$$= \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial a_m^{l+1}} \phi'(z_m^{l+1}) \cdot w_{mi}^{l+1}$$