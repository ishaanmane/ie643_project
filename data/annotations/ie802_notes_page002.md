17/02, 2nd page  (50 hrs → 1 sec)

- Linearization makes calculation very fast

$$\min (x_1+x_2-x_3+4x_4)^2 \to \text{Not separable}$$
$$\min (x_1-2x_2+x_3)^2+(x_4+x_5-x_7)^2+x_6^2$$

$$** \min f_1(x_1,x_2,x_3)+f_2(\cdots)+f_3(\cdots)+f_4(x_{10},x_{11},x_{12})$$
$$\text{st } g_i(x,y)\leq0$$

$$\min w_1+w_2+w_3+w_4$$
$$f_1\leq w_1, \quad f_4\leq w_4, \quad g_i(x,y)\leq0$$

Non-linear $b \; \& \; b$; Linearization not suitable fast, non-linear

[Diagram: A square inscribed in a circle, corners labeled $(0,1)$, $(1,1)$, $(1,0)$, $(0,0)$, center $(1/2,1/2)$ — a sphere in which there are no integer points, made square as relaxation.]

Quesada and Grossman are slow in solving this, King separability is fast; complexity → non-separable is separable expl(oit)?

**Automatic Reformation** (solvers use this)

$$* \min e^{x_1+x_2}+5e^{x_3}+7e^{x_4+x_5}-\log(x_2+x_4)$$

(Only 2 separations we can make) : variable in one separation should not be in another separation.

**Perspective Reformation:**

[Diagram: a circle containing a smaller shaded triangle/wedge shape.]

→ shrinking the region from known feasible points to make it more tighter and faster
