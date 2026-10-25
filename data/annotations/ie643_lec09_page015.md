$$\delta^L = \begin{bmatrix} \partial e/\partial a_1^L \\ \partial e/\partial a_2^L \\ \vdots \\ \partial e/\partial a_C^L \end{bmatrix}$$

[Diagram: Output-layer neurons emitting $a_1^L, a_2^L, \dots, a_C^L$.]

$$e^i = -\sum_{j=1}^{C} y_j^i \log \hat{y}_j^i$$

$$\frac{\partial e^i}{\partial a_j^L} = \sum_{k=1}^{C} \frac{\partial e^i}{\partial \hat{y}_k^i} \cdot \frac{\partial \hat{y}_k^i}{\partial a_j^L}$$
