```markdown
# Neural Network Activation Function

## Diagram: Sigmoid Activation Function

The sigmoid activation function is defined as:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

where \( z \) is the weighted sum of inputs.

## Equation: Weighted Sum of Inputs

The weighted sum of inputs can be expressed as:

$$
z = \sum_{j=1}^{d} w_j x_j
$$

Here:
- \( x_j \) represents the input features.
- \( w_j \) represents the weights associated with each feature.
- \( d \) is the number of features.

## Text Block: Learned Parametric Map

The parametric map learned by perception can be represented as:

$$
\widetilde{w} = \begin{bmatrix}
w_1 \\
w_2 \\
w_3 \\
\vdots \\
w_d \\
\end{bmatrix}
$$

This vector contains the learned weights.

## Text Block: Learned by Perception

The parametric map is "learned by perception," indicating that these weights are determined through a learning process rather than being predefined.
```