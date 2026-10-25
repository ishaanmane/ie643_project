```markdown
# Sigmoid Functions for Modeling Class Probabilities

## Linear Separability in Terms of Probability

The probability of class 1 given feature vector \( x \) is defined as:

$$
P(y=1|x) = 
\begin{cases} 
1 & \text{if } w^Tx \geq 0 \\
0 & \text{otherwise}
\end{cases}
$$

Can we somehow relax this assumption? Can we model probabilities differently?

---

## Start with a Simple Linear Model

Let's begin with a linear model where the output \( z \) is calculated as follows:

$$
z = w^Tx \quad \text{where} \quad x \in \mathbb{R}^d
$$

[Diagram: A diagram showing four regions separated by lines representing different values of \( w^Tx \). The regions are labeled as follows:
- \( x_1 \): \( w^Tx = -150 \)
- \( x_2 \): \( w^Tx = 100 \)
- \( x_3 \): \( w^Tx = -10 \)
- \( x_4 \): \( w^Tx = 0 \)]

How do we label these points \( \{x_1, x_2, x_3, x_4\} \)?

We are going to attach a probability to each point that corresponds to the label being +1 or -1.

How do we decide the probability? By the "score" of each point.

The score will be \( z = w^Tx \), where \( z \in [-\infty, \infty] \).

- Larger the score (\( z = w^Tx \)) more the probability of +1
```