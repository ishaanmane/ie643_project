[Diagram: A feedforward network — inputs $a_1, a_2, \dots, a_c$ connect via weights to hidden layer nodes $\hat{y}_1, \hat{y}_2, \dots, \hat{y}_c$, which connect further to an output node computing $\hat{y}$ (crossed out).]

$$\frac{\partial e}{\partial a_j} = \sum_{k=1}^{C} \frac{\partial e}{\partial \hat{y}_k} \cdot \frac{\partial \hat{y}_k}{\partial a_j}$$

$$= \sum_{k=1}^{C} -\frac{y_k}{\hat{y}_k} \left(\frac{\partial \hat{y}_k}{\partial a_j}\right)$$

$$e = -\sum_{j=1}^{C} y_j \log \hat{y}_j$$