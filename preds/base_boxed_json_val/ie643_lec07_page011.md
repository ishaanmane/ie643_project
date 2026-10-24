```markdown
# Optimization Algorithm

## Objective Function
The objective function \( E \) is defined as:
\[ E = \sum_{i=1}^{N} e(y_i, \hat{y}_i) \]

## Gradient Calculation
The gradient of \( E \) with respect to \( w \) can be computed as:
\[ \nabla E = \sum_{i=1}^{N} \nabla e(y_i, \hat{y}_i) \]

### Full Gradient vs Sample-based Gradient
- **Full Gradient**: Computes the gradient using all data points.
- **Sample-based Gradient**: Computes the gradient using a subset of data points.

## Iterative Optimization Process
For \( k = 0, 1, 2, \ldots \):

1. **Find Descent Direction**:
   - Compute the negative gradient: \( -\nabla E(w^k) \).

2. **Find Step Length**:
   - Determine a suitable step length \( \alpha_k \).

3. **Update Weights**:
   - Update the weights: \( w^{k+1} \leftarrow w^k + \alpha_k (-\nabla E(w^k)) \).

4. **Zero-gradient Check**:
   - Stop the process if the gradient is zero.

## Additional Notes
- \( \epsilon_k \): Fixed to be a small value close to zero.
- Step-length finding procedures are discussed.
```