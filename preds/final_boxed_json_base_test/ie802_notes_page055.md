```markdown
# Local Branching (Improvement)

## Known Solution

Let $(\hat{x}, \hat{y})$ be a known solution.

$\hat{y} \in \mathbb{Z}_{\geq 0}$

### Diagram: Tree Structure

- $\sum_{i=1}^{k} x_i - \hat{x}_i \leq 5$
- Cardinality constraint
- Not useful

### Local Jump: Idiot Crash

- Solving LP takes too long
- Initial construction:

#### Equations

$\begin{aligned}
& 2y_1 + y_2 - y_3 \leq 2 \\
& -y_1 + 2y_2 + y_3 \geq 9 \\
& y_2 + y_0 + y_4 = 5 \\
& y_3 - y_4 + y_6 \leq 8 \\
& 0 \leq y \leq 10
\end{aligned}$

#### Minimize Objective Function

$\min \sum w_i (b_i - ay)^+$

Set $y = 0$
```