## Stochastic gradient descent

**parameter regime:** $10^6$, $10^8$, ...

$$D = \{(x^i,y^i)\}_{i=1}^{N}$$

$\rightarrow w^0$

$\rightarrow$ for $k=0,1,2,\dots$

$\hookrightarrow$ Compute a **stochastic gradient**

- Randomly choose $j\in\{1,2,3,\dots N\}$
- Compute $\nabla e(y^j,\hat{y}^j)$

$$w^{k+1} \leftarrow w^k + n_k(-\nabla e(y^j,\hat{y}^j))$$

Stochastic approx. $\Rightarrow$ convergence to the local opt/saddle pt.

might not lead to descent