Can we swap min & max in B?

**Only if $f$ & $g$ are convex functions** (quadratic or linear)

$$\min_w\left[\max_{\alpha\geq0} f(w)+\alpha g(w)\right] \equiv \max_{\alpha\geq0}\left[\min_w f(w)+\alpha g(w)\right]$$

---

## For multiple constraints

$$\boxed{\min_w f(w) \text{ s.t. } g_i(w)\leq0, \; i=1,\dots,k}$$

$$\equiv \min_w\left[\max_{\alpha_1,\dots,\alpha_k\geq0} f(w)+\alpha_1g_1(w)+\alpha_2g_2(w)+\dots+\alpha_kg_k(w)\right]$$

$$\equiv \max_{\alpha_1\geq0,\dots,\alpha_k\geq0}\left[\min_w f(w)+\alpha_1g_1(w)+\dots+\alpha_kg_k(w)\right]$$
