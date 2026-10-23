[Diagram: A binary branching tree — root node $x_1\leq5 \;|\; x_1\geq5$ splitting into two children, each further split at $x_1\leq2.5$ / $x_1\geq2.5$ — "Same branch & bound techniques & LP rules".]

That's all for 5 round LPs. Add variables if difficulty.

$$\text{min } e^{-x_1^2+x_2}$$
$$\text{st } x_1+2x_2=1$$
$$-10\leq x\leq10$$

**Transform** $\Rightarrow$ (non-convex constraint) $w_1=x_1^2$, $w_2=x_2-w_1$, $w_3=e^{w_2}$

due to minimization both will become same, $w_3\geq e^{w_2}$ — convex constraint

$$\boxed{e^{-x_1^2+x_2} \text{ is not completely convex, but looks like normal dist.}}$$

[Diagram: An exponential curve $w_3=e^{w_2}$ rising from flat near 0 to steep, over axis $w_2$.]

We don't have bounds, we need to have bounds on $w_2, w_3$

$$x_1\in[-10,10], \quad w_1\in[0,100], \quad w_2\in[-110,10], \quad w_3\in[e^{-110},e^{10}]$$

We need to add variables to make linear, so we set find bounds & easy.

[Diagram: A small tree: $e^{w_3}$ ← $-w_2$ ← $x_2 - x_1^{()2}$, with leaves $x_1, x_2$.]

There is relation b/w Computational graph & Constraints.

We store nonlinear equations in computational graphs, for linear equations we use linear functions.
