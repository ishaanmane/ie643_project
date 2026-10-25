```markdown
# Neural Network Diagram

## Forward Chain Rule

The forward chain rule is used to compute the gradient of the loss function with respect to the weights in a neural network.

### Diagram: Neural Network Layer Interaction

```
jth neuron
in layer l-1
```

[Diagram: A diagram showing connections between neurons across layers]

```
i th neuron
in layer l
```

### Mathematical Formulation

#### Forward Chain Rule

$$
\frac{\partial e}{\partial w_{ij}} = \frac{\partial e}{\partial z_i} \cdot \frac{\partial z_i}{\partial w_{ij}}
$$

#### Activation Function

$$
a^l_i = \phi(z^l_i)
$$

#### Input to Neuron

$$
z_i^l = \sum_{k=1}^{N_{l-1}} w_{ik}^l a_{k}^{l-1}
$$

#### Output of Neuron

$$
a_i^l = \phi(z_i^l)
$$

#### Gradient Calculation

$$
\frac{\partial e}{\partial w_{ij}} = \frac{\partial e}{\partial z_i} \cdot \frac{\partial z_i}{\partial w_{ij}}
$$

#### Backward Pass

$$
\frac{\partial e}{\partial z_i} = \frac{\partial e}{\partial a_j^{l-1}}
$$
```