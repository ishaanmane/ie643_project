```markdown
# Gradient Descent with Momentum

## Key Equations

1. **Momentum Update**:
   \[
   m_k = \beta_1 \cdot \text{grad}_k + (1 - \beta_1) \cdot m_{k-1}
   \]

2. **Velocity Update**:
   \[
   v_k = \beta_2 \cdot (\text{grad}_k^2) + (1 - \beta_2) \cdot v_{k-1}
   \]

3. **Weight Update**:
   \[
   w^{k+1} \leftarrow w^k + \eta_k \left( -\frac{m_k}{\sqrt{v_k} + \epsilon} \right)
   \]

## Sample-based Gradient

The sample-based gradient is denoted as:

\[
\text{Del}(y_j, \hat{y}_j)
\]
```
