## Stochastic gradient descent

$$D = \{(x^i,y^i)\}_{i=1}^{N}$$

$\rightarrow w^0$

$\rightarrow$ for $k=0,1/2,\dots$

Compute a **stochastic gradient** — randomly choose $j\in\{1,2,3\dots N\}$, compute $\nabla e(y^j,x^j)$.

$$w^{k+1} \leftarrow w^k + \eta_k(-\nabla e(y^j,x^j))$$

Stochastic approx. 51 → convergence to the local opt/saddle pt

might not lead to descent