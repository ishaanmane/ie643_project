$i=1,\dots,D$, $(x_1,y_1),\dots,(x_n,y_n)$, $w_i \in \mathbb{R}$

Iteration: $w^0 = 0 \in \mathbb{R}^d$

$$Y_i \in \{+1,-1\}, \qquad [0 \; 0 \; 0 \; \dots \; 0]$$

until convergence,
- Pick $(x_i, y_i)$ pair from the dataset
- If $\text{sign}(w^T x_i) = \text{sign}(y_i)$, do nothing
else, $w^{t+1} = w^t + x_i y_i$ &nbsp;&nbsp;&nbsp;← update rule