$$(w^{l+1})^Tw^* \geq (w^*)^Tw^* + \ell\delta$$

$$\boxed{(w^{l+1})^Tw^* \geq \ell\delta}$$

---

For any $(x,y)$,

[Diagram: A point $y$ on the axis with a dashed line to an off-axis point labeled $x$, and a dot at the origin.]

$$\left\|\frac{x^Ty}{\|y\|^2}y\right\|^2 \leq \|x\|^2 \quad \text{[Pythagoras]}$$

$$(x^Ty)^2 \frac{\|y\|^2}{\|y\|^4} \leq \|x\|^2$$

**Cauchy-Schwarz Inequality**

$$(x^Ty)^2 \leq \|x\|^2\|y\|^2$$

From ②:
$$\ell^2 \leq (w^{l+1})^Tw^*$$
$$\Rightarrow \ell^2 \leq ((w^{l+1})^Tw^*)^2 \leq \|w^{l+1}\|^2\|w^*\|^2 \quad \text{[from C-S]}$$

$$\Rightarrow \|w^{l+1}\|^2 \geq \ell^2$$