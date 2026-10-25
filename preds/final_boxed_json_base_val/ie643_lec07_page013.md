```markdown
# Mini-batch SGD

## Algorithm Description

The algorithm for mini-batch Stochastic Gradient Descent (SGD) is described below:

### 1. Initialize Parameters
- $D = \{(x_i, y_i)\}_{i=1}^N$: The dataset consisting of N samples.

### 2. Iterate over epochs
- For $k = 0, 1, 2, \ldots$

### 3. Sample a mini-batch
- Sample a mini-batch of samples from the dataset.
- Let $B_k \subseteq \{1, 2, \ldots, N\}$ be the indices of the sampled mini-batch.

### 4. Compute gradients for the mini-batch
- For every $j \in B_k$, compute $\nabla L(y_j, \hat{y}_j)$.

### 5. Update weights
- $w^{k+1} \leftarrow w^k - \frac{\eta}{|B_k|} \sum_{j \in B_k} \nabla L(y_j, \hat{y}_j)$

### Convergence in Asymptotic Sense
- The algorithm converges asymptotically.

```
```