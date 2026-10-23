# Cross-validation for minimizing MSE

$$\text{trace}\left[(XX^T)^{-1}\right] \quad \text{[sum of diagonal entries] also [sum of eigenvalues of matrix]}$$

Let the eigenvalues of $XX^T$ be $\{\lambda_1,\dots,\lambda_d\}$
$\therefore$ Eigenvalues of $(XX^T)^{-1}$: $\left\{\frac{1}{\lambda_1},\dots,\frac{1}{\lambda_d}\right\}$

Mean Squared Error$(\hat{w}_{ML}) = E\left[\|\hat{w}_{ML}-\hat{w}\|^2\right] = \sigma^2\sum_{i=1}^{d}\frac{1}{\lambda_i}$

---

For some matrix $A$, let eigenvalues be $\{\lambda_1,\dots,\lambda_d\}$

Then what are the eigenvalues of $(A+\lambda I)$? $=\{(\lambda_1+\lambda),\dots,(\lambda_d+\lambda)\}$
↳ $\lambda \in \mathbb{R}_{+ve}$, $I \in \mathbb{R}^{d\times d}$

$$\text{trace}\left((XX^T+\lambda I)^{-1}\right) = \left(\sum_{i=1}^{d}\frac{1}{\lambda_i+\lambda}\right)$$

---

We want to decrease MSE by reducing the value of trace. How do we find this $\lambda \in \mathbb{R}_+$?

By the method of **cross validation**

training set | validation set
