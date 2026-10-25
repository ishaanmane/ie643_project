```markdown
# Handwritten Lecture Note Page

## KL Divergence Between Two Probability Distributions

### Definition and Formula

The Kullback-Leibler (KL) divergence between two probability distributions \( p \) and \( q \) is defined as:

\[
\text{KL}(p \parallel q) = \sum_{j=1}^{C} p_j \log \frac{p_j}{q_j}
\]

This can be rewritten as an expectation over the true distribution \( p \):

\[
\text{KL}(p \parallel q) = E_p \left[ \log \frac{p}{q} \right]
\]

### Explanation

- **KL divergence** measures how one probability distribution diverges from a second, expected probability distribution.
- It is also known as **Bregman divergence** or **Jensen-Shannon divergence**.

### Example

Consider a discrete probability distribution \( q \):

\[
\hat{y} = \begin{pmatrix}
q_1 \\
q_2 \\
\vdots \\
q_C
\end{pmatrix}, \quad q_j \geq 0, \quad \sum_{j=1}^C q_j = 1
\]

This represents a probability vector where each component \( q_j \) is non-negative and their sum equals 1.
```