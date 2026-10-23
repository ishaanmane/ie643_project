$$x_i \rightarrow \left[\sum_{j=1}^{n}\alpha_{1j}K_{ij} \;\; \sum_{j=1}^{n}\alpha_{2j}K_{ij} \;\; \cdots \;\; \sum_{j=1}^{n}\alpha_{\ell j}K_{ij}\right], \quad x_i \in \mathbb{R}^d$$

## Centering the Kernel

given $K \in \mathbb{R}^{n\times n}$, $K_{ij} = k(x_i,x_j) \; \forall i,j$

create a new kernel $K^c \Leftarrow$ centered

$$K_{ij}^c = K_{ij} - \theta_i\mathbb{1}^T - \mathbb{1}_i\theta_j^T + \zeta\mathbb{1}_i\mathbb{1}_j$$

where $\theta = \frac{1}{n}\sum_{k=1}^{n}K_{ik}$, $\zeta = \frac{1}{n^2}\sum_{i,j}K_{ij}$
