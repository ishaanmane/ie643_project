$$\hat{y} = \begin{bmatrix} q_1 \\ q_2 \\ \vdots \\ q_C \end{bmatrix}, \quad q_j \geq 0, \; \sum q_j = 1$$

KL div b/w $p$ and $q$

$$\text{KL}(p||q) = \sum_{j=1}^{C} p_j \log \frac{p_j}{q_j}$$

$$= \boxed{\int_p \log \frac{p}{q}}$$

true distribution.

Compare two discrete prob dists:
- KL divergence
- Bregman div
- Jst div