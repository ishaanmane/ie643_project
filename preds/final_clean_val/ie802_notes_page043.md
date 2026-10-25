$$\min c^Tx+d^T\theta$$
$$\text{st } g_i(x,\theta)\leq0 \quad i=1,2\dots m$$
$$x\in\mathbb{R}^n, \quad \theta\in\mathbb{Z}^p$$

$$S = \{(x,\theta): x\in\mathbb{R}^n, \theta\in\mathbb{Z}^p, g_i(x,\theta)\leq0, i=1,2\dots m\}$$

$$R = \{(x,y): x\in\mathbb{R}^n, y\in\mathbb{R}^p, g_i(x,y)\leq0, i=1,2\dots m\}$$

Find $(x,\theta)$ st it is valid for $S$ but not $R$

**Step ①** *Pick a disjunction (OR)*

- $y_1\leq0$ or $y_1\geq1$
- $y_5\leq4$ or $y_5\geq5$
- $y_5+y_6+y_3\leq1$ or $y_5+y_6+y_4\geq2$

**②**
$$S_1 = \{(x,y): x\in\mathbb{R}^n, y\in\mathbb{Z}^p, g_i(x,y)\leq0, i=1,2\dots m, y_1\leq1\}$$
$$S_2 = \{\dots, y_1\geq2\}$$
$$S = S_1\cup S_2$$

**Step③** Relax $\rightarrow R_1$ and $R_2$
$$R_1 = \{(x,y): x\in\mathbb{R}^n, y\in\mathbb{R}^p, \dots, y_1\leq1\}$$
$$R_2 = \{y\in\mathbb{R}^p, y_1\geq2\}$$