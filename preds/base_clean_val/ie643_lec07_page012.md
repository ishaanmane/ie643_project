```markdown
# Stochastic Gradient Descent

## Parameter Regime

- $10^6$
- $10^8$
- ...

### Algorithm Overview

#### 1. Define the Data Set
$$
\mathcal{D} = \{(x_i, y_i)\}_{i=1}^{N}
$$

#### 2. Initialize Parameters
$$
w^0
$$

#### 3. Iterate Over Epochs
For $k = 0, 1, 2, \ldots$

#### 4. Compute a Stochastic Gradient
- Randomly choose $j \in \{1, 2, 3, \ldots, N\}$
- Compute $\nabla e(y_j, x_j)$

#### 5. Update Parameters
$$
w^{k+1} \leftarrow w^k - \eta \cdot \nabla e(y_j, x_j)
$$

### Convergence Notes
- Convergence to local optima/saddle points
- Might not lead to descent

```
```