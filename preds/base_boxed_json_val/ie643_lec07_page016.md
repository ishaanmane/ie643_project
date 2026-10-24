```markdown
# Computation of Sample-based Gradient

The computation of sample-based gradient involves the following steps:

1. **Equation for Sampled Output**:
   \[
   y_j = \phi(w_L \cdots \phi(w_2 \phi(w_1 x_j)) \cdots)
   \]

2. **Derivative Calculation**:
   \[
   D_e(y_j, g_j) \rightarrow w_1, w_2, w_3, \ldots, w_L
   \]

## Auto-differentiation

This process uses auto-differentiation to compute gradients efficiently.
```