## Recap: Auto-differentiation ideas

$$z = a*b+c$$
$$u = \phi(z)$$

[Diagram: Two small computational graph chains — $u \to \phi \to z$ (forward) and $\partial u/\partial u \to \phi_{bck} \to \partial u/\partial z$ (backward); a separate tree for $z = a*b+c$: $z \to + \to (v_1, c)$, $v_1 \to * \to (a,b)$.]

```
def fwd():
```

Computation graph: $z = a*b+c$

[Diagram: A wider computational graph for $z = w_1 x_1 + w_2 x_2 + w_3 x_3 + \dots$, built from chained $+$ and $*$ nodes over $w_1,x_1,w_2,x_2,w_3,\dots$.]
