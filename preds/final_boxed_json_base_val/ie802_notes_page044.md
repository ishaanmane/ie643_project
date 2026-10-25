```markdown
# Handwritten Lecture Note Page

## Step 4
\[
\alpha x + \beta y \leq \beta
\]
And \(\frac{\alpha}{\beta} = \frac{\beta}{\gamma}\) valid for both \(R_1\) and \(R_2\)

### Use \(R_1, R_2...\) together to get Red line
There are lots of lines like the Red line (infinite)

---

* **Stubbs & Mehrotra, 1999**
    - Give the convex hull of \(R_1 \cup R_2\) under the assumptions:
        1. \(y = 0\) along
        2. \(R_i\) are bounded
        3. Disjunctions used like \(y_i = 0\) or \(y_i = 1\)

- Convex Hull is given by
    \[
    (x^1, y^1) \in R_1 \\
    (x^2, y^2) \in R_2
    \]
    \[
    (x, y) = \lambda^1(x^1, y^1) + \lambda^2(x^2, y^2)
    \]
    with \(\lambda^1 + \lambda^2 = 1\)
    \(\lambda^1 \geq 0, \lambda^2 \geq 0\)

[Diagram: Convex Hull]

---

\(M(x^1)\)

\[
m = \int \begin{pmatrix}
x^1_1 & y^1_1 & x^1_2 & y^1_2 & \lambda^1_1 & \lambda^2_1 \\
x^2_1 & y^2_1 & x^2_2 & y^2_2 & \lambda^1_2 & \lambda^2_2
\end{pmatrix}
\]

Assuming:
\[
y_1 = 0 \quad \text{or} \quad y_1 = 1
\]

\[
x = \lambda^1 x^1 + \lambda^2 x^2 \quad \leadsto \text{NCX}
\]
\[
y = \lambda^1 y^1 + \lambda^2 y^2 \quad \leadsto \text{NCX}
\]
\[
\lambda^1 + \lambda^2 = 1 \quad \leadsto \text{CX}
\]
\[
x^1_1, x^2_1 \geq 0 \quad \leadsto \text{CX}
\]
\[
y^1_1 = 0 \quad \leadsto \text{CX}
\]
\[
y^2_2 = 1 \quad \leadsto \text{CX}
\]

Form new constraints in place of difficult ones:

\[
x = \overline{x_1} + \overline{x_2}
\]
\[
y = \overline{y_1} + \overline{y_2}
\]

Use some trick
```