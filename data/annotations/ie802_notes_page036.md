We introduce this and use graphs to analyse their properties.

Given relaxation, how bad is relaxation?

if we take conic relaxation of $S$, how bad is that set.

$$x^TQy+a^Tx+b^Ty+c\leq0$$
$$0\leq x\leq1$$
$$0\leq y\leq1$$

[Diagram: An irregular blob labeled $S$ enclosed by a tighter red outline $R_1$ and a looser black outline $R_2$.]

**How to Quantify**

① Find maximum of a point in $R$ — for this we need to know $S$

② Take minimum function over $R, \in S$
- try different linear function and differentiate b/w optimizing over $R_1$ and $S$
- find optimal value of $R$ and $S$
- if very diff answers then they are far off
- if small result, then they are near.

③ We look at function rather than set

Non-convex function of $(x)$: find under-estimator of $f(x)$ over ... of $f(x)$ → need not tightly

[Diagram: An irregular blob with a red oval circumscribing zigzag curves labeled "gap", "over", "under", "weak over estim..."]

→ measure gap. max gap → it is weak

# analyse gap of simple mccormick eqn → gap is constant for this
