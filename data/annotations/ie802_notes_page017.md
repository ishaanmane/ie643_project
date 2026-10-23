**Optimization based Bound tightening:**

$$\min w_1$$
$$\text{st Linear constraint (outer approx)} + \text{(original linear constraints)}$$

→ one gets lower bound and another gives higher bound..
$$\max w_1$$

**Ex:** [Diagram: two rectangles labeled "x500 piece" and "x100 piece", question "How many?"]

- look at single constraint and also by combining...

**Ex:** $x_1^2+2x_1x_2+x_2^2\leq100$

Individual terms → problem, but if we combine: $(x_1+x_2)^2 \to$ much tighter bound.

- How to relax ← Global opt...
- How to branch, we have studied...?

What happen when we have relaxation of original problem vs their constraints.

$$\min c^Tx$$
$$g_1(x)\leq0$$
$$g_2(x)\leq0$$

[Diagram: Two irregular boomerang-shaped regions labeled $g_1(x)\leq0$ and $g_2(x)\leq0$, overlapping in a small shaded intersection region, and a separate small quadrilateral shape.]

Create outer approximation of both.

**Ideal:** exact relaxation of intersection of two feasible sets.

**Normal:** Relax $g_1(x)$ and then relax $g_2(x)$ → Take intersection of both relaxations.

[Diagram: A quadrilateral with a diamond cut out, and a tangled curve shape, labeled "extremely big".]
