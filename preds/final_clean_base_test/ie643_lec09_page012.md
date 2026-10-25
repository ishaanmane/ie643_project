```markdown
# KL Divergence

The Kullback-Leibler (KL) divergence between two probability distributions \( P \) and \( Q \) is defined as:

$$
\text{KL}(P || Q) = \sum_{i} P_i \log \frac{P_i}{Q_i}
$$

This can be interpreted as the expected value of the logarithmic difference between the probabilities under \( P \) and \( Q \).

## Minimizing KL Divergence

To minimize the KL divergence, we can rewrite it in terms of weights:

$$
\min_{\text{weights}} \sum_{i=1}^{N} (-\sum_{j=1}^{M} y_j \log \hat{y}_j)
$$

Here, \( y_j \) represents the actual values, and \( \hat{y}_j \) represents the predicted values.

## Simplifying the Expression

We can further simplify the expression by separating the terms:

$$
\min \left( \sum_{j} \hat{y}_j \log \hat{y}_j - \sum_{j} \hat{y}_j \log y_j \right)
$$

This form highlights the difference between the log probabilities of the predicted and actual values.
```