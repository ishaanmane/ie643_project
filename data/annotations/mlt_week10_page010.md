# Support Vector Machines

## Revisiting the Lagrangian

**Primal** $\min_w\left[\max_{\alpha\geq0} f(w)+\alpha g(w)\right] \equiv$ **Dual** $\max_{\alpha\geq0}\left[\min_w f(w)+\alpha g(w)\right]$

$w^*$ is the primal solution; $\alpha^*$ is the dual solution

$$\max_{\alpha\geq0} f(w^*)+\alpha g(w^*) \qquad \min_w f(w)+\alpha^*g(w)$$

$$f(w^*) = \min_w f(w)+\alpha^*g(w) \leq f(w^*)+\alpha^*g(w^*)$$

$$\Rightarrow f(w^*) \leq f(w^*)+\alpha^*g(w^*)$$
$$\Rightarrow \boxed{\alpha^*g(w^*)\geq0} \quad \text{---1}$$

But we already know $\alpha^*\geq0$ & $g(w^*)\leq0$
$$\Rightarrow \boxed{\alpha^*g(w^*)\leq0} \quad \text{---2}$$

① & ② $\Rightarrow$ $\boxed{\alpha^*g(w^*)=0}$ → **COMPLEMENTARY SLACKNESS**

For multiple constraints, $\boxed{\alpha_i^*g_i(w^*)=0 \; \forall i}$
