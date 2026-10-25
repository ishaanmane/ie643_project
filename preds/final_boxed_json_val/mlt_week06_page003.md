**training set** | **validation set**
80% | 20%

- Train on training set & check for errors on validation set
- Pick $\lambda$ which gives least error

How to decide the best way to divide the data?

## k-fold cross validation

$f_1 \; f_2 \; \cdots \; \cdots \; \cdots \; f_k$

- Train on folds $= \{f_1,\dots f_{i-1},f_{i+1},\dots f_n\}$
- Validate on $f_i$
- Pick $\lambda$ which gives least avg error

$$\hat{w}_{new} = (XX^T + \lambda I)^{-1}Xy$$