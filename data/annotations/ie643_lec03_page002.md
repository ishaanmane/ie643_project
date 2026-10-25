[Diagram: A perceptron neuron receiving inputs $x_1, x_2, x_3, x_4, \dots, x_d$ via weights $w_1, w_2, w_3, w_4, \dots, w_d$, computing $\sum_{j=1}^{d} w_j x_j$, output $\geq \theta \to +1$, $< \theta \to -1$.]

$$\tilde{w} = \begin{bmatrix} w_1 \\ w_2 \\ w_3 \\ \vdots \\ w_d \\ -\theta \end{bmatrix}$$

> $h_{\tilde{w}}$ — parametric map learned by perceptron
