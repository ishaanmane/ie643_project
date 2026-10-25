Step (4) And $\alpha x + \beta y \leq \beta$ valid for both R1 and R2

$\Rightarrow$ use R1, R2 ... together to get red line.

$\Rightarrow$ There are lots of lines like the red line (infinite)

* Stuber & Mehrotra, 1999

Give the convex hull of $R_1 \cup R_2$ under the assumptions:
(i) $y$ = binary
(ii) $R_i$s are bounded
(iii) disjunctions used like $y_i=0$ or $y_i=1$

- Convex hull is given by $(x^1,y^1) \in R_1$, $(x^2,y^2) \in R_2$
  $$(x,y) = \lambda^1(x^1,y^1) + \lambda^2(x^2,y^2)$$ with $\lambda^1+\lambda^2=1$, $\lambda^1\geq0$, $\lambda^2\geq0$

[Diagram: A red line through a set of points, with several supporting lines drawn from the origin to points on the red line.]

$$M(x^1) = \int (x_1^1y_1^1, x_1^2y_1^2, \lambda_1^1\lambda_2^2)$$

Assuming $y_1=0$ or $y_1=1$

$$\exists_1(x^1,y^1)\leq0 \rightarrow cx$$
$$\exists_1(x^2,y^2)\leq0 \rightarrow cx$$
$$x=\lambda^1x^1+\lambda^2x^2 \rightarrow NCX$$
$$y=\lambda^1y^1+\lambda^2y^2 \rightarrow NCX$$
$$\lambda^1+\lambda^2=1 \rightarrow CX$$
$$\lambda^1,\lambda^2\geq0 \rightarrow CX$$
$$y_1^1=0 \quad \exists \rightarrow CX$$
$$y_2^2=1 \quad \exists \rightarrow CX$$

Form new constraints in place of difficult ones: $x=\vec{x}_1+\vec{x}_2$, $y=\vec{y}_1+\vec{y}_2$. Use some trick.