$$\hat{y} = \begin{bmatrix} q_1 \\ q_2 \\ \vdots \\ q_C \end{bmatrix}, \quad q_j > 0, \quad \sum_j q_j = 1$$

Compare two discrete prob distr's
$\rightarrow$ **KL divergence**
$\rightarrow$ Bregman div
$\rightarrow$ JS div ...

## KL div b/w p and q

$$KL(p \| q) = \sum_{j=1}^{C} p_j \log \frac{p_j}{q_j} = \mathbb{E}_p \log \frac{p}{q}$$

true distribution.
