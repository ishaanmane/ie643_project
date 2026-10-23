## Recap: Multilayered perceptrons

## Training Algo:

Input: $D = \{(x^i, y^i)\}_{i=1}^{N}$, $x^i \in \mathbb{R}^d$, $y^i \in \{+1,-1\}$ or $\{0,1\}$ or $\{1,\dots C\}$

**NN architecture of MLP.**

[Diagram: input layer ($x^i$, dim) → several hidden layers (columns of nodes) → output layer.]

$\rightarrow$ Setup: loss fn (task defined)
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ optimizer: minibatch sgd, adam, ... — learning rate schedule, minibatch size
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ (num of hidden layers, num of neurons in each hidden layer, i/p layer design, o/p layer design, activation fns for each layer)
