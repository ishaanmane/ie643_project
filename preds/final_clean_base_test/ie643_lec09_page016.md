```markdown
# Neural Network Diagram

## Input Layer
- $a_1$
- $a_2$
- ...
- $a_c$

## Hidden Layer
- $y_1$
- $y_2$
- ...
- $y_c$

## Output Layer
- $\hat{y}_k$

## Loss Function
$$
\ell = - \sum_{j=1}^{c} y_j \log \hat{y}_j
$$

## Partial Derivative of Loss with Respect to Weights
$$
\frac{\partial \ell}{\partial a_j} = \sum_{k=1}^{c} \frac{\partial \ell}{\partial \hat{y}_k} \cdot \frac{\partial \hat{y}_k}{\partial a_j}
$$

## Simplified Expression
$$
= \sum_{k=1}^{c} - \frac{y_k}{\hat{y}_k} \cdot \frac{\partial \hat{y}_k}{\partial a_j}
$$

## Diagram: Neural Network Structure
```
```