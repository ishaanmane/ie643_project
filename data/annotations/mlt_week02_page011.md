## Kernel PCA

Input: $\{x_1,\dots,x_n\}$, $x_i \in \mathbb{R}^d$, where kernel $k: \mathbb{R}^d\times\mathbb{R}^d \rightarrow \mathbb{R}$

- Step 1: Compute $K \in \mathbb{R}^{n\times n}$ where $K_{ij} \in k(i,j) \; \forall i,j$ — "center the kernel"

- Step 2: Compute $\{\beta_1,\dots,\beta_\ell\}$ eigenvectors & $\{n\lambda_1,\dots,n\lambda_\ell\}$ eigenvalues of $K$, & normalize to get:
$$\alpha_u = \frac{\beta_u}{\sqrt{n\lambda_u}} \; \forall u$$

- Step 3: $w_k = \phi(x)\alpha_k$ $\rightarrow$ This defeats the purpose as we did all that just to avoid the computation of $\phi(x)$

  - We cannot "reconstruct" the eigenvectors of the covariance matrix.
  - But we can compute the "compressed" representation.

- Step 3 (modified): Compute $\sum_{j=1}^{n}\alpha_{kj}K_{ij} \; \forall k$
