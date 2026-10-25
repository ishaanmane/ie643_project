```markdown
# Local Branching (Improvement)

Let $(\hat{x}, \hat{y})$ be a known solution.

$$
y \in Z_{01}^{n}
$$

[Diagram: Tree diagram showing branching process]

## Local Jump

- **Idiot Crash:** Solving LPs takes too long.
- **Initial Construction:**

$$
\begin{aligned}
& 2x_1 + x_2 - x_3 \leq 2 \\
& -x_1 + 2x_2 + x_3 \geq 9 \\
& x_2 + x_3 + x_4 = 5 \\
& x_3 - x_4 + x_6 \leq 8 \\
& 0 \leq y \leq 10
\end{aligned}
$$

$$
\min \sum w_i (b_i - a_i)^+
$$

- **Local Jump:** 
  - $y_1$ should be small.
  - $y_2$ should be small.
  - Set $y = 0$
```
