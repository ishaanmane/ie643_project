# Sigmoid Functions for Modeling Class Probabilities

Linear Separability in terms of Probability:
$$P(y=1/x) = 1 \quad \text{if } w^Tx \geq 0$$
$$= 0 \quad \text{otherwise}$$

Can we somehow relax this assumption? Can we model probabilities differently?

---

Start with a simple linear model.
$$z = w^Tx \leftarrow \text{feature } x \in \mathbb{R}^d$$

[Diagram: A 2D plot showing a line through the origin (normal vector $w$) with several points $x_1, x_2, x_3, x_4$ marked on either side, labeled $\{x:w^Tx=-15\}$, $\{x:w^Tx=-5\}$, $\{x:w^Tx=0\}$, $\{x:w^Tx=1\}$, $\{x:w^Tx=100\}$, illustrating the decision boundary.]

How to label $\{x_1,x_2,x_3,x_4\}$?
We are going to attach probability for the label to be +1 or -1 to each point.

How to decide the probability? By high or low the "score" of each point is.
The score will be $z=w^Tx$, $z \in [-\infty,\infty]$

- Larger the score ($z=w^Tx$) more the probability of +1