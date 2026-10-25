```markdown
# KL Divergence

The equation for KL divergence between two probability distributions \( \hat{y} \) and \( y \) is given by:

$$
\text{KL}( \hat{y} || y ) = \sum_{j=1}^{N} \frac{\hat{y}_j}{y_j} \log \frac{\hat{y}_j}{y_j}
$$

This can be broken down into two parts:

1. **First Part**:
   - Minimize the sum of the weighted logarithms of the ratios of the probabilities.

2. **Second Part**:
   - Minimize the difference between the sum of the logarithms of the predicted probabilities and the sum of the logarithms of the actual probabilities.

### Diagram: 
- The first part is represented as:
  $$
  \min \sum_{i=1}^{N} (-\sum_{j=1}^{N} y_i \log \hat{y}_i)
  $$
- The second part is represented as:
  $$
  \min \sum_{j=1}^{N} \hat{y}_j \log \hat{y}_j - \sum_{j=1}^{N} y_j \log y_j
  $$

```