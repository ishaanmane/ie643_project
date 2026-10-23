From ② and ④: $(x_1+1)(x_2+1)\geq0$, $w_1+x_1+x_2\geq0$

From ① and ④: $(2-x_1)(x_2+1)\geq0$, $2-x_1+2x_2-w_1\geq0$

also solve ② and ③: [similar cross-product]

$$w_1\geq2x_1+2x_2+4$$
$$w_1\geq-x_1-2x_2-1$$
$$w_1\leq-x_1+2x_2+2$$
$$w_1\leq2x_1-x_2+2$$
$\{x\geq0,y\geq0\}$, $Z=xy$

$$3x_1^2+4x_2^2-7x_1x_2+8x_3x_4+8x_3+x_4\leq10$$
$$x_1^2=w_1, \quad x_2^2=w_2, \quad x_1x_2=w_3, \quad x_3x_4=w_4$$
$$3w_1+4w_2-7w_3+8w_4+8x_3+x_4\leq10$$

Let $(\hat{x},\hat{w})$ be the LP solution with $\hat{w}_3\neq\hat{x}_1\hat{x}_2$?? → use cut on branch. Not possible bc cutting other points.

$\hat{x}_1=1$, $\hat{x}_2=1$, $\hat{w}_3=1/2$ → branch on any one.

**Lemma:** Let $(\hat{x}_1,\hat{x}_2,\hat{w})$ be any point inside the LP relaxation of $w=x_1x_2$ with $l_1\leq x_1\leq u_1$ and $l_2\leq x_2\leq u_2$.

If $\hat{x}_1=l_1$ then $\hat{w}=\hat{x}_1\hat{x}_2$. Similarly, if $\hat{x}_1=u_1$ then...
Sim. if $\hat{x}_2=l_2\dots$
If $\hat{x}_2=u_2\dots$
