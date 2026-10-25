## Recap:

[Diagram: A chain of $N_1 \to N_2 \to \cdots \to N_{L-1} \to N_L$ boxes, labeled "Input layer" (input vector $x \in \mathbb{R}^{n_d}$) on the left, "Output layer" on the right.]

$$\hat{y} = a^L = \phi(W^L; \phi(W^3 \phi(W^2 \phi(W^1 x))))$$

$$e(y,\hat{y}) \rightarrow \text{loss fn to compare true and predicted labels}$$