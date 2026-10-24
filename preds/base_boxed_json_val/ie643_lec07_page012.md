```markdown
# Stochastic Gradient Descent

## Parameter Regime

- $10^6$
- $10^8$

### Stochastic Approximation

#### Convergence to Local Optima/Saddle Points

- $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^{N}$

#### Update Rule

$$
w^{k+1} \leftarrow w^k + \eta \nabla f(w^k)
$$

#### Potential Issues

- Might not lead to descent

### Algorithm Steps

1. Initialize weights: $w^0$
2. For $k = 0, 1, 2, \ldots$

#### Compute a Stochastic Gradient

- Randomly choose $j \in \{1, 2, 3, \ldots, N\}$
- Compute $\nabla f(y_j, x_j)$
```