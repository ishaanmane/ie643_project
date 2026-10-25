```markdown
# Integer Programming

## Linear Relaxation

### Original Problem
\[
\min \quad x^T Q x + c^T x
\]
Subject to:
\[ 0 \leq x_i \leq 1 \]

### Introduction of Mixed Variables
Introduce mixed variables \( y_i \) where:
- \( x_i = X_1 x_i + X_2 y_i \)
- \( y_i = x_i^2 \)

Subject to:
\[ 0 \leq x_i \leq 1 \]

### Boolean Case
In case of only boolean variables (\( x \in \{0,1\} \)):
\[
\min \quad \sum Q_{ij} x_i + \sum c_i x_i
\]
Subject to:
\[ x_i = x_j x_k \]
where \( x_i \in \{0,1\} \).

### Convex Hull
The convex hull of the feasible region is the same as the convex hull of the set defined by:
\[ x_i = x_j x_k \]
with constraints:
\[ 0 \leq x_i \leq 1 \]

### Result by Burer and Letchford
Result by Burer and Letchford.
```