$$\min c^Tx+d^Ty$$
$$\text{st } g_i(x,y)\leq0 \quad i=1,2,\dots m$$

$$x\in\mathbb{R}^n, \quad y\in\mathbb{Z}^p$$

$$S = \{(x,y): x\in\mathbb{R}^n, y\in\mathbb{Z}^p, g_i(x,y)\leq0, i=1,2,\dots m\}$$

$$R = \{(x,y): x\in\mathbb{R}^n, y\in\mathbb{R}^p, g_i(x,y)\leq0, i=1,2,\dots m\}$$

Find $(x,y)$ st it is valid for $S$ but not $R$

**Step ①:** Pick a disjunction ($\lor R$)
- $y_1\leq0$ or $y_1\geq1$
- $y_5\leq4$ or $y_5\geq5$
- $y_5+y_6+y_4\leq1$ or $y_5+y_6+y_4\geq2$

**②** $S_1 = \{(x,y): x\in\mathbb{R}^n, y\in\mathbb{Z}^p, g_i(x,y)\leq0, i=1,2,\dots m, y_1\leq1\}$

$$S_2 = \{\dots, y_1\geq2\}$$

$$S = S_1\cup S_2$$

**Step ③:** Relax $\rightarrow R_1$ and $R_2$
$$R_1 = \{(x,y): x\in\mathbb{R}^n, y\in\mathbb{R}^p, y_1\leq1\}$$
$$R_2 = \{(x,y): y\in\mathbb{R}^p, y_1\geq2\}$$