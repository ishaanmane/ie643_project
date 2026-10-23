## Stochastic gradient descent.

$$D = \{(x^i, y^i)\}_{i=1}^{N}$$

$\rightarrow w^0$
$\rightarrow$ for $k = 0, 1, 2, \dots$
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ Compute a stochastic gradient
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;randomly choose $j \in \{1,2,3,\dots N\}$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute $\nabla e(y^j, \hat{y}^j)$

$$w^{k+1} \leftarrow w^k + \eta_k(-\nabla e(y^j, \hat{y}^j))$$

**Stochastic approx.**$^{'51}$ $\rightarrow$ convergence to the local opt/saddle pt $\rightarrow$ might not lead to descent
