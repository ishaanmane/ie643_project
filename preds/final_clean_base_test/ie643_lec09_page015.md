```markdown
$\delta = \left( \frac{\partial e}{\partial a_1^L}, \frac{\partial e}{\partial a_2^L}, \ldots, \frac{\partial e}{\partial a_c^L} \right)$

## Diagram: Neural Network Layers

[Diagram: A neural network with three layers (input, hidden, output) connected by arrows indicating the direction of data flow.]

### Output Layer Calculation

$$
e^i = -\sum_{j=1}^{c} y_j \log(y_j)
$$

### Backpropagation Formula

$$
\frac{\partial e^i}{\partial a^L_k} = \sum_{k=1}^{c} \frac{\partial e^i}{\partial y_k} \cdot \frac{\partial y_k}{\partial a^L_j}
$$
```