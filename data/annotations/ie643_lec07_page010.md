**Gradient descent to solve**

$$\min_{x \in \mathbb{R}^d} f(x), \qquad f: \mathbb{R}^d \to \mathbb{R}$$

1. local minimum
2. saddle points ??

$\rightarrow$ Start at $x^0 \in \mathbb{R}^d$
$\rightarrow$ for $k = 0, 1, 2, \dots$
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ find a descent direction $u^k$ (−ve gradient)
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ find step length $\alpha_k$
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ $x^{k+1} \leftarrow x^k + \alpha_k u^k$
