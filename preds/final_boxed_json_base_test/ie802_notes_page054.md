```markdown
# Convex MINLO Case (Pure Binary)

$\min c^T x + d^T y$

$\text{subject to:}$

$(Ax + By) \leq 0$

$x \in \mathbb{R}^n$

$y \in \{0,1\}^p$

$\rightarrow$ continuous

## Solve NLP Relaxation

1. Get $\bar{x}, \bar{y} \rightarrow round(\bar{x})$

2. $\min \sum_{i=1}^{p} |y_i - round(\bar{y}_i)|$

$\text{subject to:}$

$(Ax + By) \leq 0$

$0 \leq y \leq 1$

$\Rightarrow$

$\min \sum |y_i - round(y_i)|$

$\text{subject to:}$

$\nabla$ inequalities at $(\bar{x}, \bar{y})$

$0 \leq y \leq 1$

## You can also solve MILP relaxation

### Non-convex MINLO Case (Pure Binary)

$\rightarrow$ Leave it...

# RINS Heuristic (Relaxed-Induced Neighborhood Search) → Improvement

## Convex MINLO

Let $(\bar{x}, \bar{y})$ be known solution of MINLO.

1. Solve NLP relaxation of that node

$\rightarrow (\bar{x}, \bar{y})$

$\bar{y} \notin \mathbb{Z}^p$

$\rightarrow$ If majority of equal, randomly fix

$(\bar{y}_i = \bar{y}_j)$

2. Compare $\bar{x}$ and $\bar{y} \rightarrow$ all these same $\rightarrow$ fix it

3. Solve the smallest MINLO

$\rightarrow$ Don't solve fully but time limits e.g., 5 sec. and some other parameters.
```