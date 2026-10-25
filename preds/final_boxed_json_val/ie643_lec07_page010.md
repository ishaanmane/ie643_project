## Gradient descent to solve

$$\min_{x \in \mathbb{R}^n} f(x) \qquad f: \mathbb{R}^n \to \mathbb{R}$$

$\rightarrow$ Start at $x^0 \in \mathbb{R}^d$

$\rightarrow$ for $k=0,1,2,\dots$

- find a descent direction
- find step length $\alpha_k$
- $x^{k+1} \leftarrow x^k + \alpha_k u^k$

**Local minimum**, **Saddle points**

$\hookrightarrow$ **-ve gradient** $\Rightarrow$ ?

$u^k$, $x^{k+1}$