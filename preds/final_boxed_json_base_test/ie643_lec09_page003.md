```markdown
# Handwritten Lecture Note Page

## Main Equation

The main equation presented on the page is:

$$
\left( \frac{\partial e}{\partial a^l_1}, \frac{\partial e}{\partial a^l_2}, \ldots, \frac{\partial e}{\partial a^{l+1}_{N_{l+1}}} \right)^T = W^{l+1} \text{Diag}\left(\phi'(z^{l+1})\right)
$$

This equation represents the gradient of the error function with respect to the activations at layer \( l+1 \). The right-hand side involves the weight matrix \( W^{l+1} \) and the diagonal matrix formed by the derivative of the activation function \( \phi' \) evaluated at the activations \( z^{l+1} \).

### Vanishing/Exploding Gradient Issue

Below the main equation, there is a note indicating the issue of vanishing/exploding gradients:

- **Vanishing Gradient**: This occurs when the gradients become very small during backpropagation, leading to slow learning.
- **Exploding Gradient**: This happens when the gradients become very large, potentially causing numerical instability.

## Left Block

On the left block, the partial derivatives of the error function with respect to the activations at layer \( l \) are written:

$$
\frac{\partial e}{\partial a^l_1}, \frac{\partial e}{\partial a^l_2}, \ldots, \frac{\partial e}{\partial a^l_{N_l}}
$$

These represent the gradients of the error function with respect to the activations at layer \( l \).

## Right Block

On the right block, the partial derivatives of the error function with respect to the activations at layer \( l+1 \) are written:

$$
\frac{\partial e}{\partial a^{l+1}_1}, \frac{\partial e}{\partial a^{l+1}_2}, \ldots, \frac{\partial e}{\partial a^{l+1}_{N_{l+1}}}
$$

These represent the gradients of the error function with respect to the activations at layer \( l+1 \).
```