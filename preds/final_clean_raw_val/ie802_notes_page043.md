$$\min c^Tx + 2\beta y \quad \text{st } g_i(x,y) \leq 0 \quad i=1,2,\dots m$$

$$x \in \mathbb{R}^n, \quad y \in \mathbb{Z}^p$$

$$S = \{(x,y): x \in \mathbb{R}^n, y \in \mathbb{Z}^p, g_i(x,y) \leq 0, i=1,2,\dots m\}$$

$$R = \{(x,y): x \in \mathbb{R}^n, y \in \mathbb{R}^p, g_i(x,y) \leq 0, i=1,2,\dots m\}$$

Find $(x,y)$ st it is valid for $S$ but not $R$

**Step①** Pick a disjunction ($\lor R$)

eg. $y_1 \leq 0 \; \text{or} \; y_1 \geq 1$
eg. $y_5 \leq 4 \; \text{or} \; y_5 \geq 5$
eg. $y_5+y_6+y_9 \leq 1 \; \text{or} \; y_5+y_6+y_4 \geq 2$

**②** $S_1 = \{(x,y): x \in \mathbb{R}^n, y \in \mathbb{Z}^p, g_i(x,y) \leq 0, i=1,2,\dots m, y_1 \leq 1\}$

$$S_2 = \{\dots, y_1 \geq 2, \dots\}$$

$$S = S_1 \cup S_2$$

**Step②** Relax $\rightarrow R_1$ and $R_2$

$$R_1 = \{ \dots x \in \mathbb{R}^n, y \in \mathbb{R}^p, \dots y_1 \leq 1 \}$$
$$R_2 = \{ \dots y \in \mathbb{R}^p, y_1 \geq 2 \}$$