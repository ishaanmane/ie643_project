[Diagram: A feedforward neural network with input layer nodes $a_1, a_2, \dots, a_c$, fully connecting to an output layer node (neuron) computing $\hat{y}_j$ for each of $c$ outputs.]

$$\frac{\partial e}{\partial a_j} = \sum_{k=1}^{c} \frac{\partial e}{\partial \hat{y}_k} \cdot \frac{\partial \hat{y}_k}{\partial a_j}$$

$$= \sum_{k=1}^{c} -\frac{y_k}{\hat{y}_k} \left(\frac{\partial \hat{y}_k}{\partial a_j}\right)$$

$$e = -\sum_{j=1}^{c} y_j \log \hat{y}_j$$