$$\min_{w} E = \sum_{i=1}^{N} e(y^i, \hat{y}^i)$$

$\nabla E = \sum_{i=1}^{N} \nabla e(y^i, \hat{y}^i)$ — full gradient → sample-based gradient

```
for k=0,1,2,...:
    find descent dir using $\nabla E(w^k)$
    find a suitable step length $\alpha_k$
    $w^{k+1} \leftarrow w^k + \alpha_k(-\nabla E(w^k))$
```

> zero-gradient check to stop this process

$10^{-8}$, $10^{-5}$, $10^{-4}$, $10^{-3}$, $10^{-2}$, $10^{-1}$, $10^0$, $10^1$, $10^2$, $10^3$, $10^4$, $10^5$

$k$: fixed to be small value close to $10^{-4}$ — step-length finding procedures