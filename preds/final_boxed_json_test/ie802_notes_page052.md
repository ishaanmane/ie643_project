## Continuous Non-convex Quadratic Models:

$$\min \frac{1}{2}x^TQx + c^Tx$$
$$\text{st } \frac{1}{2}\otimes_i x^TQ_ix + a_i^Tx \leq b_i$$
$$l \leq x \leq u$$

**O Multistart NLP Heuristic:** Give it to a local gradient based solver.

[Diagram: A wavy curve with a local minimum marked at a point near the left, labeled "Start", and another point further right.]

also give them another point, if not good then previous take another point

**O Under cover heuristic**
- You pick some $x$ values, suppose p=100 $\Rightarrow$ pick 90 and fix for some values
$$x_1^2+5x_1x_2+7x_3x_4+x_1x_3-2x_1x_4 \leq 1$$

1st iteration:
$x_1=2$, next change values and solve NLP
$x_3=1$, after $x_1$ $x_2$ as any thing (change variable) $\rightarrow$ Trial and error

- how to know which variable to pick and what values...
$\hookrightarrow$ Graph

[Diagram: A tree graph — root $x_1$ branching into $x_2$, $x_3$, $x_4$.]

pick smallest node so that every set is covered...
- G find smallest node (cover) cover fan this graph so that every edge is covered...

$(x_1,x_3)$ $(x_1,x_4)$ $\hookrightarrow$ Solve...