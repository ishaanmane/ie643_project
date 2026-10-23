2 constraints at a time:
$$x_1^2-2x_2\leq0$$
$$-x_1^2+4x_2\leq4$$
$$\overline{2x_2\leq4}$$
gives, $x_2\leq2$

Using this in constraint 1: $x_1^2\leq2x_2$, $x_1^2\leq4$, which gives $\boxed{-2\leq x_1\leq2}$

**Ex:** $x_1^2+5x_1x_2+12x_2^2+7x_3^2-5x_1x_3\leq20$, $-1\leq x\leq5$

$x_1^2=w_1$, $x_1x_2=w_2$, $w_1\in[0,25]$ → Not easier to find bound on $x_1$

Bound on $x \Rightarrow$ Bound on $w$

**Forward bound propagation** → tighter bound on
$$x_2^2=w_3, \quad x_1x_3=w_4, \quad x_3^2=w_5$$
$$\boxed{w_1+5w_2+12w_3-5w_4+7w_5\leq20}$$

also back propagation
$$w_2\in[-5,25], \quad w_3\in[0,25], \quad w_4\in[-5,25], \quad w_5\in[0,25]$$

Take col at one side and other, another side → get maximum value of $w_1$
$$w_1\leq20-w_1-5w_2-12w_3+5w_4-7w_5$$

Forward → Reverse, do this multiple times.
- adding constraint → problematic for model
