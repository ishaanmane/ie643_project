## Recap:

[Diagram: A chain of boxes labeled $N_1, N_2, \dots, N_{L-1}, N_L$, with an input layer box on the left containing $x \in \mathbb{R}^d$.]

$$\hat{y} = a^L = \phi(W^L \cdots \phi(W^3 \phi(W^2 \phi(W^1 x))))$$

Input layer → $N_1$ → $N_2$ → $\cdots$ → $N_{L-1}$ → $N_L$ (output layer)

$$e(y, \hat{y}) \rightarrow \text{loss fn to compare true and predicted labels}$$