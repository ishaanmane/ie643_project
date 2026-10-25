$$\min_W E = \sum_{i=1}^{N} e(y^i, \hat{y}^i) \qquad \nabla E = \sum_{i=1}^{N} \nabla e(y^i, \hat{y}^i)$$

$N$: very large $\rightarrow$ over... (overload)

full gradient vs. sample-based gradient

- $w^0$
- for $k = 0, 1, 2, \dots$
  - find descent dirn using $-\nabla E(w^k)$
  - find a suitable step length $\alpha_k \rightarrow$ step-length finding procedures ($10^{-5}, 10^{-4}, \dots$; $\alpha_k$ fixed to be small value close to $\dots$; $10^{-8}$)
  - $w^{k+1} \leftarrow w^k + \alpha_k(-\nabla E(w^k))$
  - zero-gradient check to stop this process
