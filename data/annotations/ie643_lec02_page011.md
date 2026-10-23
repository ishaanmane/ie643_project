[Diagram: A perceptron neuron receiving inputs $x_2, x_3, \dots, x_d$ via weights $w_2, \dots, w_d$, computing $\sum_{i=1}^{d} w_i x_i > \theta \Rightarrow$ Yes $\to +1$, No $\to -1$.]

$$\text{Perceptron}(\vec{x}, w, \theta):$$

$$\langle \vec{w}, \vec{x} \rangle - \theta > 0 \implies \vec{x} \to +1$$
$$\langle \vec{w}, \vec{x} \rangle - \theta < 0 \implies \vec{x} \to -1$$
