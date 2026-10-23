**model-1**
$$x_1^2+x_2^2\leq100$$
$$x_1^2+x_2^2-100\leq0$$
$$-10x_1\leq x_1\leq10x_2$$

**Try!**
1. Taking function $g_1(x_1,x_2)=x_1^2+x_2^2-100$
2. Apply perspective formulae: $y_1\left[\left(\frac{x_1}{y_1}\right)^2+\left(\frac{x_2}{y_2}\right)^2-100\right]\leq0$
3. Distribute sq. $y_1\left[\frac{x_1^2}{y_1^2}+\frac{x_2^2}{y_2^2}-100\right]\leq0$
4. Multiply the outer $y_1$ through the terms: $\frac{x_1^2}{y_1}+\frac{x_2^2}{y_1}-100y_1\leq0$

02/03/26

For convex MINLO we don't know the function
$$\min f(x,y)$$
$$g_i(x,y)\leq0, \; i=1,2\dots m$$
$$x\in\mathbb{R}^n, \quad y\in\mathbb{Z}^p$$

$$g_i(\hat{x},\hat{y})+\nabla g_i(\hat{x},\hat{y})\begin{bmatrix}x-\hat{x}\\y-\hat{y}\end{bmatrix}\leq0 \quad \to \text{solve by} \begin{cases}\text{(1) Branch and Bound}\\\text{(2) Convex Relaxation}\\\text{(3) Interval analysis}\end{cases}$$

**Global Optimization of "Factorable Functions"**

Recursive fn using a limited no. of operators: $+,-,\times,\div,\log,\;{}^{\wedge}k,\;k^{()},\sin,\cos,\tan(c)\dots$

Ex: $x_1^{()}*(3x_1^2+\log(5+\sin^2(5x_1x_2+7)))$

Ex- Powerflow problem  **Pooling applications**

Crudeoil: [Diagram: A network flow diagram with source nodes ①(1%), ②(8%, "sulphon"), ③(5%) feeding into intermediate nodes ④, ⑤, which feed into output nodes ⑥, ⑦, with edge flows labeled $q_{14}, q_{24}, q_{34}, q_{46}, q_{56}$ etc.]

$$p_4 = \frac{0.01q_{14}+0.08q_{24}+0.05q_{34}}{q_{14}+q_{24}+q_{34}}, \qquad p_6 = \frac{q_{46}\times p_4+q_{56}\times p_5}{q_{46}+q_{56}}$$

$\{26 < p_6 < 46\}$ — constraint on supply, flow, etc. There is upper and lower bound; more sulphur → more benefit
