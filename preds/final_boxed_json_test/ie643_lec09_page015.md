$$\delta^L = \begin{bmatrix} \frac{\partial e}{\partial a_1^L} \\ \frac{\partial e}{\partial a_2^L} \\ \vdots \\ \frac{\partial e}{\partial a_C^L} \end{bmatrix}$$

[Diagram: A chain of neurons — input layer neuron → $a_1^L$, $a_2^L$, $\dots$, $a_C^L$.]

$$e^i = -\sum_{j=1}^{C} y_j^i \log y_j^i$$

$$\frac{\partial e^i}{\partial a_j^L} = \sum_{k=1}^{C} \frac{\partial e^i}{\partial \hat{y}_k^i} \cdot \frac{\partial \hat{y}_k^i}{\partial a_j^L}$$