$\lceil a_2\rceil+f_2$, $\lceil a_3\rceil+f_3$

$a_2y_2+a_3y_3\leq b+x_1$
$$y\geq0$$
$$x\geq0$$
$$y\in\mathbb{Z}^2$$

→ MIR (Mixed Integer Rounding) cut

① $\lceil a_2\rceil y_2+\left(\lceil a_3\rceil+\dfrac{f_3-f_0}{1-f_0}\right)y_3 \leq \lfloor b\rfloor+\dfrac{x_1}{1-f_0}$ &nbsp; ($b-\lfloor b\rfloor$)

$$f_2=a_2-\lceil a_2\rceil$$
$$f_3=a_3-\lceil a_3\rceil$$

② $\left(\lceil a_2\rceil+\dfrac{f_2-f_0}{1-f_0}\right)y_2+\lceil a_3\rceil y_3 \leq \lfloor b\rfloor+\dfrac{x_1}{1-f_0}$

also you can combine, and take maximum.

**Generalization**

$$y_1+\sum_{i=2}^{p}a_iy_i+\sum_{i=1}^{n}a_ix_i=b$$
$$y\geq0$$
$$y\in\mathbb{Z}^p$$
$$x\in\mathbb{R}^n$$

→ apply MIR cut and get Gomory mixed integer inequality.

**Prop: (MIR, GG)**
- cheap cuts
- Guaranteed to cut off fractional corner points
- weak → convergence slow
