```markdown
# KL Divergence

## Definition and Properties

### KL Divergence (p → q)
The KL divergence from distribution p to distribution q is defined as:

$$
KL(p \rightarrow q) = \sum_{j=1}^{n} p_j \log \frac{p_j}{q_j}
$$

### KL Divergence (q → p)
The KL divergence from distribution q to distribution p is defined as:

$$
KL(q \rightarrow p) = \sum_{j=1}^{n} q_j \log \frac{q_j}{p_j}
$$

### Symmetry of KL Divergence
It's important to note that the KL divergence is not symmetric. This means:

$$
KL(p \rightarrow q) \neq KL(q \rightarrow p)
$$

### Relationship Between KL Divergences
Interestingly, there exists a relationship between these two divergences:

$$
KL(p \rightarrow q) + KL(q \rightarrow p) = KL(p \rightarrow p) + KL(q \rightarrow q)
$$

### Interpretation
- **KL(p → q)** represents the amount of information lost when using distribution q to approximate distribution p.
- **KL(q → p)** represents the amount of information lost when using distribution p to approximate distribution q.

### Minimum KL Divergence
When distributions p and q are identical (i.e., p = q):

$$
KL(p \rightarrow p) = 0
$$

Thus,

$$
KL(p \rightarrow q) + KL(q \rightarrow p) = 0
$$

This implies that the total information loss is zero when distributions are the same.

## Negative Entropy

### Definition
Negative entropy can be expressed as:

$$
-\sum_{j=1}^{n} p_j \log p_j
$$

### Interpretation
This term represents the uncertainty or randomness inherent in the distribution p. It quantifies how much information is contained within p.

### Conclusion
Understanding KL divergence helps in assessing the difference between two probability distributions and provides insights into the information content and uncertainty associated with each distribution.
```