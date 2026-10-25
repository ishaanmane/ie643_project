```markdown
# Handwritten Lecture Note Page

## Diagram: Neural Network Structure

The diagram illustrates a neural network with multiple layers. The input layer has nodes labeled \(a_1\) through \(a_c\). Each node in the hidden layer is connected to all nodes in the input layer, indicated by arrows pointing from the input layer to the hidden layer. The output layer has nodes labeled \(\hat{y}_1\) through \(\hat{y}_c\).

## Equations

### Loss Function

The loss function \(L\) is defined as:
\[ L = -\sum_{j=1}^{C} y_j \log \hat{y}_j \]

### Partial Derivative of Loss Function

The partial derivative of the loss function with respect to \(a_j\) is given by:
\[ \frac{\partial L}{\partial a_j} = \sum_{k=1}^{C} \frac{\partial L}{\partial \hat{y}_k} \cdot \frac{\partial \hat{y}_k}{\partial a_j} \]

### Simplified Form

Simplifying the above equation, we get:
\[ \frac{\partial L}{\partial a_j} = \sum_{k=1}^{C} \left( \frac{\partial \hat{y}_k}{\partial a_j} \right) \]
```