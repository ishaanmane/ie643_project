$$(w^{l+1})^Tw^* \geq \frac{(w^0)^Tw^*}{0} + l\delta$$

$$\boxed{(w^{l+1})^Tw^* \geq l\delta}$$

---

For any $(x,y)$,

[Diagram: A point $y$ on the right of a squiggly curve, with a dashed line from it to a point on the curve labeled $\frac{x\cdot y}{\|y\|^2}y$, and an arrow from that point to $y$.]

$$\left\|\frac{x\cdot y}{\|y\|^2}y\right\|^2 \leq \|x\|^2 \quad \text{[Pythagoras]}$$

$$(x\cdot y)^2 \frac{\|y\|^2}{\|y\|^p} \leq \|x\|^2$$
$$\Rightarrow (x\cdot y)^2 \leq \|x\|^2\|y\|^2$$

**Cauchy-Schwarz Inequality**

From ②
$$l\gamma \leq (w^{l+1})^Tw^*$$
$$\Rightarrow l^2\gamma^2 \leq (w^{l+1}^Tw^*)^2 \leq \|w^{l+1}\|^2\|w^*\|^2 \quad \text{[from C-S]}$$

$$\Rightarrow \|w^{l+1}\|^2 \geq l^2\gamma^2 \quad \text{③}$$