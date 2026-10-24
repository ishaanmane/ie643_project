```markdown
# Backpropagation Algorithm

## Partial Derivatives

The partial derivative of the error function with respect to the input of the i-th neuron can be expressed as:

$$
\frac{\partial e}{\partial z_i} = \frac{\partial e}{\partial a_i} \cdot \frac{\partial a_i}{\partial z_i}
$$

Where:
- \( e \) is the error function.
- \( a_i \) is the output of the i-th neuron.
- \( z_i \) is the input to the i-th neuron.

### Chain Rule Application

Applying the chain rule, we get:

$$
\frac{\partial e}{\partial z_i} = \frac{\partial e}{\partial a_i} \cdot \phi'(z_i)
$$

Where:
- \( \phi'(z_i) \) is the derivative of the activation function with respect to its input.

## Network Structure

[Diagram: Neural Network]

The network consists of multiple layers, where each layer has neurons connected to the next layer. The connections between neurons are represented by weights.

### Layer Representation

For the l-th layer, the output \( a_i^l \) can be calculated as:

$$
a_i^l = f(z_i^l)
$$

Where:
- \( f \) is the activation function applied to the weighted sum of inputs.
- \( z_i^l \) is the weighted sum of inputs for the i-th neuron in the l-th layer.

### Error Calculation

The error at the output layer (l+1) is calculated as:

$$
\frac{\partial e}{\partial a_i^{l+1}} = \sum_{m=1}^{N_{l+1}} \frac{\partial e}{\partial z_m^{l+1}} \cdot w_{mi}^{l+1}
$$

Where:
- \( N_{l+1} \) is the number of neurons in the (l+1)-th layer.
- \( w_{mi}^{l+1} \) is the weight connecting the m-th neuron in the (l+1)-th layer to the i-th neuron in the l-th layer.

### Propagation of Error

The error propagates back through the network, allowing us to update the weights and biases to minimize the error.

## Summary

The backpropagation algorithm allows us to compute the gradient of the loss function with respect to the weights and biases in a neural network. This gradient is then used to update the weights using an optimization algorithm like gradient descent.
```