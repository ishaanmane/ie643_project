## Recap:

$$x \in \mathbb{R}^{n\times d}$$

[Diagram: A chain of layers — input layer ($\begin{bmatrix}0\\0\\\vdots\\0\end{bmatrix}$) → $N_1$, $N_2$, $\dots$, $N_{L-1}$, $N_L$ (output layer).]

$$\hat{y} = \vec{a}^L = \phi(W^L)\phi(W^{L-1}\phi(W^2\phi(W^1x)))$$

$$e(y,\hat{y}) \rightarrow \text{loss fn to compare true and predicted labels}$$