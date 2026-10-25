```markdown
# Relay

## Partial Derivatives

The partial derivatives of the error function \( e \) with respect to the weights \( w_{ij} \) and activations \( a_i^l \) can be expressed as follows:

1. **Partial derivative of the error with respect to the weight \( w_{ij} \):**

   $$ 
   \frac{\partial e}{\partial w_{ij}} = \frac{\partial e}{\partial z_i^l} \cdot \frac{\partial z_i^l}{\partial w_{ij}}
   $$

2. **Partial derivative of the error with respect to the activation \( a_i^l \):**

   $$ 
   \frac{\partial e}{\partial a_i^l} = \sum_m \frac{\partial e}{\partial z_m^{l+1}} \cdot \frac{\partial z_m^{l+1}}{\partial a_i^l}
   $$

3. **Detailed breakdown of the second equation:**

   $$ 
   \frac{\partial e}{\partial a_i^l} = \sum_m \frac{\partial e}{\partial a_m^{l+1}} \phi'(z_m^{l+1}) w_{mi}^l
   $$

```
```