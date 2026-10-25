```markdown
# Logistic Regression

## Key Concepts

### Kullback-Leibler Divergence (KL)
- **Definition**: KL divergence measures the difference between two probability distributions \( P \) and \( Q \).
- **Properties**:
  - \( KL(P||Q) = 0 \) when \( P = Q \)
  - \( KL(P||Q) > 0 \) when \( P \neq Q \)

### Cross-Entropy (CE)
- **Definition**: Measures the difference between two probability distributions.
- **Minimization**: Minimizing CE is equivalent to minimizing the negative log-likelihood.

### Bernoulli Likelihood
- **Formula**: \( P(y_i = 1 | x_i) = \sigma(\mathbf{w}^T x_i + b) \)
- **Explanation**: The Bernoulli likelihood function is used in logistic regression to model the probability of a binary outcome.

### Objective Function
- **Minimize**: \( \sum_{i=1}^{N} KL(y_i, \hat{y}_i) \)
- **Weights**: Optimize the weights of the neural network to minimize the KL divergence.

### Expected Value
- **Expression**: \( E[y|x=\vec{x}] \)
- **Interpretation**: The expected value of the output given the input vector \( \vec{x} \).

### Diagram: Flowchart
- **Nodes**:
  - KL divergence
  - Cross-entropy minimization
  - Bernoulli likelihood
  - Logistic regression
  - Expected value calculation

### Summary
- The goal of logistic regression is to find the parameters that minimize the KL divergence or cross-entropy between the true distribution and the predicted distribution.
- This minimization process can be interpreted as finding the best fit for the Bernoulli likelihood function.
```