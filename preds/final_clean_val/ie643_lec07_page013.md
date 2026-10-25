## Mini-batch SGD

$$D = \{(x^i, y^i)\}_{i=1}^{N}$$

$\rightarrow w^0$

$\rightarrow$ for $k=0, 1, 2, \dots$

$\hookrightarrow$ Sample mini-batch of samples:
$$B_k \subseteq \{1, 2, \dots, N\}$$

for every $j \in B_k$: compute $\nabla e(y^j, \hat{y}^j)$

$\hookrightarrow$ $w^{k+1} \leftarrow w^k + \eta_k \left(-\sum_{j \in B_k} \nabla e(y^j, \hat{y}^j)\right)$

$\hookrightarrow$ convergence in asymptotic sense