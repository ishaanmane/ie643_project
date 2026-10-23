## Recap.

$$D = \{(x^s,y^s)\}_{s=1}^{S}, \quad x^s, y^s \in \mathbb{R}^n$$

## Encoder-decoder architecture

[Diagram: $n$-neuron layer $\xrightarrow{B}$ $p$-neuron bottleneck layer ($p \leq n$) $\xrightarrow{A}$ $n$-neuron output layer, producing $\hat{y}$.]

All hidden layer + output layer neurons have **linear** activations.

For input $x$, the prediction is $\hat{y} = ABx$.
