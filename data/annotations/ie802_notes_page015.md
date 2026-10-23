**Example:** $\dfrac{x_1^2+x_2^2}{3x_1+x_3}+5x_1x_2\leq6$

Linearise.
$$x_1^2=w_1, \quad x_1x_2=w_2, \quad 3x_1+x_3=w_3, \quad \frac{1}{w_3}=w_4, \quad x_2^2=w_5$$
$$w_6=w_4\cdot w_5$$
$$w_1+w_6+5w_2\leq6$$

Solve and find $(\hat{x},\hat{w})$. Check if all satisfies. If anyone not → do branching.

- To draw box around terms, we need bound on $x_1$, i.e. $\leq x_1\leq$, $\leq x_2\leq$
  also on $\leq w_1\leq$, $\leq w_2\leq\dots$

**Example:** Min $x_1-10x_2$
$$x_1^2\leq2x_2$$
$$-x_1^2+4x_2\leq4$$
$$-100\leq x_1,x_2\leq100$$

Introduce new variables. LP relaxation

**Soln:** $w_1=x_1^2$
$$w_1\leq2x_2$$
$$-w_1+4x_2\leq4$$

[Diagram: A parabola $w_1=x_1^2$ with a shaded band around the vertex, labeled "search space smaller" after bound tightening, over range $-2\leq x_1\leq2$.]

$$0\leq w_1\leq10{,}000$$
$$-100\leq x_1\leq100$$

Tightening bound from one constraint: $x_1^2\leq200$, $x_1\leq\sqrt{200}$, $-14.1\leq x_1\leq14.1$

After bound tightening, our search space reduces and also secant reduces.

Second const: $-x_1^2+4x_2\leq4$
$$x_1^2\geq4x_2-4 \geq -400-4=-404 \to \text{Not much in B}\dots$$
