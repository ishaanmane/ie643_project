Gradient descent to solve

$$\min_{x \in \mathbb{R}^d} f(x) \qquad f: \mathbb{R}^d \to \mathbb{R}$$

$\rightarrow$ Start at $x^0 \in \mathbb{R}^d$

$\rightarrow$ for $k=0,1,2,\dots$
  - find a descent direction $u^k$
  - find step length $\alpha_k$
  - $x^{k+1} \leftarrow x^k + \alpha_k u^k$

**local minimum**
**Saddle points**

[Diagram: A box "ve gradient" with an arrow pointing to a question mark (?) branching off into two paths labeled "1. local minimum" and "2. Saddle points".]