$$\|w^{\ell+1}\|^2 = \|w^\ell+xy\|^2 = (w^\ell+xy)^T(w^\ell+xy) = \|w^\ell\|^2 + 2(w^{\ell T}x)y + \|x\|^2y^2$$

($2(w^{\ell T}x)y \leq 0$ because mistake; $\|x\|^2y^2 \leq R^2$)

$$\|w^{\ell+1}\|^2 \leq \|w^\ell\|^2 + R^2 \leq (\|w^{\ell-1}\|^2+R^2)+R^2 \leq \dots \leq \underbrace{\|w^0\|^2}_{=0}+\ell R^2$$

$$\boxed{\|w^{\ell+1}\|^2 \leq \ell R^2} \quad \text{(}\ell \to \text{no. of mistakes)} \quad \text{---1}$$

$$(w^{\ell+1})^Tw^* = (w^\ell+xy)^Tw^* = w^{\ell T}w^* + \underbrace{(w^{*T}x)y}_{\geq\gamma}$$

$$(w^{\ell+1})^Tw^* \geq w^{\ell T}w^* + \gamma \geq (w^{\ell-1T}w^*+\gamma)+\gamma \geq \dots$$
