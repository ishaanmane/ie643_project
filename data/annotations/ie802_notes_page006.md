**Methods for Global Optimization:**

Ex: $\min x_1-2x_2$
$$\text{st } x_1^2+2x_2\leq0$$
$$-x_1^2+4x_2\leq4$$
$$x_1,x_2\in\mathbb{R}$$

[Diagram: A curve with local minimum marked at $(-2,2)$ labeled "Global optimal", a saddle-like point at $(0,1)$, and another critical point at $(2,2)$ labeled "local optimal", with a red line through $(0,0)$ representing the level set "$\lambda$ of $x_1-2x_2=(0)$".]

$\to$ **Convex hull**: [Diagram: a bowl-shaped curve with a shaded region beneath a chord, labeled "relaxation".]

**ex:** Convex hull of set $S$ = minimal closed convex set containing $S$

**ex:** [Diagram: An irregular blob shape $S$ shaded, enclosed within its convex hull (a larger smooth oval outline), with the gap between them labeled "convex hull".]

→ weak convex relaxation "Easy to get"; hard: as hard as solving to problem itself

How to get these weak convex relaxations?

**Ex:** Min $x_1+2x_2+3x_3-x_4$
$$\text{st } x_1^2+x_2^2-x_3^2+x_5^2-x_4^2=7 \; \Big\} \text{Non-linear + Non-convex}$$
$$3x_2+x_3-x_4+3x_5=1$$
$$0\leq x_i\leq10, \quad i=1,2\dots5$$
