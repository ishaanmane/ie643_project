```markdown
# Linear Algebra and Online Learning

## Linear Equation

The equation presented is:

$$
3x_1 + 2x_2 = 3
$$

This can be represented in matrix form as:

$$
\begin{bmatrix}
3 & 2 \\
-1 & -3
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
3 \\
0
\end{bmatrix}
$$

The solution to this system of linear equations is:

$$
\text{sign} = \pm 1
$$

## Online Learning Diagram

[Diagram: Online Learning Flowchart]

The flowchart illustrates the process of online learning over time (t → ∞):

1. At each step t:
   - The current weight vector \( w^t \) is updated based on the input \( x^t \) and the target output \( y^t \).
   - The new weight vector \( w^{t+1} \) is calculated.
   - The process continues iteratively until convergence.

2. The final weight vector \( w^{t+1} \) is used to predict the next target output \( y^{t+1} \).

This iterative process allows the model to adapt and improve its predictions over time.
```