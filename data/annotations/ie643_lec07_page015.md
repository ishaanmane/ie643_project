$$m_k = \beta_1 \cdot \text{grad}_k + (1-\beta_1) m_{k-1}$$
$$v_k = \beta_2 \cdot (\text{grad}_k^2) + (1-\beta) v_{k-1}$$

$$w^{k+1} \leftarrow w^k + \eta_k \left(-\frac{m_k}{\sqrt{v_k} + \epsilon}\right)$$

**Sample-based gradient**

$$\nabla e(y^j, \hat{y}^j)$$
