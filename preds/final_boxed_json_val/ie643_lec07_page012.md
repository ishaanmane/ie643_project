## Stochastic gradient descent

$$D = \{(x^i,y^i)\}_{i=1}^{N}$$

$\rightarrow w^0$

$\rightarrow$ for $k=0,1,2,\dots$

Compute a **stochastic gradient** — randomly choose $j\in\{1,2,3,\dots N\}$, compute $\nabla e(y^j,\hat{y}^j)$.

$$w^{k+1} \leftarrow w^k - \eta\nabla e(y^j,\hat{y}^j)$$

Stochastic approx. of $\nabla f$
- Convergence to the local opt/saddle pt
- Might not lead to descent

parameter regime: $10^6$, $10^8$, $\vdots$