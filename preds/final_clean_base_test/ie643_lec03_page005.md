```markdown
# Train a Perceptron

## Online Learning

- **Data Set:** $\mathcal{D} = \{(x^t, y^t)\}$ where $t=1, 2, 3, \ldots$
- **Initial Weights:** $\tilde{w}^0 = \overrightarrow{0}$
- **Iteration Counter:** $t=0, 1, 2, 3, \ldots$

### Algorithm Steps:

1. Receive a sample $(x^t, y^t) \in \mathcal{D}$
2. Update the weights:
   - If $\hat{y}^t = y^t$: No update
   - Otherwise: Update rule
     $$\tilde{w}^{t+1} = \tilde{w} + y^t x^t$$

## Update Rule

If $\hat{y}^t == y^t$:
- No update
Else:
- Update rule:
  $$\tilde{w}^{t+1} = \tilde{w} + y^t x^t$$

### Prediction

$$\hat{y}^t = \text{Perceptron}(\tilde{x}^t, \tilde{w}^t)$$
```
