[Diagram: A large computational graph — $z = w_1 x_1 + w_2 x_2 + \dots + w_d x_d$, built as a tree: $u \leftarrow + \leftarrow (v_1, v_2)$ chained further with $v_3, \dots$, each $v_i = *(x_i, w_i)$, with a backward pass branch $*_{bck}, \phi_{bck}$ shown at left connecting to $\partial v_1/\partial x_1, \partial v_1/\partial w_1$.]

$$z = w_1 x_1 + w_2 x_2 + \dots + w_d x_d$$
