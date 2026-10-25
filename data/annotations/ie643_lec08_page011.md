$$\delta^l = (W^{l+1})^T \text{Diag}(\phi')^{l+1} \delta^{l+1}$$
$$\vdots$$
$$\delta^l = (W^{l+1})^T \text{Diag}(\phi')^{l+1} (W^{l+2})^T \text{Diag}(\phi')^{l+2} \cdots (W^L)^T \text{Diag}(\phi')^L \delta^L$$

[Diagram: A chain of layer boxes from $x$ through $\delta^l, \delta^{l+1}, \delta^{l+2}, \dots, \delta^{L-1}, \delta^L$, labeled "Backpropagation of error derivatives."]

$$w^{k+1} \leftarrow w^k - \eta_k \left(-\sum_{j \in B_k} \nabla e(y^j, \hat{y}^j)\right)$$
