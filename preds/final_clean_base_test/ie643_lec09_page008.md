```markdown
# Handwritten Lecture Note Page

## KL Divergence

### Definition
The KL divergence between two probability distributions \( p \) and \( q \) is defined as:

$$
\text{KL}(p \parallel q) = \sum_{j=1}^{C} p_j \log \frac{p_j}{q_j}
$$

### Explanation
- **\( p \)**: The true distribution.
- **\( q \)**: The estimated distribution.

### KL Divergence as Expectation
The KL divergence can also be expressed as an expectation:

$$
\text{KL}(p \parallel q) = E_p \log \frac{p}{q}
$$

### Comparison of Two Discrete Probability Distributions
- **KL Divergence**
- **Bregman Divergence**
- **JS Divergence**

### Notations
- \( \hat{y} = \begin{bmatrix} q_1 \\ q_2 \\ \vdots \\ q_C \end{bmatrix} \)
  - \( q_j \geq 0 \)
  - \( \sum q_j = 1 \)

```
```