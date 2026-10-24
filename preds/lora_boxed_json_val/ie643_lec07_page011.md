$$\min_{w} E = \sum_{i=1}^{N} e(y^i, \hat{y}^i) \quad \nabla E = \sum_{i=1}^{N} \nabla e(y^i, \hat{y}^i) \rightarrow \text{sample-based gradient}$$

full gradient

for $k=0,1,2,\dots$

- find descent dirn wrt $\nabla E(w^k)$
- find a suitable step length $\alpha_k$
- $w^{k+1} \leftarrow w^k + \alpha_k(-\nabla E(w^k))$

zero-gradient check to stop this process