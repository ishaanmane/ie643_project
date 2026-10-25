```markdown
# Entropy and Cross-Entropy

## Entropy

The entropy \( H(p) \) of a probability distribution \( p \) is defined as:

\[
H(p) := -\sum_{j} p_j \log p_j
\]

## Probability Distribution

A probability distribution can be represented as:

\[
p_1, p_2, \ldots, p_c
\]

## Kullback-Leibler Divergence

The Kullback-Leibler divergence between two distributions \( P \) and \( Q \) is given by:

\[
KL(P \| Q) = \sum_i P(i) \log \frac{P(i)}{Q(i)}
\]

## Cross-Entropy

Cross-entropy measures the difference between two probability distributions.

## Data Representation

The data set \( D \) is represented as:

\[
D = \{(x_i, y_i)\}_{i=1}^N
\]
where:
\[
y_i = \begin{bmatrix}
y_{i1} \\
y_{i2} \\
\vdots \\
y_{ic}
\end{bmatrix} \in \mathbb{R}^c
\]

## Predicted Outputs

The predicted outputs \( \hat{y}_i \) are represented as:

\[
\hat{y}_i = \begin{bmatrix}
\hat{y}_{i1} \\
\hat{y}_{i2} \\
\vdots \\
\hat{y}_{ic}
\end{bmatrix}
\]
```