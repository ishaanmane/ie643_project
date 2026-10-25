```markdown
# Convex MINLO Case (Pure Binary)

\begin{equation}
\min c^T x + d^T y
\end{equation}

Subject to:
\begin{equation}
g_i(x,y) \leq 0
\end{equation}
where \(x \in \mathbb{R}^n\) and \(y \in \{0,1\}^p\).

- **Continuous**: Solve NLP relaxation.

    - Get \(\bar{x}, \bar{y}\) → round of \(\bar{x}, \bar{y}\)
    - You can also solve MILP relaxation.

- **Minimize**:
    \begin{equation}
    \sum_{i=1}^{p} |y_i - \text{round}(y_i)|
    \end{equation}
    Subject to:
    \begin{equation}
    g_i(x,y) \leq 0 \\
    0 \leq y \leq 1
    \end{equation}
    This is equivalent to:
    \begin{equation}
    \min \sum |y_i - \text{round}(y_i)|
    \end{equation}
    Subject to:
    \begin{equation}
    \nabla \text{inequalities at } (\bar{x}, \bar{y}) \\
    0 \leq y \leq 1
    \end{equation}

- **MILP**:
    \begin{equation}
    \vdots
    \end{equation}
    Subject to:
    \begin{equation}
    \theta \in \{0,1\}^p
    \end{equation}

## Non-convex MINLO Case (Pure Binary)

- Leave it...

# RINS Heuristic (Relaxed-Induced Neighborhood Search) → Improvement

Given a known solution \((\bar{x}, \bar{y})\) of MINLO:

1. Solve NLP relaxation of that node.
   - Get \((\bar{x}, \bar{y})\).
   - If majority of equalities are satisfied, randomly fix them.
2. Compare \(\bar{x}\) and \(\bar{y}\).
   - If all values are the same, fix them.
3. Solve the smallest MINLO.
   - Don't solve fully but with time limits, e.g., 5 seconds.
   - Use other parameters.

```
```