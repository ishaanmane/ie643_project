$$\begin{bmatrix} \hat{y}_1 \\ \hat{y}_2 \\ \vdots \\ \hat{y}_C \end{bmatrix} \leftarrow \begin{bmatrix} a_1^L \\ a_2^L \\ \vdots \\ a_C^L \end{bmatrix} \leftarrow \frac{(a_1)^L}{\sum(a_j)^L}, \quad \text{min-max scaling 1.}$$

$$\hat{y}_j > 0, \qquad \sum_{j}\hat{y}_j = 1.$$

**Soft-max function**

$$\hat{y}_j = \frac{\exp(a_j^L)}{\sum_k \exp(a_k^L)}, \quad k=1$$