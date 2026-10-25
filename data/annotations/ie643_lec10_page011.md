[Diagram: Computational graph tree. Root: $\phi \to a_1 \to f(a_1,y) \to e$. Below $\phi$: $z_1 \to + \to (v_1, v_2)$; $v_1 = * (x_1, w_1)$, $v_2 = *(x_2, w_2)$.]

[Diagram: A separate node labeled $w_{ij}^l$.]

$$\frac{\partial e}{\partial w_{ij}^l} = \frac{\partial e}{\partial z_i^l} \cdot \frac{\partial z_i^l}{\partial w_{ij}^l}$$
