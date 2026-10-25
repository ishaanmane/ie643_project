Step (4) And $\alpha x + \gamma y \leq \beta$, valid for both R1 and R2

G use R1, R2 ... together to Red line.
$\Rightarrow$ There are lots of lines like the Red line (infinite)

* Stuber & Mehrotra, 1999
  Give the convex hull of $R_1 \cup R_2$ under the assumptions:
(i) $y$ = binary
(ii) $R_i$s are bounded
(iii) disjunctions used like $y_i=0$ or $y_i=1$

- Convex hull is given by $(x^1,y^1) \in R_1$, $(x^2,y^2) \in R_2$
  $(x,y) = \lambda^1(x^1,y^1) + \lambda^2(x^2,y^2)$ with $\lambda^1+\lambda^2=1$, $\lambda^1\geq0$, $\lambda^2\geq0$

[Diagram: A red line (convex hull boundary) through a set of marked points on an oval curve, illustrating the convex hull concept.]

$$M(x^1)$$
$$m = \begin{bmatrix} x_1^1 \\ x_1^2 \\ y_1^1 \\ y_1^2 \\ \lambda_1^1 \\ \lambda_1^2 \end{bmatrix}, \quad \text{assuming } y_1=0 \text{ or } y_1=1$$

Form new constraints in place of difficult set:
$$x = \bar{x}_1 + \bar{x}^2, \quad y = \bar{y}_1 + \bar{y}_2$$

difficult posn $\rightarrow$ base posn

$$\exists i(x^i,y^i)\leq0 \rightarrow cx$$
$$\exists i(x^2,y^2)\leq0 \rightarrow cx$$
$$x=\lambda^1x^1+\lambda^2x^2 \rightarrow ncx$$
$$y=\lambda^1y^1+\lambda^2y^2 \rightarrow ncx$$
$$\lambda^1+\lambda^2=1 \rightarrow cx$$
$$x^1,x^2\geq0 \rightarrow cx$$
$$y_1^1=0, y_1^2=1 \rightarrow cx$$