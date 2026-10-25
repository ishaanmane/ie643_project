**Ex:** $6y_1+9y_2\leq14$, $y_1,y_2\in\mathbb{Z}$

→ divide by 3: $2y_1+3y_2\leq5.6667$
→ Now scale: $2y_1+3y_2\leq5$
→ $\boxed{6y_1+9y_2\leq15}$ ← Round on method..

**Chvátal and Gomory**

① $y_1+3.2y_2-2.3y_3+6y_4=12.4$
$$y\geq0$$
$$y\in\mathbb{Z}^4$$

$$\hat{y}=\begin{bmatrix}12.4\\0\\0\\0\end{bmatrix}$$

→ do roundoff and apply above rule.. find cutting plane

**Mixed Integer Rounding**

original constraint:
1. $x_1+y_1\leq b$
2. $x_1\geq0$
3. $y_1\in\mathbb{Z}$

$b\to$ fractional

[Diagram: A plot of $y_1$ vs $x_1$, showing a family of parallel red lines at $y_1$-intercepts $(0,\lfloor b\rfloor+1)$, $(0,b)$, $(b-\lfloor b\rfloor,\lfloor b\rfloor)$, and the constraint line $x_1+y_1\leq b$ crossing them, with a "cutting plane" labeled and "equation of cutting plane" pointing to it.]

$$\frac{x_1}{f}+y_1\geq\lceil b\rceil$$

Fractional part of $b = (b-\lfloor b\rfloor)$

After cutting + no need to cut...
