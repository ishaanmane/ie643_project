Continuous Non-convex Quadratic Models:

$$\min \frac{1}{2}x^TQx + c^Tx$$
$$\text{st } \frac{1}{2}Q_i x^T Q_i x + q_i^T x \leq b_i$$
$$l \leq x \leq u$$

**0 Multistart NLP Heuristic**
- Give it to a local gradient based solver

[Diagram: A wavy curve with a local minimum marked at the start, and another point further along the curve.]

also give them another point, if not good then previous take another point

**0 Under cover heuristic**
- You pick some $x$ values
  suppose p=100
  $\Rightarrow$ pick 90 and fix for some values

$$x_1^2+5x_1x_2+7x_3x_4+x_1x_3-2x_1x_4 \leq 1$$

**ISAC Heuristic**
$x_1=2$, $x_3=1$
$\rightarrow$ next choose values and solve NLP (take $x_1,x_2$ as anything, change available)

- how to know which variable to pick and what value? $\rightarrow$ Trial and error

[Diagram: A graph with nodes $x_1, x_2, x_3, x_4$ — $x_1$ has edges to $x_2$ and $x_4$, $x_3$ has an edge to $x_4$.]

pick smallest node so that every set is covered.
- G find smallest node (edge) cover fan this graph so that every edge is covered.

$(x_1,x_3)$ & $(x_1,x_4)$ Solve..