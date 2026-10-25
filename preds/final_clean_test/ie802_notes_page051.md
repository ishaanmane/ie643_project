$$\min f(x,y) \quad x \in \mathbb{R}^n, \; y \in \mathbb{Z}^p$$

(1) **Algo-1**
1. Pick a random point $(x,y)$ with $x \in \mathbb{R}^n$ and $y \in \mathbb{Z}^p$
2. Check if it is best
3. Go to 1 (until... value not improves) $\rightarrow$ stopping criteria is important works but Not so good... $\rightarrow$ we have good idea after many trials

Neighbourhood search:

(2) **Algo-2**
1. Solve continuous relaxation
2. Round $y$ to nearest integer $\hookrightarrow$ Good if convex problem relaxation is there

Also couple with Neighbourhood search

1. Try different rounding.

we get: $y = \begin{bmatrix}0.6 \\ 0.4 \\ 0.2 \\ 0.5\end{bmatrix}$

$$\min f(x,y) \qquad \sum_{i=1}^{p} y_i = k, \quad y_i \in \{0,1\}, \; i=1\dots p$$

(1) Algo-1 $\rightarrow$ same mostly most soln on $x$.. if 0 or 1 not blu...