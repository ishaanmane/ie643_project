[Diagram: A feedforward neural network — inputs $a_1, a_2, \dots, a_C$ connect via weights to hidden layer nodes, which connect via weights to output layer nodes $\hat{y}_1, \hat{y}_2, \dots, \hat{y}_C$.]

$$e = -\sum_{j=1}^{C} y_j \log \hat{y}_j$$

$$\frac{\partial e}{\partial a_j} = \sum_{k=1}^{C} \frac{\partial e}{\partial \hat{y}_k} \cdot \frac{\partial \hat{y}_k}{\partial a_j}$$

$$= \sum_{k=1}^{C} -\frac{y_k}{\hat{y}_k} \left(\frac{\partial \hat{y}_k}{\partial a_j}\right)$$