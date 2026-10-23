It does not have any square terms

$$x_1y_1\geq1$$
$$x_1\geq0$$
$$y_1\geq0 \text{ integer}$$

To find outer approximation convex hull of points, it becomes flatter and flatter as goes to $\infty$ segments

$$y_1\geq1$$
$$\vdots$$

Infinitely many linear constraints

$$S=\begin{cases}x_1y_1+x_2y_2+x_3y_3+\dots x_ny_n\geq\gamma\\x\geq0\\y\geq0 \; \text{continuous}\end{cases}$$

convex hull of $S$?

Consider $\gamma=6$, set $S$ is Non-convex.
take $x_1=3, y_1=2$ and other values $=0$
$x_2=x_3=\dots x_n=0$, $y_2=y_3=\dots y_n=0$

we can show convex hull of $S$ is given by ... divide both sides by $\gamma$ and take $\sqrt{}$

$$\text{Conv}(S) = \left\{\sqrt{\frac{x_1y_1}{\gamma}}+\sqrt{\frac{x_2y_2}{\gamma}}+\dots+\sqrt{\frac{x_ny_n}{\gamma}}\geq1\right\}$$

The result won't work when we make change in equation like $x_2y_1$ as $x_1^2$

* Every point feasible in top original formulation is also point in relaxation which is in bottom

26/02/26

$$x_1y_1\geq1$$
$$x_1\geq0$$
$$y_1\geq0, \; y\to\text{continuous}$$

[Diagram: A hyperbola-like decreasing curve with sample points $(1,1)$, $(2,1/2)$, $(2,1/3)$, arrows pointing up from each labeled "above possible" → relaxation.]

Pure bilinear term $y_1y_2, x_1y_2$ Not allowed.

Due to no upper bound → we can't try... we can still use SDP.
