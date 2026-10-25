**Continuous Non-convex Quadratic Models:**

$$\min \frac{1}{2}x^TQx+c^Tx$$
$$\text{st } \frac{1}{2}x^TQ_ix+a_i^Tx\leq b_i$$
$$l\leq x\leq u$$

⊙ **Multistart NLP Heuristic**
- Give it to a local gradient based solver

[Diagram: A wavy non-convex curve with a local minimum circled at "Start" and another point marked further right with an arrow.]

→ also give them another point, if not good then previous take another point.

⊙ **Undercover heuristic**
- You pick some $x$ values, suppose $p=100$ → pick 90 and fix for some values

$$x_1^2+5x_1x_2+7x_3x_4+x_1x_3-2x_1x_4\leq1$$

1st iteration: $x_1=2$, $x_3=1$ → next change values and solve NLP; take $x_1$ as anything, $x_4$ (change variable)

- How to know which variable to pick and what values... → graph → trial and error

[Diagram: A graph with node $x_1$ (with a self-loop) connected to $x_2$, $x_3$, $x_4$, with an additional edge between $x_3$ and $x_4$.]

... pick smallest node so that every set is covered..
- Find smallest node (edge) cover for this graph so that every edge is covered..
$(x_1,x_3)$, $(x_1,x_4)$ → solve..
