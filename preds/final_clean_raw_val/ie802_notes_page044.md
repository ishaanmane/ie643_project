Step (4) Find $\alpha x + \beta y \leq \gamma$ valid for both R1 and R2

$\Rightarrow$ Use $R_1, R_2 \dots$ together to get red line.
$\Rightarrow$ There are lots of lines like the red line (infinite)

* Sturker & Mehndha, 1999
  Give the convex hull of $R_1 \cup R_2$ under the assumptions...
(i) $y$ = binary
(ii) $R_i$s are bounded
(iii) disjunctions used like $y_1=0$ or $y_1=1$

[Diagram: An oval-shaped region with several grid lines crossing it, labeled with "x" at various points along the axes.]

- Convex hull is given by $(x^1,y^1) \in R_1$, $(x^2,y^2) \in R_2$
  $(x,y) = \lambda^1(x^1,y^1) + \lambda^2(x^2,y^2)$ with $\lambda^1+\lambda^2=1$, $\lambda^1\geq0$, $\lambda^2\geq0$

$$M(x^1)$$
$$m = \left\{(x_1^1,y_1^1), (x_2^1,y_2^1), (\lambda^1,\lambda^2)\right\}$$

Assuming, $y_1=0$ or $y_1=1$

$$g_i(x^1,y^1) \leq 0 \rightarrow \text{cx}, \quad g_i(x^2,y^2) \leq 0 \rightarrow \text{cx}$$
$$x = \lambda^1x^1 + \lambda^2x^2 \rightarrow \text{NCX}$$
$$y = \lambda^1y^1 + \lambda^2y^2 \rightarrow \text{NCX}$$
$$\lambda^1+\lambda^2=1 \rightarrow \text{cx}$$
$$x^1,x^2\geq0 \rightarrow \text{cx}$$
$$y_1^1=0 \qquad \; \rightarrow \text{cx}$$
$$y_1^2=1 \qquad \; \rightarrow \text{cx}$$

Form new constraints in place of difficult part: $x=\bar{x}_1+\bar{x}^2$, $y=\bar{y}_1+\bar{y}_2$. Cure some trick.