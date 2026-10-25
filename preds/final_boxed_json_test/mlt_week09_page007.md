$$\|w^{l+1}\|^2 = \|w^l + xy\|^2$$

$$= (w^l + xy)^T(w^l + xy)$$

$$= \|w^l\|^2 + 2(w^Tx)y + \|x\|^2y^2 \leq 0 \quad \text{because mistake}$$

$$\|w^{l+1}\|^2 \leq \|w^l\|^2 + R^2$$
$$\|w^{l+1}\|^2 \leq (\|w^{l-1}\|^2 + R^2) + R^2$$
$$\vdots$$
$$\|w^{l+1}\|^2 \leq \|w^0\|^2 + lR^2$$
$$\|w^{l+1}\|^2 \leq lR^2 \quad \text{(no. of mistakes)}$$

$$(w^{l+1})^Tw^* = (w^l + xy)^Tw^*$$
$$= w^Tw^* + (w^{*^T}x)y \geq \gamma$$

$$(w^{l+1})^Tw^* \geq w^Tw^* + \gamma$$
$$\geq (w^{l-1}^Tw^* + \gamma) + \gamma$$