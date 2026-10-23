In our problem,
$$\frac{\alpha^*(1-(w^{*T}x_i)y_i)}{g(w^*)} = 0 \; \forall i$$

$\Rightarrow$ If $\alpha^*>0 \Rightarrow 1-(w^*x_i)^Ty_i=0$
$\Downarrow$
$(w^*x_i)^Ty_i=1$ → This means that only the points on the margin contribute to $w^*$.
$\alpha^*=0$ for the points not on the margin line.

[Diagram: Green "+" points and red "−" points separated by a line through the origin with normal $w^*$; points sitting exactly on the two margin boundaries $\{x:(w^{*T}x)y=1\}$ and $\{x:(w^{*T}x)y^{-1}=-1\}$ are boxed/highlighted.]

- These special points on "Supporting" hyperplanes are called **"SUPPORT VECTOR"**
- The algorithm is called **Support Vector Machine (SVM)**
- $w^*$ is a sparse linear combination of the data points
