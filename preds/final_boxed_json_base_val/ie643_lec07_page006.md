```markdown
# Gradient of a function at a point \( x \)

## Definition

The gradient of a function \( f: \mathbb{R}^n \rightarrow \mathbb{R} \) at a point \( x \) is given by:

\[
\nabla f(x) = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n} \right)
\]

## Directional Derivative

For any vector \( u \):

\[
f'(x; u) = \langle \nabla f(x), u \rangle
\]

## Gradient Vector

Let \( u = -\nabla f(x) \). Then:

\[
u = -\nabla f(x) = -||\nabla f(x)|| e_i
\]

where \( e_i \) is the unit vector in the direction of the \( i \)-th coordinate axis.

## Case when \(\nabla f(x)\) is not zero vector

If \(\nabla f(x) \neq\) zero vector:

\[
f'(x; u) = \langle \nabla f(x), -\nabla f(x) \rangle
\]
```