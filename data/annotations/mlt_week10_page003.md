# Maximum Margin: Formulation

**Goal:** To come up with a formulation that maximizes "margin"

$$\max_{w,\gamma} \gamma \quad \text{such that: } (w^Tx_i)y_i \geq \gamma \; \forall i$$

**Issue:** Can scale $w$ arbitrarily

**improved**
$$\max_{w,\gamma} \gamma \quad \text{such that } (w^Tx_i)y_i \geq \gamma, \; \|w\|^2=1$$

After fixing $w$, $\gamma$ becomes a function of $w$

[Diagram: Two parallel margin lines around two candidate normal vectors $w_1,w_2$, labeled $\{x:w_1^Tx=5\}$ and $\{x:w_2^Tx=3\}$.]

After fixing $\gamma$ to a constant (say 1),
