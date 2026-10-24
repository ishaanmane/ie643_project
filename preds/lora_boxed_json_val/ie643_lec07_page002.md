## Recap:

$$x \in \mathbb{R}^{n \times d}$$

[Diagram: A chain of $N_1, N_2, \dots, N_{L-1}, N_L$ neurons (layers) — input layer $\rightarrow N_1 \rightarrow N_2 \rightarrow \cdots \rightarrow N_{L-1} \rightarrow N_L$ — output layer.]

$$\hat{y} = \vec{a}^L = \phi(W^L; \phi(W^3 \phi(W^2 \phi(W^1 x))))$$

$$e(y, \hat{y}) \rightarrow \text{loss fn to compare true and predicted labels}$$