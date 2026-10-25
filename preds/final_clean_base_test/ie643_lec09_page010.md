```markdown
# Entropy and KL Divergence

## Entropy Definition
The entropy of a probability distribution \( p \) is defined as:

\[
\text{Entropy}(p) := -\sum_{j} p_j \log p_j
\]

## Cross-Entropy
Cross-entropy measures the difference between two probability distributions.

## KL Divergence
The Kullback-Leibler (KL) divergence between two distributions \( p \) and \( q \) is given by:

\[
D(p \| q) = \sum_{j} p_j \log \left( \frac{p_j}{q_j} \right)
\]

## Data Representation
Let \( D \) be a dataset consisting of pairs \( (x_i, y_i) \):

\[
D = \{(x_i, y_i)\}_{i=1}^N
\]

where:
- \( x_i \in \mathbb{R}^n \)
- \( y_i \in \mathbb{R}^m \)

## Predicted Outputs
For each data point \( i \), the predicted output \( \hat{y}_i \) is represented as:

\[
\hat{y}_i = \begin{bmatrix}
\hat{y}_{i1} \\
\hat{y}_{i2} \\
\vdots \\
\hat{y}_{im}
\end{bmatrix}
\]
```