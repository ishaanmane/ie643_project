# Gradient Descent

$$w^* = (XX^T)^+Xy$$

How computationally expensive is it to compute $w^*$?

If $d$ is large then the inverse is the most expensive: $O(d^3)$

We know $w^*$ is the solution of the unconstrained optimization problem.
We can apply Gradient Descent to get the minimizer of $w^*$.

$$w_{t+1} = w_t - \eta\nabla f(w_t)$$

Our main function: $f(w) = \|Xw-y\|^2 = \sum_{i=1}^{n}(w^Tx_i-y_i)^2$

$$\nabla f(w) = 2(XX^T)w - 2Xy$$

**Gradient Descent update for Linear Regression:**
$$w_{t+1} = w_t - \eta[2(XX^T)w-2Xy]$$

Now we do not have to calculate inverse. $d$ can be as large as possible & it won't be as computationally expensive as the inverse.
