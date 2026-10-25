$$\min_{w} E = \sum_{i=1}^{N} e(y^i, \hat{y}^i) \qquad \nabla E = \sum_{i=1}^{N} \nabla e(y^i, \hat{y}^i) \rightarrow \text{full gradient}, \; \nabla E = \sum_{i=1}^{N'} \nabla e(y^i, \hat{y}^i) \rightarrow \text{sample-based gradient}$$

for $k=0,1,2,\dots$
- find descent dirn using $-\nabla E(w^k)$
- find a suitable step length $\alpha_k$
- $w^{k+1} \leftarrow w^k + \alpha_k(-\nabla E(w^k))$

$\rightarrow$ zero-gradient check to stop this process ($\nabla E(w^{k+1}) \approx 0$)

$$10^{-5}, 10^{-4}, \dots$$

$\epsilon_k$: fixed to be small value close to $0$, typically $10^{-8}$.

$\rightarrow$ step-length finding procedures