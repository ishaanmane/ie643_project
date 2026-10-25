```markdown
# KL Divergence

## Definition

The Kullback-Leibler divergence (KL divergence) measures the difference between two probability distributions \( p \) and \( q \).

### KL Divergence Formulas

#### KL(p → q)
\[ KL(p \rightarrow q) = \sum_{j=1}^{n} p_j \log \frac{p_j}{q_j} \]

#### KL(q → p)
\[ KL(q \rightarrow p) = \sum_{j=1}^{n} q_j \log \frac{q_j}{p_j} \]

### Properties

- **Symmetry**: \( KL(p \rightarrow q) \neq KL(q \rightarrow p) \)
- **Non-negativity**: \( KL(p \rightarrow q) \geq 0 \)
- **Zero KL**: \( KL(p \rightarrow q) = 0 \) if and only if \( p = q \)

### Interpretation

- **Negative Entropy**: The KL divergence can be interpreted as the negative entropy of the distribution \( q \) when viewed through the eyes of the distribution \( p \).

### Example

Consider two distributions:
- \( p = [0.5, 0.5] \)
- \( q = [0.2, 0.8] \)

Calculate \( KL(p \rightarrow q) \):

\[ KL(p \rightarrow q) = 0.5 \log \frac{0.5}{0.2} + 0.5 \log \frac{0.5}{0.8} \]

\[ = 0.5 \log 2.5 + 0.5 \log 0.625 \]

\[ = 0.5 \times (-0.3219) + 0.5 \times (-0.5229) \]

\[ = -0.16095 - 0.26145 \]

\[ = -0.4224 \]

Thus, the KL divergence \( KL(p \rightarrow q) \approx 0.4224 \).
```