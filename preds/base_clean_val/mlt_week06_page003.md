```markdown
# Training and Validation Set

## Splitting Data

- **Training Set:** 80%
- **Validation Set:** 20%

### Steps:
1. Train on the training set.
2. Check for errors on the validation set.
3. Pick λ which gives the least error.

## Choosing the Best Way to Divide the Data

### K-fold Cross Validation

[Diagram: K-fold cross-validation]

- **Folds:** F₁, F₂, ..., Fₖ
- **Training on folds:** {F₁, ..., Fᵢ₋₁, Fᵢ₊₁, ..., Fₖ}
- **Validate on:** Fᵢ
- **Pick λ which gives the least average error**

## Regularization Parameter Selection

$$
\hat{w}_{new} = (X X^T + \lambda I)^{-1} X Y
$$

```
```