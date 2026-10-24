```markdown
# Gradient of a Function at a Point x

The gradient of a function \( f \) at a point \( x \in \mathbb{R}^n \rightarrow \mathbb{R} \) is given by:

\[
\nabla f(x) = \left[ \begin{array}{c}
\frac{\partial f}{\partial x_1} \\
\frac{\partial f}{\partial x_2} \\
\vdots \\
\frac{\partial f}{\partial x_n}
\end{array} \right]
\]

## Directional Derivative

The directional derivative of \( f \) at \( x \) in the direction of a vector \( u \) is defined as:

\[
f'(x; u) = \langle \nabla f(x), u \rangle
\]

### Special Case: Negative Gradient

If \( u = -\nabla f(x) \), then:

\[
f'(x; u) = \langle \nabla f(x), -\nabla f(x) \rangle
\]

If \( \nabla f(x) \neq 0 \):

\[
f'(x; u) = \langle \nabla f(x), -\nabla f(x) \rangle
\]

This expression represents the dot product of the gradient with itself, which can be further simplified using the norm of the gradient.
```