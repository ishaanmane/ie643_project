```markdown
# Iteration

## Initialization
- $\omega^0 = 0 \in \mathbb{R}^d$
- $[0\; 0\; 0\; \ldots\; 0]$

## Until convergence,
- Pick $(x_i, y_i)$ pair from the dataset
- If $\text{sign}(\omega^T x_i) = \text{sign}(y_i)$, do nothing
- Else,
    $$\omega^{t+1} = \omega^t + x_i y_i \quad \leftarrow \text{update rule}$$
```
