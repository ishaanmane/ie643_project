```markdown
# Optimization Algorithms

## Algorithm 1

1. **Pick a random point** $(x,y)$ within $x \in \mathbb{R}^n$ and $y \in \mathbb{Z}^p$
2. **Check if it is best**
3. **Go to 1 (until value not improved)** → Stopping criteria is important works but not so good... → We have good idea after many trials

Neighbourhood search:

## Algorithm 2

1. Solve continuous relaxation
2. Round $y$ to nearest integer
   - Good if convex problem relaxation is there
Also couple with Neighbourhood search

Try different rounding.

We get:

$$
\begin{bmatrix}
0.6 \\
0.4 \\
0.2 \\
0.5
\end{bmatrix}
$$

## Algorithm 1

$\min f(x,y)$

Subject to:
- $0 \leq x \leq 1$
- $y \in \{0,1\}^p$

$$
\sum_{i=1}^{p} y_i = k
$$

Most solutions on $x$ → If 0 or 1 not blue...
```