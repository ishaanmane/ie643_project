## Training Set & Validation Set

- Train on training set & check for errors on validation set
- Pick $\lambda$ which gives least error

How to decide the best way to divide the data?

**K-fold cross validation**

[Diagram: A row of boxes labeled $F_1, F_2, \dots, F_k$, with a dashed line splitting them into two groups.]

- Train on folds $= \{f_1, \dots f_{i-1}, f_{i+1}, \dots f_n\}$
- Validate on $f_i$
- Pick $\lambda$ which gives least avg error

---

$$\hat{w}_{new} = (XX^T + \lambda I)^{-1}Xy$$