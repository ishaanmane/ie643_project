$$A = \begin{bmatrix} \uparrow & \uparrow & & \uparrow \\ A_1 & A_2 & \cdots & A_p \\ \downarrow & \downarrow & & \downarrow \end{bmatrix} \qquad h = \begin{bmatrix} h_1 \\ h_2 \\ \vdots \\ h_p \end{bmatrix}$$

[Diagram: chain $D \to B \to A \to D$, an encoder-decoder bottleneck symbol.]

$$Ah = h_1A_1 + h_2A_2 + \cdots + h_pA_p \rightarrow b\text{'s}$$

$$\min_{A,B} \|\text{vec}(ABX) - \text{vec}(Y)\|$$

$$W = AB$$
$$E(A,B) = \text{Tr}(\Sigma_{yy}) - \sum_{i \in \mathcal{I}} \lambda_i$$
