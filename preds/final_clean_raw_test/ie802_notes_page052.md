## Continuous Non-Convex Quadratic Models:

$$\min \frac{1}{2}x^TQx + c^Tx$$
$$\text{s.t. } \frac{1}{2}Q_0x^TQ_1x + q_1^Tx \leq b_1$$
$$l \leq x \leq u$$

**O Multistart NLP Heuristic:** Give it to a local gradient based solver.

[Diagram: A wavy curve with a local minimum at the left, a local maximum in the middle, and another local minimum on the right, labeled "Start" at the left minimum.]

also give them another point, if not good then previous take another point

**O Under cover heuristic**
- You pick some $x$ values
  suppose p=100
  $\Rightarrow$ pick go and fix X for some values

$$x_1^2+5x_1x_2+7x_3x_4+x_1x_3-2x_1x_4 \leq 1$$

**1st Heuristic**
$x_1=2$, $x_3=1$ → next change values and solve NLP
take $x_1$ as any thing (change variable)
take $x_4$ as any thing (change variable)

- how to know which variable to pick and what value? → Trial and error

[Diagram: A graph with nodes $x_1, x_2, x_3, x_4$ — $x_1$ has edges to $x_2$ and $x_3$, $x_3$ has an edge to $x_4$.]

...pick smallest node so that every set is covered.
→ find smallest node (edge) cover for this graph so that every edge is covered.

$(n_1,n_3)$ & $(n_1,n_4)$ Solver..