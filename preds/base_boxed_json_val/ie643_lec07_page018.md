```markdown
# Handwritten Lecture Note Page

## Equations

1. $\frac{\partial e}{\partial z^l_i} = \frac{\partial e}{\partial a^l_i} \left( \frac{\partial a^l_i}{\partial z^l_i} \right)$
   - $\phi'(z^l_i)$
   - $\frac{\partial e}{\partial a^l_i}$

2. $\frac{\partial e}{\partial a^l_i} = \sum_{m=1}^{N_{\ell+1}} \frac{\partial e}{\partial z^{\ell+1}_m} \cdot \frac{\partial z^{\ell+1}_m}{\partial a^l_i}$

## Figure

[Diagram: Neural Network Layer]

- $i^{th}$ neuron
- $a_i$
- $z_m^{\ell+1}$
- $a_m^{\ell+1}$

## Equations

3. $\frac{\partial e}{\partial z^{\ell+1}_m} = \sum_{i=1}^{N_{\ell+1}} \frac{\partial e}{\partial z^{\ell+1}_m} \cdot w_{mi}^{\ell+1}$
```