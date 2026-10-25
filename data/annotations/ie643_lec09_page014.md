[Diagram: A softmax output layer — activations feed through weight $w$ into a neuron with multiple output arrows, and a wider fully-connected diagram: nodes $O_1, O_2, \dots$ fully connect to output nodes producing $\hat{y}_1, \hat{y}_2, \dots, \hat{y}_C$.]

$$\delta^l = (W^{l+1})^T \, \text{Diag}(\phi'^{l+1}) \cdot \delta^{l+1} \; \rightarrow \; \delta^L$$

fwd pass: error is CE.
bckwd pass: ??
