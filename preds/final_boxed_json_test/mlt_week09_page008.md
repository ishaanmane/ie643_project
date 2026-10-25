$$(w^{l+1})^Tw^* \geq (w^*{}^Tw^*) + l\gamma$$

$$\boxed{(w^{l+1})^Tw^* \geq l\gamma}$$

For any $(x,y)$,

[Diagram: A point $y$ on a line through the origin, with a dot at $\frac{x'y}{\|y\|^2}$ along the way.]

$$\left\|\left(\frac{x'y}{\|y\|^2}\right)y\right\|^2 \leq \|x\|^2 \quad \text{[Pythagoras]}$$

$$(x'y)^2 \frac{\|y\|^2}{\|x\|^2} \leq \|x\|^2$$
$$\Rightarrow (x'y)^2 \leq \|x\|^2\|y\|^2$$

**Cauchy-Schwarz Inequality**

From ②:
$$l^2 > (w^{l+1})^Tw^*$$
$$\Rightarrow l^2 > (w^{l+1}{}^Tw^*)^2 \leq \|w^{l+1}\|^2\|w^*\|^2 \quad \text{[from C-S]}$$

$$\Rightarrow \|w^{l+1}\|^2 \geq l^2 \gamma^2 \quad \boxed{③}$$