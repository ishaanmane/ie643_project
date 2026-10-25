$r=1,\dots,n$, $n\in\mathbb{N}$, $\;x_i\in\mathbb{R}^d$
$$Y_i\in\{+1,-1\}$$

Iteration:
$$w^0 = 0 \in \mathbb{R}^d \qquad [0\;0\;0\;\dots\;0]$$

until convergence,
- Pick $(X_i,Y_i)$ pair from the dataset
- If $\text{sign}(w^Tx_i) = \text{sign}(y_i)$, do nothing
else,
$$w^{t+1} = w^t + x_iy_i \leftarrow \text{update rule}$$