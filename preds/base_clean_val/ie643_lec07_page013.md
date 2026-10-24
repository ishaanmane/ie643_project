```markdown
# Mini-batch SGD

The process of mini-batch Stochastic Gradient Descent (SGD) can be described as follows:

1. **Initialization**: Start with the initial weight vector \( w^0 \).

2. **Iterate over epochs**:
   - For each epoch \( k = 0, 1, 2, \ldots \):

     a. **Sample a mini-batch**:
        - Sample a mini-batch \( B_k \subseteq \{1, 2, \ldots, N\} \).
        - This mini-batch contains a subset of the total samples.

     b. **Compute gradients**:
        - For every sample \( j \in B_k \):
          - Compute the partial derivative \( \partial e(y_j, \hat{y}_j) \) with respect to the weights.
          - Here, \( y_j \) is the true label, and \( \hat{y}_j \) is the predicted label.

     c. **Update weights**:
        - Update the weight vector \( w^{k+1} \) using the following formula:
          $$ w^{k+1} \leftarrow w^k + \frac{\eta}{|B_k|} \sum_{j \in B_k} \partial e(y_j, \hat{y}_j) $$
          where \( \eta \) is the learning rate, and \( |B_k| \) is the size of the mini-batch.

3. **Convergence**:
   - The process converges asymptotically as the number of iterations increases.

This method allows for efficient computation by processing a subset of the data at each iteration, which is particularly useful for large datasets.
```