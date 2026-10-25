[Diagram: $a_1, a_2, \dots, a_C$ fully connect to output neurons producing $\hat{y}_1, \hat{y}_2, \dots, \hat{y}_C$.]

$$e = -\sum_{j=1}^{C} y_j \log \hat{y}_j$$

$$\frac{\partial e}{\partial a_j} = \sum_{k=1}^{C} \frac{\partial e}{\partial \hat{y}_k} \cdot \frac{\partial \hat{y}_k}{\partial a_j}$$

$$= \sum_{k=1}^{C} \left(-\frac{y_k}{\hat{y}_k}\right) \left(\frac{\partial \hat{y}_k}{\partial a_j}\right)$$
