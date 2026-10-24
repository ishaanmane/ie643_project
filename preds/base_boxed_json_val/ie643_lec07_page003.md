```markdown
# Supervised Learning

## Data Representation
- **Data Set**: \( D = \{(x_i, y_i)\}_{i=1}^N \)
  - \( x_i \in \mathbb{R}^q \)
  - \( y_i \in \{-1, +1\} \)

## Function Mapping
- \( h: X \rightarrow Y \)
- MLP weights

## Training a Multilayered Perceptron
- **Objective**: Find \( h_{MLP} \) that minimizes the error function.
- **Error Function**: 
  $$ E = \sum_{i=1}^{N} e(y_i, \hat{y}_i) $$

## Optimization
- Minimization over weights of MLP.

## Complexity
- **NP-hard** problem.

## Local Minimum
- Local minimum in the optimization landscape.
```