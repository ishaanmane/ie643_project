**Step ④**
Find $\alpha x+\gamma y\leq\beta$ valid for both $R_1$ and $R_2$

→ use $R_1, R_2$ ... to get to Red line.
→ There are lots of lines like the Red line (infinite)

**Stubbs & Mehrotra, 1999**

Give the convex hull of $R_1\cup R_2$ with the assumptions..
(i) $y \to$ binary
(ii) $R$'s are bounded
(iii) disjunctions used like $y_i=0$ or $y_i=1$

Convex hull is given by:
$$(x^1,y^1)\in R_1$$
$$(x^2,y^2)\in R_2$$
$$(x,y)=\lambda^1(x^1,y^1)+\lambda^2(x^2,y^2)$$
with $\lambda^1+\lambda^2=1$, $\lambda^1\geq0$, $\lambda^2\geq0$

$$M = \left\{(x_1^1,y_1^1,x_2^2,y_2^2,\lambda_1,\lambda_2^2):\right.$$
$$g_i(x^1,y^1)\leq0 \to \text{cx}$$
$$g_i(x^2,y^2)\leq0 \to \text{cx}$$
$$x=\lambda^1x^1+\lambda^2x^2 \to \text{NCX}$$
$$y=\lambda^1y^1+\lambda^2y^2 \to \text{NCX} \to \text{very difficult part}$$
$$\lambda^1+\lambda^2=1 \to \text{cx}$$
$$x^1,\lambda^2\geq0 \to \text{cx}$$
$$y_1^1=0 \Big\} \to \text{cx}$$
$$y_1^2=1 \Big\}$$

Assuming $y_i=0$ or $y_i=1$. Form new constraint in place of difficult one:
$$a=\bar{x}_1+\bar{x}_2, \quad b=\bar{y}_1+\bar{y}_2 \leftarrow \text{use some trick}$$
