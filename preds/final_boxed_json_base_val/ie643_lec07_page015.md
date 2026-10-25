```markdown
# Handwritten Lecture Note Page

## Equations

1. 
   \[
   m_k = \beta_1 \cdot \text{grad}_k + (1 - \beta_1) \cdot m_{k-1}
   \]

2. 
   \[
   v_k = \beta_2 \cdot (\text{grad}_k^2) + (1 - \beta_2) \cdot v_{k-1}
   \]

3. 
   \[
   w^{k+1} \leftarrow w^k + \eta_k \left( -\frac{m_k}{\sqrt{v_k} + \epsilon} \right)
   \]

## Text

- Sample-based gradient
- $\Delta(y_j, \hat{y}_j)$
```