```markdown
# Handwritten Lecture Note Page

## Mathematical Equations

The handwritten notes contain three main mathematical equations:

### Equation 1
$$
z_{m}^{l+1} = \sum_{k=1}^{N_{\ell}} w_{mk}^{l+1} \cdot a_{k}^{\ell}
$$

### Equation 2
$$
\frac{\partial e}{\partial a_i} = \sum_{m=1}^{N_{\ell+1}} \frac{\partial e}{\partial z_m^{\ell+1}} \cdot w_{mi}^{\ell+1}
$$

### Equation 3
$$
= \sum_{m=1}^{N_{\ell+1}} \frac{\partial e}{\partial a_m^{\ell+1}} \cdot \frac{\partial a_m^{\ell+1}}{\partial z_m^{\ell+1}} \cdot w_{mi}^{\ell+1}
$$

### Equation 4
$$
= \sum_{m=1}^{N_{\ell+1}} \frac{\partial e}{\partial a_m^{\ell+1}} \phi'(z_m^{\ell+1}) \cdot w_{mi}^{\ell+1}
$$
```