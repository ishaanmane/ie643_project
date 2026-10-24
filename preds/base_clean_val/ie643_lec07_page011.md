```markdown
# Gradient Descent Algorithm

## Objective
Minimize the error function \( E \) with respect to the weights \( w \).

### Error Function
\[ E = \sum_{i=1}^{N} e(y_i, \hat{y}_i) \]

### Gradient Calculation
- **Full Gradient**: 
  \[ \nabla E = \sum_{i=1}^{N} \nabla e(y_i, \hat{y}_i) \]
- **Sample-based Gradient**:
  \[ \nabla E = \sum_{i=1}^{N} \nabla e(y_i, \hat{y}_i) \]

### Algorithm Steps
For \( k = 0, 1, 2, \ldots \):

1. **Find Descent Direction**:
   \[ -\nabla E(w_k) \]

2. **Find a Suitable Step Length**:
   \[ \alpha_k \]

3. **Update Weights**:
   \[ w^{k+1} \leftarrow w^k + \alpha_k (-\nabla E(w_k)) \]

4. **Zero-gradient Check to Stop the Process**:

### Notes
- \( \epsilon_k \): Fixed to be small value close to zero.
- \( 10^{-5}, 10^{-8} \): Small values chosen to ensure convergence.

```
```