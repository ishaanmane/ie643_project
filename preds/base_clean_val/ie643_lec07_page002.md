```markdown
# Recap

The diagram illustrates the architecture of a neural network with multiple hidden layers.

## Neural Network Architecture

- **Input Layer**: The input vector `x` is represented as a column vector with dimension `d`.
- **Hidden Layers**: There are `L` hidden layers, each denoted by `D`. The number of neurons in each hidden layer is given by `N1`, `N2`, ..., `NL`.
- **Output Layer**: The output layer computes the predicted label $\hat{y}$ using the formula:
  $$
  \hat{y} = \overrightarrow{a^L} = \phi(\overrightarrow{w^L}) = \phi(W^3\phi(W^2\phi(W^1x)))
  $$
- **Loss Function**: The loss function `e(y, \hat{y})` is used to compare the true label `y` and the predicted label $\hat{y}$.

## Diagram: Neural Network Structure

```
x ∈ R^d
x → [D] → [D] → ... → [D]
      N1        NL
```

## Loss Function

The loss function `e(y, \hat{y})` is defined as:

```
e(y, \hat{y}) → loss fn to compare true and predicted labels
```
```