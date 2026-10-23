$$\nabla_{W^l} e = \text{Diag}(\phi'^l) \cdot [\delta^l] (\vec{a}^{l-1})^T$$

$$(W^l)^{k+1} = (W^l)^k + \eta_k \left(-\nabla_{W^l} e\right)$$

**Automatic Differentiation / Griewank**

**Input:**
1. NN $\rightarrow$ num layers, num of neurons in each layer, activation fns.
2. loss fn.
3. $D = \{(x^i, y^i)\}_{i=1}^{N}$

Setup: opt scheme, hyperparams ...
