```markdown
# Continuous Non-Convex Quadratic Models

## Objective Function
\[
\text{minimize } \frac{1}{2} x^T Q x + c^T x
\]

## Constraints
\[
\begin{aligned}
&\text{subject to} \\
&\quad \frac{1}{2} \sum_{i} x_i^T Q_i x_i + a_i^T x \leq b_i \\
&\quad l \leq x \leq u
\end{aligned}
\]

### 0 Multistart NLP Heuristic
- Give it to a local gradient-based solver.

[Diagram: Multi-start heuristic diagram]

### 0 Undercover Heuristic
- You pick some \(x\) values.
- Suppose p=100.
- Pick 90 and fix for some values.

\[
x_1^2 + 5x_1x_2 + 7x_3x_4 + x_1x_3 - 2x_1x_4 \leq 1
\]

- \(x_1 = 2\)
- \(x_3 = 1\)

[Diagram: Graph with nodes labeled \(x_1\), \(x_2\), \(x_3\), and \(x_4\)]

- How to know which variable to pick and what values...
- Trial and error.

[Diagram: Graph with edges covered by nodes \(x_1\) and \(x_3\)]
```