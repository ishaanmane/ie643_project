```markdown
# Recay

## Partial Derivatives

### Block 1:
$\frac{\partial e}{\partial w_{ij}} = \frac{\partial e}{\partial z_i^l}$

### Block 2:
$\frac{\partial e}{\partial a_i^{l-1}}$

### Block 3:
$\frac{\partial e}{\partial a_i^l} = \phi'(z_i^l)$

### Block 4:
$$
\frac{\partial e}{\partial a_i^l} = \sum_m \frac{\partial e}{\partial z_m^{l+1}} \cdot \frac{\partial z_m^{l+1}}{\partial a_i^l}
$$

### Block 5:
$$
\frac{\partial e}{\partial a_i^l} = \sum_m \frac{\partial e}{\partial a_m^{l+1}} \cdot \phi'(z_m^l) \cdot w_{mi}
$$
```