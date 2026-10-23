$w_3=x_2+x_3+x_4+x_5$, $w_4=w_3x_1$
$$0\leq x_1\leq10$$
$$0\leq w_3\leq40 \leftarrow \text{The bounds are bigger, no guarantee it is tight or not — can be bigger set (or) weak relaxation}$$

16/03/26

$$\text{min } f(x,y)$$
$$\text{st } g_i(x,y)\leq0$$
$$x\in\mathbb{R}^n, \; y\in\mathbb{Z}^p$$

[Diagram: A red blob region overlapping with a blue irregular region full of scattered "x" points, with "valid inequality" lines drawn tangent to the boundary, one line labeled "optimal sol" and another marked "not a valid inequality"; region labeled "Convex relaxation".]

Branch ⓑ (or) [not a useful cut] make relaxation tighter after getting a point. Starting point.

By branching the work increases as 1 problem becomes 2 & more common.

→ The better option is to tighten relaxation after we have an initial solution of relaxation.

→ before initial point we can't say is it tight or not.

→ The new relaxation is convex even by having a cut which is valid inequality.

→ A cut which not cuts feasible points is also valid inequality.

→ if valid inequality cuts off optimal point then it is not a valid inequality.

Given a model
$$\text{min } f(x,y)$$
(P) $g_i(x,y)\leq0, i=1,\dots,m$
$$x\in\mathbb{R}^n, \; y\in\mathbb{Z}^n$$
