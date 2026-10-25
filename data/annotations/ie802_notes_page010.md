[Diagram: A crescent/wedge-shaped feasible region with point $(\hat{x},\hat{w})$ marked inside — "we can get such a point in simplex".]

① There are lot of variables in high dimension, such cases happen via simplex.

But not on the curve (so) 2 things happen:
1) Above the curve:
2) Below the curve: if $\hat{w}_1<\hat{x}_1^2$, add a tangent at $(\hat{x}_1,\hat{x}_1^2)$

We will find a point on curve, to set tangent
1) by drawing a line vertically.
2) try to find nearest point on curve to get the tangent.

[Diagram: Two curve sketches showing a point $(\hat{x},\hat{w})$ inside the region between the curve and a chord, with a red vertical line and a labeled tangent construction; a second small diagram shows "secant", "Child1", "Child2" nodes.]

1) **Above the curve:**

We do branch & bound. Child① | Child②

→ We will draw a secant that cut points in both splitted individual childs.

All we need is, we don't count that point & we don't want to lose our original feasible region (curve).

→ at the corners, the secant cuts off the point because the secant is tight at corners.

Here there is no integer requirements, but we do branch & bound, there will be many cases (or branches) as not integer.
