## Parameterized Regime ($10^6$, $10^8$, $\dots$)

**Stochastic gradient descent**

$$D = \{(x^i,y^i)\}_{i=1}^{N}$$

$\rightarrow w^0$

$\rightarrow$ for $k=0,1,2,\dots$

$\hookrightarrow$ Compute a **stochastic gradient**: randomly choose $j\in\{1,2,3,\dots N\}$; compute $\nabla e(y^j,\hat{y}^j)$

$$w^{k+1} \leftarrow w^k + \eta \frac{-\nabla e(y^j,\hat{y}^j)}{J}$$

**Stochastic approx. 51** — Convergence to the local opt/saddle pt.

might not lead to descent