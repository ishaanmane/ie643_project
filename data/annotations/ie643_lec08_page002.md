## Recap.

Obj. of training a MLP:
$$\min_{w^1, w^2, \dots, w^L} E = \sum_{i=1}^{N} e(y^i, \hat{y}^i; x^i)$$

## Gradient descent:

$\rightarrow w^0 = [(w^1)^0, (w^2)^0, \dots, (w^L)^0]$
$\rightarrow$ for $k=0,1,2,\dots$
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ find a descent dirn $u^k \neq \vec{0}$ ($-\nabla_w E$)
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ find a step length $\alpha_k$
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ make a move: $w^{k+1} = w^k + \alpha_k u^k$

**Descent direction of a function** $f: \mathbb{R}^d \to \mathbb{R}$ **at a point** $x$:

$u \neq \vec{0}$ is called a descent dirn of $f$ at $x$ if: $\exists \epsilon > 0$ s.t. $\forall \alpha \in (0, \epsilon]$,

$$f(x + \alpha u) < f(x)$$
