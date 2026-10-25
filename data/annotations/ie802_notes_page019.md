Can we make good tight relaxation by looking at all constraints rather than doing term by term relaxation.

$$x_1^2-x_2^2+3x_1x_2\leq5$$
$$x_1^2=w_1, \quad x_2^2=w_2, \quad x_1x_2=w_3$$
$$w_1-w_2+3w_3\leq5$$

We know how to relax individual constraints but how to do on whole.

[Diagram: A parabola-like curve in $(x_1,x_2)$ plane from $(-1,1)$ to $(3,9)$, with a red "Convex hull" line connecting the endpoints, showing the true curve tightly bounded by the hull.]

**Ex 1:** ① $x_2=x_1^2$, $-1\leq x_1\leq3$ } $S_1$

if I take new constraint $x_1+x_2\leq1$ $S_2$

$S_1\cap S_2 \to$ [shaded lens shape] not tight as desired is [half-moon shape]

→ we do bound tightening. $x_2\in[0,9]$

from $(x_1+x_2\leq1)$ the $x_1$ can have bound: Upper bound of 1.
Now we update to $\boxed{-1\leq x_1\leq1}$ this gives better result.

② $x_1x_2\geq40$
$$0\leq x_1\leq10$$
$$0\leq x_2\leq10$$

add a new variable. $w_1=x_1x_2 \to w_1\geq40$, $0\leq x_1\leq10$, $0\leq x_2\leq10$ — outer box using bilinear relaxation

[Diagram: A 3D plot with vertices $(0,0,0)$, $(0,10,0)$, $(10,0,0)$, $(10,10,100)$ forming a tetrahedron-like shape.]

we get a curve where cut at 40, still non convex in 1 direction & reverse other side.
