$$D = D_1 \oplus D_2$$
$D_1$: train partition
$D_2$: val partition

## Training loop:

for every epoch: (full pass over $D_1$)
&nbsp;&nbsp;&nbsp;&nbsp;for every minibatch $B_j$ in $D_1$:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\hat{y}(B_j) = \text{MLP}(B_j)$ // forward pass
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute loss($\hat{y}(B_j), y(B_j)$)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute error gradients wrt weights/biases of MLP $\rightarrow$ backpropagation: $w \leftarrow w + \eta(-\nabla e)$ $\rightarrow$ update weights, biases

after every $m$ epochs $\rightarrow$ validate model's perf on val-set.
