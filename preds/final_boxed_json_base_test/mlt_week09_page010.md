```markdown
# Sigmoid Functions for Modeling Class Probabilities

## Linear Separability in Terms of Probability:

$$
P(y=1|x) = 
\begin{cases} 
1 & \text{if } w^Tx \geq 0 \\
0 & \text{otherwise}
\end{cases}
$$

## Can we somehow relax this assumption? Can we model probabilities differently?

### Start with a simple linear model.

$$
z = w^Tx \quad \text{feature } x \in \mathbb{R}^d
$$

[Diagram: A diagram showing different regions defined by the linear function \( z = w^Tx \). The regions are labeled as follows:
- \( x_1 \): \( w^Tx = 1 \)
- \( x_2 \): \( w^Tx = 0 \)
- \( x_3 \): \( w^Tx = -1 \)
- \( x_4 \): \( w^Tx = -100 \)]

## How to label \( \{x_1, x_2, x_3, x_4\} \)?

We are going to attach probability for the label to be +1 or -1 to each point.

How to decide the probability? By how high or low the "score" of each point is.

The score will be \( z = w^Tx \), \( z \in [-\infty, \infty] \).

- Larger the score (\( z = w^Tx \)) more the probability of +1
```