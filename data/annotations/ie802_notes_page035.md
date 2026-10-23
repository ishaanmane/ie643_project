A constraint of the form $x^TQy$ is called a **pure bilinear term form**. There are no terms $x_ix_j$, $y_ky_\ell$.

**Example:**
(1) $x_1x_2+x_3x_4+x_5x_6+x_7x_8\geq10$ ✓
(2) $x_1x_2+x_3x_4+x_2x_3\geq10$ ✓
(3) $x_1x_2+x_2x_3+x_1x_3\geq10$ ✗

every term in edge, can we divide the graph?

[Diagram: A 4-node graph (①) with edges $m_1\to m_2$, $m_3\to m_4$, $m_2\to m_3$ (or similar). Create nodes for variables, for terms; separate nodes into 2 so nodes pass from one side to another.]

② $m_1-m_2-m_3$, $x_4$ branch — finding these are easy than quadratic terms.

③ Triangle graph $m_1\to m_2$, $m_2\to m_3$, $m_3\to m_1$ — this is not to be there, so not this type.

Let $S=\{(x,y): x^TQy+a^Tx+b^Ty+c\leq0, \; 0\leq x\leq1, \; 0\leq y\leq1\}$

Result: Conv($S$) can be written as a **second order cone**

closed form of SOC? → explore in paper

Let $S=\{(x,y): x^TQ_1y+a_1^Tx+b_1^Ty+c_1\leq0$, $\vdots$, $x^TQ_ky+a_k^Tx+b_k^Ty+c_k\leq0$, $0\leq x\leq1$, $0\leq y\leq1\}$

Convex hull → Conv($S$) is SOC representable.
