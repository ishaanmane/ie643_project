$$\delta^L = \begin{bmatrix} \frac{\partial e}{\partial a_1^L} \\ \frac{\partial e}{\partial a_2^L} \\ \vdots \\ \frac{\partial e}{\partial a_C^L} \end{bmatrix}$$

[Diagram: A chain of neurons $a_1^L \to a_2^L \to \cdots \to a_C^L$, each feeding into the next.]

$$e^i = -\sum_{j=1}^{C} y_j \log \hat{y}_j^i$$

$$\frac{\partial e^i}{\partial a_k^L} = \sum_{k=1}^{C} \frac{\partial e^i}{\partial \hat{y}_k^i} \cdot \frac{\partial \hat{y}_k^i}{\partial a_j^L}$$