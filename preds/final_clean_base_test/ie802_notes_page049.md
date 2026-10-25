```markdown
# Integer Programming

## Introduction

The problem involves minimizing the objective function subject to certain constraints.

### Original Problem

\[
\begin{aligned}
& \min & x^T Q x + c^T x \\
& \text{s.t.} & 0 \leq x_i \leq 1
\end{aligned}
\]

This is an integer programming problem because the variables \(x_i\) must be integers.

### Relaxation

To solve this problem, we introduce new variables:

- \(y_{ij}\) where \(y_{ij} = x_i x_j\)
- \(z_i\) where \(z_i = x_i^2\)

Thus, the problem becomes:

\[
\begin{aligned}
& \min & \sum Q_{ij} y_{ij} + \sum Q_{ii} z_i + \sum c_i x_i \\
& \text{s.t.} & \\
& & x_{ij} = x_i x_j \quad \forall i,j \\
& & z_i = x_i^2 \quad \forall i \\
& & 0 \leq x_i \leq 1
\end{aligned}
\]

### Boolean Case

In the case of only boolean variables (\(x \in \{0,1\}\)), the problem can be simplified using Padberg's triangle inequalities.

\[
\begin{aligned}
& \min & \sum Q_{ij} x_{ij} + \sum c_i x_i \\
& \text{s.t.} & \\
& & x_{ij} = x_i x_j \\
& & x_i \in \{0,1\} \quad \forall i \\
& & \text{Convex hull of } \{x_{ij} = x_i x_j \mid 0 \leq x_i \leq 1\} \\
& & \text{is same as convex hull of } x_{ij} = x_i x_j \\
& & 0 \leq x_i \leq 1
\end{aligned}
\]

### Result by Bowen and Letchford

The result by Bowen and Letchford states that the convex hull of the set defined by \(x_{ij} = x_i x_j\) with \(0 \leq x_i \leq 1\) is equivalent to the convex hull of the set defined by the same conditions.
```