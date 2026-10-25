```markdown
# Computation of Sample-based Gradient

The computation of the sample-based gradient involves the following steps:

1. **Forward Pass**:
   - Compute the output \( y_j \) using the formula:
     $$ y_j = \phi(w_L \cdots \phi(w_2 \phi(w_1 x_i))) $$
   - Here, \( w_1, w_2, \ldots, w_L \) represent the weights of the neural network.

2. **Backward Pass**:
   - Calculate the derivative of the loss function with respect to the output \( y_j \):
     $$ D_e(y_j, g_j) $$
   - This step is crucial for updating the weights during backpropagation.

3. **Weight Update**:
   - The gradients computed in the backward pass are used to update the weights:
     $$ w_1, w_2, \ldots, w_L $$

## Auto-differentiation

Auto-differentiation is a technique that automatically computes the derivatives of functions defined by computer programs. It is essential for computing gradients efficiently in machine learning models.
```