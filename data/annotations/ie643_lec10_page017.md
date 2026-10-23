$$\vec{w}_j = \begin{bmatrix} w_{j1} \\ w_{j2} \\ w_{j3} \\ \vdots \\ w_{jd} \end{bmatrix}$$

connecting $j^{th}$ neuron in hidden layer from some neuron in prev layer.

$$\hat{y}(x) = \alpha \phi(\vec{w}^T x)$$

$$\hat{y}(x) = \sum_{j=1}^{N} \alpha_j \phi(w_j^T x + b_j)$$

$\alpha_j$: weight connecting $j^{th}$ hidden neuron to o/p neuron
