Input: $\{(x_1,y_1),\dots,(x_n,y_n)\}$, $x_i\in\mathbb{R}^d$, $y_i\in\{+1,-1\}$

$$w^0 = 0 \in \mathbb{R}^d \; [0\;0\;0\;\dots\;0] \quad \text{iteration}$$

until convergence,
- Pick $(x_i,y_i)$ pair from the dataset
- If $\text{sign}(w^{t^T}x_i) = \text{sign}(y_i)$, **do nothing**

else,
$$\boxed{w^{t+1} = w^t + x_iy_i} \leftarrow \text{update rule}$$
