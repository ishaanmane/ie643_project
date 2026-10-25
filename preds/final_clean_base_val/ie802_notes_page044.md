```markdown
# Step (4) and $\alpha x + \beta y \leq \beta$

## Valid for both R1 and R2

- Use R1, R2...
- Together to Red line.
- There are lots of lines like the Red line (infinite)

* **Studier by Mehnoona, 1999**
    * Give the convex hull of R1 ∪ R2
    * Under the assumptions:
        1. y = binary
        2. R is bounded
        3. Disjunctions used like
            - y_i = 0 or y_i = 1

### Convex Hull is given by

- $(x^1, y^1) \in R_1$
- $(x^2, y^2) \in R_2$
- $(x, y) = \lambda^1(x^1, y^1) + \lambda^2(x^2, y^2)$
- With $\lambda^1 + \lambda^2 = 1$
- $\lambda^1 \geq 0$, $\lambda^2 \geq 0$

**M(x²)**

$m = \sum (\begin{array}{cc} x^1_1 & y^1_1 \\ x^2_1 & y^2_1 \\ \lambda^1_1 & \lambda^2_1 \end{array})$

Assuming,
- y_i = 0 or y_i = 1

[Diagram: Convex Hull]

Form new constraints in place of difficult set:

$x = x_1 + x_2$

$y = y_1 + y_2$

Use some trick

$\begin{aligned}
& x = x_1 + x_2 \\
& y = y_1 + y_2 \\
& x = \lambda^1 x^1 + \lambda^2 x^2 \quad \rightarrow \text{NCX} \\
& y = \lambda^1 y^1 + \lambda^2 y^2 \quad \rightarrow \text{NCX} \\
& \lambda^1 + \lambda^2 = 1 \quad \rightarrow \text{CX} \\
& \lambda^1, \lambda^2 \geq 0 \quad \rightarrow \text{CX} \\
& y_1 = 0 \quad \rightarrow \text{CX} \\
& y_2 = 1 \quad \rightarrow \text{CX}
\end{aligned}$

```
