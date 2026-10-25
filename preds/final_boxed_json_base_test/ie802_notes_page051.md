```markdown
# Handwritten Lecture Note Page

## Algorithm 1

1. Pick a random point \((x,y)\) with \(x \in \mathbb{R}^n\) and \(y \in \mathbb{Z}^p\)
2. Check if it is best
3. Go to 1 (until value not improved) → Stopping criteria is important works but Not so good… → We have good idea after many trials

### Neighbourhood Search

[Diagram: Neighborhood Search]

## Algorithm 2

1. Solve continuous relaxation
2. Round \(y\) to nearest integer

Good if convex problem relaxation is there.

Also couple with Neighbourhood Search

Try different rounding:

\[ y = \begin{bmatrix}
0.6 \\
0.4 \\
0.2 \\
0.5
\end{bmatrix} \]

## Algorithm 1

Most soln on \(x\) … if 0 or 1 not bad…

[Diagram: Diagram]
```