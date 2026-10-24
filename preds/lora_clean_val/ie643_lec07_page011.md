$$\min_{w} E = \sum_{i=1}^{N} e(y^i, \hat{y}^i) \qquad \nabla E = \sum_{i=1}^{N} \nabla e(y^i, \hat{y}^i) \rightarrow \text{sample-based gradient}$$

full gradient → very large → overfit

- $w^0$
- for $k=0,1,2,\dots$
  - find descent dirn using $-\nabla E(w^k)$ ($10^{-8}$)
  - find a suitable step length $\alpha_k$
  - $w^{k+1} \leftarrow w^k + \alpha_k(-\nabla E(w^k))$
  - zero-gradient check to stop this process

$\epsilon_k$: fixed to be small value close to $0$; $10^{-5}, 10^{-4}, \dots$

$\alpha_k$: step-length finding procedures