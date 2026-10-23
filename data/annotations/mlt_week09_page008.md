$$(w^{\ell+1})^Tw^* \geq \underbrace{(w^{0T}w^*)}_{0} + \ell\gamma$$

$$\boxed{(w^{\ell+1})^Tw^* \geq \ell\gamma} \quad \text{---2}$$

---

## For any $(x,y)$

[Diagram: A triangle showing vector $x$, its projection $\left(\frac{x^Ty}{\|y\|^2}\right)y$ onto vector $y$, and the perpendicular residual.]

$$\left\|\left(\frac{x^Ty}{\|y\|^2}\right)y\right\|^2 \leq \|x\|^2 \quad \text{[Pythagorous]}$$
$$(x^Ty)^2\frac{\|y\|^2}{\|y\|^4} \leq \|x\|^2 \;\Rightarrow\; (x^Ty)^2 \leq \|x\|^2\|y\|^2$$

**Cauchy-Schwartz Inequality**

From ②: $\ell\gamma \leq (w^{\ell+1})^Tw^*$
$$\Rightarrow \ell^2\gamma^2 \leq \left((w^{\ell+1})^Tw^*\right)^2 \leq \|w^{\ell+1}\|^2\underbrace{\|w^*\|^2}_{1} \; [\text{From C.S}]$$

$$\Rightarrow \boxed{\|w^{\ell+1}\|^2 \geq \ell^2\gamma^2} \quad \text{---3}$$
