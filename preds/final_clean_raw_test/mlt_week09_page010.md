# Sigmoid Functions for Modeling Class Probabilities

Linear Separability in terms of Probability:
$$P(y=1/x) = 1 \quad \text{if } w^Tx \geq 0$$
$$= 0 \quad \text{otherwise}$$

Can we somehow relax this assumption? Can we model probabilities differently?

---

Start with a simple linear model.
$$z = w^Tx \leftarrow \text{feature } x \in \mathbb{R}^d$$

[Diagram: A 2D plot showing several blue lines (decision boundaries) through the origin, each labeled $\{x:w^Tx=c\}$ for various constants $c$. Points $x_1, x_2, x_3, x_4$ are marked near the axes.]

How to label $\{x_1,x_2,x_3,x_4\}$?
We are going to attach probability for the label to be +1 or -1 to each point.

How to decide the probability? By high or low the "score" of each point is.
The score will be $z=w^Tx$, $z \in [-\infty,\infty]$

- Larger the score ($z=w^Tx$) more the probability of +1