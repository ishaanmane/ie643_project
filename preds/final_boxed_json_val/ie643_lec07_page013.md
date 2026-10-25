## Mini-batch SGD

$$D = \{(x^i,y^i)\}_{i=1}^{N}, \quad \rightarrow W^D$$

for $k=0,1,2,\dots$

$\hookrightarrow$ Sample mini-batch of samples: $B_k \subseteq \{1,2,\dots,N\}$

for every $j \in B_k$: compute $\nabla e(y^j,\hat{y}^j)$

$$W^{k+1} \leftarrow W^k + \eta_k \left(-\sum_{j \in B_k} \nabla e(y^j,\hat{y}^j)\right)$$

convergence in asymptotic sense