[Diagram: A simple chain — node $\xrightarrow{b}$ node $\xrightarrow{a}$ node, with $n=1$, $p=1$, $n=1$ (single-neuron encoder-decoder example).]

$$D = \{(x^s, y^s)\}, \quad y^s = x^s$$

$$(x^s, y^s), \quad x^s \in \mathbb{R}, \; y^s \in \mathbb{R}$$

$$E(a,b) = \sum_{s=1}^{S} (abx^s - y^s)^2$$

$$D = \{(x^s, x^s)\} \quad \text{Auto-encoder}$$
$$\sum (abx^s - x^s)^2$$
