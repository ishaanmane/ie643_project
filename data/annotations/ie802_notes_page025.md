**Cuts From the Boolean Quadric Polytope:**

$$\min c^Ty+y^TQy \quad \text{st } y\in\{0,1\}^n$$
$$= c_1y_1+\dots c_ny_n+q_{11}y_1^2+(q_{12}+q_{21})y_1y_2+\dots \quad \text{replace with } w_{12}$$

$$\min c^Ty+q_{11}y_1+q_{22}y_2+\dots+q_{nn}y_n$$
$$+q_{12}\underbrace{y_1y_2}_{w_{12}}+q_{21}\underbrace{y_1y_2}_{w_{12}}+q_{13}\underbrace{y_1y_3}_{w_{13}}+q_{14}\underbrace{y_1y_4}_{w_{14}}+\dots$$

st $w_{12}=y_1y_2$, $w_{13}=y_1y_3$, $w_{i,j}\in\{0,1\}$, $y_i\in\{0,1\}$

[circled note: $w_{12}\geq0$; $w_{12}\leq1$ (not req.); $w_{12}\leq y_1$; $w_{12}\leq y_2$; $w_{12}\geq y_1+y_2-1$ ← corners are $[0,0,0]$, $[1,1,1]$, $[1,0,0]$, $[0,1,1]$, 3 active. When $n=2$: $y_1$ and $y_2$ only.]

$w_{13}\leq y_1$, $w_{13}\leq y_3$, $w_{13}\geq y_1+y_3-1$ — maybe we set some half values like $\frac{1}{2}w_{12}$ or something.

@ $n=3$: $w_{13}\geq0$, $w_{13}\leq y_1$, $w_{13}\leq y_3$, $w_{13}\geq y_1+y_3-1$; $w_{23}\geq0$, $w_{23}\leq y_2$, $w_{23}\leq y_3$, $w_{23}\geq y_2+y_3-1$ (complex...)

Table: $y_1,y_2,y_3,w_{12},w_{13},w_{23}$: rows (0,0,0,0,0,0), (0,0,1,0,0,0), (0,1,0,0,0,0), (0,1,1,0,?,1)...

**Manfred Padberg: Triangle inequalities**
$$* \; y_1+y_2+y_3-w_{12}-w_{13}-w_{23}\leq1$$

① It does not cut off integer feasible points. @ always valid → check logically

② It cuts off some non-integer points from e.g. $y_1=y_2=y_3=1/2 \leftarrow$ allowed... $w_{12}=w_{13}=w_{23}=0 \leq y_2+w_{13}$

$$* \; w_{12}+w_{13}\leq y_1+w_{23}$$
$$y_1=y_2=y_3=1/2 \leq y_3+w_{12}$$
$$w_{13}=w_{12}=1/2, \; w_{23}=0$$

@ don't add an inequalities blindly — solve and use some needed... # don't blindly add
