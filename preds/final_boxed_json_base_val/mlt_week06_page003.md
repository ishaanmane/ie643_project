```markdown
# Training Set and Validation Set

## Training Set and Validation Set
- Train on training set & check for errors on validation set
- Pick λ which gives least error

## How to decide the best way to divide the data?

### K-fold Cross Validation

#### Diagram: K-fold cross validation
| F₁ | F₂ | ... | ... | Fₖ |

## Training and Validation Process

- Train on folds = {F₁, ..., Fᵢ₋₁, Fᵢ₊₁, ..., Fₙ}
- Validate on Fᵢ
- Pick λ which gives least avg error

## Update Weights

$$
\hat{w}_{new} = (X X^T + \lambda I)^{-1} X Y
$$
```