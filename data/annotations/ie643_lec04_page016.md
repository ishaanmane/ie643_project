[Diagram: A small multi-layer perceptron — inputs $x_1, x_2$ connect via weights $a,b,c,d$ to two hidden-layer neurons, which connect via weights $e,f$ to one output neuron producing $\hat{y}$, labeled "XOR o/ps".]

$$\text{relu}(z) = \max(0, z)$$

**Perceptron's decision rule:**
$$\hat{y} = \text{sign}(\langle w, x \rangle - \theta) \quad \text{(activation fn.)}$$
