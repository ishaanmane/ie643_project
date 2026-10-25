$$\min_{x \in \mathbb{R}^n, y \in \mathbb{Z}^p} f(x,y)$$

**(1) Algo-1**
1. Pick a random point $(x,y)$ with $x \in \mathbb{R}^n$ and $y \in \mathbb{Z}^p$
2. Check if it is best
3. Go to 1 (until.. value not improves) $\rightarrow$ stopping criteria is important works but Not so good... $\rightarrow$ we have good idea @ after many trials

Neighbourhood search.

**(2) Algo-2**
1. Solve continuous relaxation
2. Round $y$ to nearest integer

$\hookrightarrow$ Good if convex problem relaxation is there.

Also couple with Neighbourhood search

Try different rounding:

$$y = \begin{bmatrix}0.6 \\ 0.4 \\ 0.2 \\ 0.5\end{bmatrix} \Rightarrow \text{we get} \dots$$

$$\min_{x \in [0,1]^n, y \in \{0,1\}^p} f(x,y)$$
$$\sum_{i=1}^{p} y_i = k$$

**(1) Algo-1 $\rightarrow$ same mostly** most soln on $x$ .. if 0 or 1 not blw ...