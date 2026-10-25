[Diagram: Two feedforward networks side-by-side — left is a single-layer perceptron (input layer $\to$ output layer via weight $w$), right is a multi-layer network with input layer $\to$ hidden layer $\to$ output layer, each neuron producing an output $\hat{y}_1,\hat{y}_2,\dots,\hat{y}_C$.]

$$\delta^l = (W^{l+1})^T \text{diag}(\phi^{l+1}) \cdot \epsilon^{l+1}$$

**fwd pass:** error is CE.

**bckwd pass:** ??