05/03/26

$$\text{min } x_1+2x_2+3x_3-x_4$$

Ⓐ st $x_1^2+x_2^2-x_3^2-x_4^2+x_5^2=7 \to$ Non convex
$$3x_2+x_3-x_4+3x_5=1$$
$$0\leq x_i\leq10, \; i=1\dots5$$

**Transform: Ⓟ**

$w_1+w_2-w_3-w_4+w_5=7$
$w_1=x_1^2$
$w_2=x_2^2$
$w_3=x_3^2$
$w_4=x_4^2$
$w_5=x_5^2$
$0\leq x_i\leq10, \; i=1\dots5$

To put a lid, we need to know the bounds of $x_i$; we want to be online

[Diagram: Parabola $w=x_1^2$ over $[0,10]$, with a red chord/secant labeled "chord (or secant)" from the origin to $(10,100)$, and a second sketch showing a tangent line at $(u_2, u_2^2)$ touching the curve near $(0,0)$ and $(l_1,l_1^2)$ — "secant works only for square types".]

equality, $x_1^2-w_1=0$
$$\boxed{g(\hat{x})+\nabla g(\hat{x})^T(x-\hat{x})\leq0} \leftarrow \text{This doesn't depend on bound}$$
