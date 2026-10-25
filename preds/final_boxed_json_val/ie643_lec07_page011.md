$$\min_{w} E = \sum_{i=1}^{N} e(y^i, \hat{y}^i) \quad \nabla E = \sum_{i=1}^{N} \nabla e(y^i, \hat{y}^i) \rightarrow \text{very large} \rightarrow \text{over}$$

full gradient $\rightarrow$ sample-based gradient

for $k=0,1,2,\dots$

$\hookrightarrow$ find descent dirn using $-\nabla E(w^k)$

$\hookrightarrow$ find a suitable step length $\alpha_k$

$\hookrightarrow$ $w^{k+1} \leftarrow w^k + \alpha_k(-\nabla E(w^k))$

$\hookrightarrow$ zero-gradient check to stop this process ($\nabla E(w^{k+1}) \approx 0$)

$$10^{-8}, 10^{-5}, 10^{-2} \dots$$

$\epsilon_k$: fixed to be small value close to zero, small value chosen by user.

$\alpha_k$: step-length finding procedures