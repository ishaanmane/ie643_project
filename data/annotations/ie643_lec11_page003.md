$d$-dim i/p. hidden layer: $N$ neuron, 0-1 sigmoid. single o/p neuron: linear act.

[Diagram: $d$ input nodes fully connect to $N$ hidden neurons ($j^{th}$ neuron), which connect via $\alpha_1, \alpha_2, \dots, \alpha_N$ to a single output neuron.]

$$\vec{w}_j = \begin{bmatrix} w_{j1} \\ w_{j2} \\ \vdots \\ w_{jd} \end{bmatrix}$$

"universal approximators"

$$\phi(z) = z$$

$$x \in \mathbb{R}^d, \; x \in [0,1]^d, \qquad \hat{y} = \sum_{j=1}^{N} \alpha_j \left(\phi(\vec{w}_j^T \vec{x} + b_j)\right)$$
