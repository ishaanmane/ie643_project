Mathematical

$$\min c^Tx+d^Ty$$
$$\text{st } g_i(x,y)\leq0, \; i=1,2\dots m$$
$$x\in\mathbb{R}^n$$
$$y\in\mathbb{Z}^p$$

$$S=\left\{(x,y): x\in\mathbb{R}^n, y\in\mathbb{Z}^p, \; g_i(x,y)\leq0, \; i=1,2\dots m\right\}$$
$$R=\left\{(x,y): x\in\mathbb{R}^n, y\in\mathbb{R}^p, \; g_i(x,y)\leq0, \; i=1,2\dots m\right\}$$

Find $(\alpha,\beta)$ st it is valid for $S$ but not $R$

**Step ①**
* Pick a disjunction (OR)
eg. $\boxed{y_1\leq0 \text{ or } y_1\geq1}$ → pick this
eg. $y_5\leq4$ or $y_5\geq5$
eg. $y_5+y_6+y_7\leq1$ or $y_5+y_6+y_7\geq2$

②
$$S_1=\left\{(x,y): x\in\mathbb{R}^n, y\in\mathbb{Z}^p, \; g_i(x,y)\leq0, \; i=1,2\dots m, \; y_1\leq1\right\}$$
$$S_2=\left\{\dots, \; y_1\geq2\right\}$$
$$S=S_1\cup S_2$$

**Step ③**
Relax → $R_1$ and $R_2$
$$R_1=\{\dots, x\in\mathbb{R}^n, y\in\mathbb{R}^p, \dots, y_1\leq1\}$$
$$R_2=\{\dots, y\in\mathbb{R}^p, \dots, y_1\geq2\}$$
