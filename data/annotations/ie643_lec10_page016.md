## MLP

$x \in \mathbb{R}^d$, &nbsp; $x \in [0,1]^d$ &nbsp; $d$ input, &nbsp; $N$ hidden neurons

[Diagram: $d$ input nodes fully connect (weight vector $\vec{w}_j$) to $N$ hidden-layer nodes ($j$-th neuron shown), each hidden neuron connects via $\alpha_1, \alpha_2, \dots, \alpha_N$ to a single output neuron.]

hidden layer neurons: 0-1 sigmoid
output: linear activation, $\phi(z) = z$

$$\hat{y}(x) = \sum \alpha_j w_j$$
