$$\therefore (y-X^T\alpha^*)^T(X^T\alpha^*) = 0$$
$$y^TX^T\alpha^* - \alpha^{*T}(XX^T)\alpha^* = 0 \quad \text{---1}$$

Substituting $w^*=(XX^T)^+Xy$ as $w^*=\alpha^*$ on LHS we get,

$$y^TX^T(XX^T)^+Xy - \left[(XX^T)^+Xy\right]^T(XX^T)\left[(XX^T)^+Xy\right] = 0$$

**Conclusion:** $X^Tw^*$ is the "PROJECTION" of the labels onto the subspace spanned by the features.
