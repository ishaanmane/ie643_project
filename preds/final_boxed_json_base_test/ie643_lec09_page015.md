```markdown
# Handwritten Lecture Note Page

## Left Block: Equation

$\delta^L = \begin{pmatrix}
\frac{\partial e}{\partial a_L^1} \\
\frac{\partial e}{\partial a_L^2} \\
\vdots \\
\frac{\partial e}{\partial a_L^c}
\end{pmatrix}$

## Middle Block: Diagram

[Diagram: A flowchart with nodes labeled \(a_L^1\), \(a_L^2\), ..., \(a_L^c\). Arrows point from each node to the next.]

## Right Block: Equations

$$
e_i^i = -\sum_{j=1}^{c} y_j \log y_j
$$

$$
\frac{\partial e_i^i}{\partial a_L^k} = \sum_{k=1}^{c} \frac{\partial e_i^i}{\partial y_k} \cdot \frac{\partial y_k}{\partial a_L^j}
$$
```