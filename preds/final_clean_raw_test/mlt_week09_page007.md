$$\|w^{l+1}\|^2 = \|w^l + xy\|^2$$
$$= (w^l + xy)^T(w^l + xy)$$
$$= \|w^l\|^2 + 2(w^{l^T}x)y + \|x\|^2y^2 \quad \underbrace{\leq 0}_{\text{because mistake}} \quad \underbrace{=R^2}_{-+1}$$

$$\|w^{l+1}\|^2 \leq \|w^l\|^2 + R^2$$
$$\|w^{l+1}\|^2 \leq (\|w^{l-1}\|^2 + R^2) + R^2$$
$$\vdots$$
$$\|w^{l+1}\|^2 \leq \|w^0\|^2 + lR^2$$

$$\boxed{\|w^{l+1}\|^2 \leq lR^2} \quad \text{(no of mistakes)} \tag{①}$$

$$(w^{l+1})^Tw^* = (w^l + xy)^Tw^*$$
$$= w^{l^T}w^* + (w^{*^T}x)y \quad \underbrace{\geq \gamma}_{\text{?}}$$

$$(w^{l+1})^Tw^* \geq w^{l^T}w^* + \gamma$$
$$\geq (w^{l-1^T}w^* + \delta) + \gamma$$