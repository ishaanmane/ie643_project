$$\frac{\partial \hat{y}_k}{\partial a_j} = \begin{cases} \hat{y}_j - (\hat{y}_j)^2 & \text{when } k=j \\ -\hat{y}_k \hat{y}_j & \text{when } k\neq j \end{cases}$$

$$\hat{y}_k = \frac{\exp(a_k)}{\sum_{m=1}^{n}\exp(a_m)}$$

$$= \sum_{k\neq j} (-y_k)(-\hat{y}_j) - y_j(1-\hat{y}_j)$$

$$+ \left(-\frac{y_j}{\hat{y}_j}\right)\left(\hat{y}_j(1-\hat{y}_j)\right)$$