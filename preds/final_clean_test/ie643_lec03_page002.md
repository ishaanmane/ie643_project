[Diagram: A perceptron neuron — inputs $x_1, x_2, \dots, x_d$ each with weight $w_1, w_2, \dots, w_d$, feeding into a dot-product sum $\sum_{j=1}^{d} w_j x_j$. The output branch splits: $\geq\theta \to +1$, $<\theta \to -1$.]

$$\tilde{W} = \begin{bmatrix} w_1 \\ w_2 \\ w_3 \\ \vdots \\ w_d \\ \theta \end{bmatrix}$$

$h_w \equiv F$ — parametric map learned by perceptron