```markdown
# Supervised Learning

## Definitions

- **Data Set:** $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^N$
  - $x_i \in \mathbb{R}^d$
  - $y_i \in \{-1, +1\}$

- **Hypothesis Function:** $h: X \rightarrow Y$

## Training a Multi-Layered Perceptron (MLP)

To find the optimal weights of an MLP:

$$
\min_{\text{weights of MLP}} E = \sum_{i=1}^{N} e(y_i, \hat{y}_i)
$$

## Complexity and Optimization

- **NP-hard problem**: Finding the global minimum.
- **Local minimum**: A point where the error function is minimized but not necessarily the global minimum.

[Diagram: Error function with local minimum]

```