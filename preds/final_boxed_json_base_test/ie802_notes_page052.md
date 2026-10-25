```markdown
# Continuous Non-convex Quadratic Models

$$
\begin{aligned}
& \min \frac{1}{2} x^T Q x + c^T x \\
& \text { st } \quad \frac{1}{2} Q_i x^T Q_i x + q_i^T x \leq b_i \\
& 1 \leqslant x \leqslant U
\end{aligned}
$$

## Multistart NLP Heuristic

- Give it to a local gradient based solver

[Diagram: Graph showing multiple local minima]

Also give them another point, if not good then take another point.

## Under cover heuristic

- You pick some \( x \) values
- Suppose \( p = 100 \)
- Pick \( p_0 \) and fix for some values
- \( x_1^2 + 5 x_1 x_2 + 7 x_3 x_4 + x_1 x_3 - 2 x_1 x_4 \leq 1 \)

### ISA Iteration
- \( x_1 = 2 \)
- Next change values and solve NLP
- Take \( x_1 \) as any thing (change variable)
- How to know which variable to pick and what value?
- Trial and error

[Diagram: Graph with nodes \( x_1, x_2, x_3, x_4 \)]

Pick smallest node so that every set is covered...
- Find smallest node (edge) cover for this graph so that every edge is covered...

\( (x_1, x_3) \)
\( (x_1, x_4) \)

Solve...
```