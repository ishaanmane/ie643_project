## Sigmoid Functions for Modeling Class Probabilities

**Linear Separability in terms of Probability:**
$$\text{P}(y=1/x) = 1 \quad \text{if } w^Tx \geq 0$$
$$= 0 \quad \text{otherwise}$$

Can we somehow relax this assumption? Can we model probabilities differently?

---

**Start with a simple linear model:**
$$z = w^Tx \leftarrow \text{feature } x \in \mathbb{R}^d$$

[Diagram: A 2D plane showing decision boundaries $w^Tx = -150$, $w^Tx = -50$, $w^Tx = 0$, $w^Tx = 1$, $w^Tx = 100$. Points $x_1, x_2, x_3, x_4$ are plotted near these lines.]

How to label $\{x_1, x_2, x_3, x_4\}$?

We are going to attach probability for the label to be +1 or -1 to each point.

How to decide the probability? By high or low the "score" of each point is.

The score will be $z = w^Tx$, $z \in [-\infty, \infty]$

- Less/greater the score ($z = w^Tx$) more the probability of +1