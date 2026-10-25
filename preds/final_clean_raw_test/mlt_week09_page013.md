$$= \sum_{i=1}^{n}\left[-x_i + y_ix_i + x_i\frac{e}{1+e^{-w^Tx_i}}\right]$$

$$= \sum_{i=1}^{n}\left[y_ix_i - x_i\left(\frac{1}{1+e^{-w^Tx_i}}\right)\right]$$

$$\nabla\log L(w) = \sum_{i=1}^{n}\left[x_i(y_i-\frac{1}{1+e^{-w^Tx_i}})\right]$$

**Gradient update rule**

$$w_{t+1} = w_t + \eta_t\nabla\log L(w)$$
$$= w_t + \eta_t\left(\sum_{i=1}^{n}[x_i, y_i \in \mathbb{R}^d], \; \theta_i \in [0,1], \; g(w_t^Tx_i)\right)$$

[Diagram: A chain of nodes — input $x_i$, target $y_i$, sigmoid neuron output $\frac{1}{1+e^{-w_t^Tx_i}}$, and its derivative $g'(w_t^Tx_i)$ — illustrating the gradient flow.]

$$\min_w \underbrace{\sum_{i=1}^{n}\left[\log(1-e^{w^Tx_i}) + y_i(1-y_i)\right]}_{\text{REGULARIZED VERSION}} \rightarrow \underbrace{+\lambda\|w\|^2}_{\text{Regularizer}}$$