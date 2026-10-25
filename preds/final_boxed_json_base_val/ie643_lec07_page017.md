```markdown
# Forward Chain Rule

## Diagram: Neural Network Layer Interaction

The diagram illustrates the interaction between neurons across different layers in a neural network.

### Mathematical Formulation

#### Forward Chain Rule
- **i-th neuron in layer l**
  - **z_i** = ∑(w_{ik} * a^{l-1}_k)
  - **a^l_i** = φ(z_i)

#### Partial Derivatives
- $\frac{\partial e}{\partial w_{ij}}$ = $\frac{\partial e}{\partial z_i}$ * $\frac{\partial z_i}{\partial w_{ij}}$
- $\frac{\partial z_i}{\partial w_{ij}}$ = $\frac{\partial e}{\partial z_i}$ * $\frac{\partial a^{l-1}_j}{\partial z_i}$
```