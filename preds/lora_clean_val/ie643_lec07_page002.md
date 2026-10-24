## Recap:

[Diagram: A chain of $N_1 \to N_2 \to \cdots \to N_{L-1} \to N_L$ nodes (layers) — input layer ($x \in \mathbb{R}^d$) feeding into $N_1$, then each layer feeding into the next until output layer.]

$$\hat{y} = a^L = \phi(W^L; \phi(W^{L-1}\phi(W^2\phi(W^1 x))))$$

$$e(y,\hat{y}) \rightarrow \text{loss fn to compare true and predicted labels}$$

output layer.