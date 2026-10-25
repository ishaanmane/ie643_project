[Diagram: A neuron receiving inputs $x_1, x_2, \dots, x_d$ via weights $w_1, w_2, \dots, w_d$, computing $\sum_{j=1}^{d} w_j x_j$, with an output branch "$\geq \theta \to +1$" and "$< \theta \to -1$".]

$$\tilde{W} = \begin{bmatrix} w_1 \\ w_2 \\ w_3 \\ \vdots \\ w_d \\ -\theta \end{bmatrix}$$

$$h_w \equiv F \quad \text{parametric map learned by perceptron}$$