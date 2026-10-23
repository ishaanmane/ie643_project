$$E = \|\text{vec}(ABX) - \text{vec}(Y)\|^2$$

When we fix $A$: $E = \|M \, \text{vec}(B) - \text{vec}(Y)\|^2$

Suppose $z = \text{vec}(B)$, $c = \text{vec}(Y)$

$$E = \|Mz-c\|_2^2 = (Mz-c)^T(Mz-c) = (z^TM^T - c^T)(Mz-c)$$
$$= z^TM^TMz - 2(Mz)^Tc + c^Tc$$

$$F(z) = \|Mz-c\|^2$$
$$\nabla F(z) = 2M^TMz - 2M^Tc$$
$$\nabla^2 F(z) = 2M^TM$$

$M^TM$ is p.s.d.
