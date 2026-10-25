```markdown
# Clustering Example

## Given Data
$\{X_1, X_2, X_3, X_4, X_5\}$

## Clusters
- $Z_1 = 1$
- $Z_2 = 2$
- $Z_3 = 1$
- $Z_4 = 1$
- $Z_5 = 2$

## Partitioning
- 5 points assigned to 2 clusters.
- $X_1, X_3, X_4 \rightarrow 1st$
- $X_2, X_5 \rightarrow 2nd$

## Centroids Calculation
- $\mu_1 = \frac{X_1 + X_3 + X_4}{3}$
- $\mu_2 = \frac{X_2 + X_5}{2}$

## Goodness of Partition
- $F(Z_1, \ldots, Z_n)$
- $(X_1 - \mu_1)^2 + (X_2 - \mu_2)^2 + (X_3 - \mu_1)^2 + (X_4 - \mu_1)^2 + (X_5 - \mu_2)^2$

## Goal
- Minimize $\sum_{i=1}^{n} \|x_i - \mu_{z_i}\|^2$

## Observations
- This will be difficult due to too many calculations ($n^k$).
```