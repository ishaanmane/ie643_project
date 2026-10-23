| training set (80%) | validation set (20%) |
|---|---|

- Train on training set & check for errors on validation set
- Pick $\lambda$ which gives least error

How to decide the best way to divide the data?

**K-fold cross validation**

$$[F_1 | F_2 | \cdots | F_K]$$

- Train on folds $= \{f_1,\dots f_{i-1},f_{i+1},\dots,f_k\}$
- Validate on $f_i$
- Pick $\lambda$ which gives least avg error

---

$$\boxed{\hat{w}_{new} = (XX^T+\lambda I)^{-1}Xy}$$
