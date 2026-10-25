$$z^{l+1}_m = \sum_{k=1}^{N_l} w^{l+1}_{mk} \cdot a^l_k$$

$$\frac{\partial e}{\partial a_i^l} = \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial z_m^{l+1}} \cdot w^{l+1}_{mi}$$

$$= \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial a_m^{l+1}} \cdot \frac{\partial a_m^{l+1}}{\partial z_m^{l+1}} \cdot w^{l+1}_{mi} = \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial a_m^{l+1}} \phi'(z_m^{l+1}) \cdot w^{l+1}_{mi}$$