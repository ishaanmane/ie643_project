```markdown
# Handwritten Lecture Note Page

## Linear Classification

The handwritten notes appear to be discussing linear classification, specifically the perceptron algorithm or a similar linear decision boundary model.

### Notations

- $\vec{\omega}$: Weights vector
- $\vec{x}$: Input vector
- $\theta$: Bias term

### Equations

1. **Weight Vector Representation**
   - $\vec{\omega} = \begin{bmatrix}
   w_1 \\
   w_2 \\
   \vdots \\
   w_d \\
   -\theta
   \end{bmatrix}$

2. **Input Vector Representation**
   - $\vec{x} = \begin{bmatrix}
   x_1 \\
   x_2 \\
   \vdots \\
   x_d \\
   1
   \end{bmatrix}$

3. **Decision Rule**
   - $\sum_{j=1}^{d} w_j x_j \geqslant 0$
   - $\langle \vec{\omega}, \vec{x} \rangle - \theta \geqslant 0$

4. **Classification Conditions**
   - $\langle \vec{\omega}, \vec{x} \rangle - \theta < 0$

5. **Another Perspective on Weights and Input**
   - $\vec{\omega} = \begin{bmatrix}
   w_1 \\
   w_2 \\
   \vdots \\
   w_d
   \end{bmatrix}$
   - $\vec{x} = \begin{bmatrix}
   x_1 \\
   x_2 \\
   \vdots \\
   x_d
   \end{bmatrix}$

6. **Decision Boundary Conditions**
   - $\langle \vec{\omega}, \vec{x} \rangle \geqslant 0$
   - $\langle \vec{\omega}, \vec{x} \rangle < 0$

### Diagrams

[Diagram: Weight and Input Vectors]

```