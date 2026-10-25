[Diagram: A chain of fully-connected layers (left) vs. a fully-connected layer feeding into a single output neuron (right).]

$$\delta^l = (W^{l+1})^T \text{Diag}(\phi'^{l+1}) \cdot \boxed{\delta^{l+1}}$$

**front pass:** error is $C\epsilon$

**backward pass:** ??