[Diagram: Margin lines $\{x:w_1^Tx=5\}$ rescaled to $\{x:(w_1/5)^Tx=1\}$, i.e. $w_1'^Tx=1$.]

$$\max_w \text{width}(w) \quad \text{such that, } (w^Tx_i)y_i \geq 1 \; \forall i \quad \left(\text{was } \gamma, \text{now fixed to } 1\right)$$

What is width($w$)?

[Diagram: A rhombus formed by the margin lines $\{x:w^Tx=-1\}$ and $\{x:w^Tx=1\}$ around the origin, with points $x, z$ on opposite margins and $w$ as normal.]

$$\min_z \frac{1}{2}\|x-z\|^2 \quad \text{s.t. } w^Tz=+1 \qquad \boxed{w^Tx=-1}$$

**Solution:** $\text{width}(w) = \dfrac{2}{\|w\|^2}$

---

$$\boxed{\max_w \frac{2}{\|w\|^2} \text{ such that } (w^Tx_i)y_i\geq1\;\forall i} \qquad \boxed{\min_w \frac{1}{2}\|w\|^2 \text{ such that } (w^Tx_i)y_i\geq1\;\forall i}$$
