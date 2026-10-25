$$i = 1,\dots,n \quad \forall i \in \mathbb{N}$$

Iteration:
$$w^0 = 0 \in \mathbb{R}^d$$

until convergence,

- Pick $(x_i,y_i)$ pair from the dataset
- If $\text{sign}(w^T x_i) = \text{sign}(y_i)$, do nothing
else,
$$w^{t+1} = w^t + x_i y_i \leftarrow \text{update rule}$$