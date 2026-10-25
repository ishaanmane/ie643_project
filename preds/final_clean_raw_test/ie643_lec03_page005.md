## Train a perceptron:

$$D = \{(x^t, y^t)\}_{t=1,2,3,\dots} \quad (\text{Online learning})$$

$\rightarrow \tilde{w}^0 = 0$

$\rightarrow t=0,1,2,3,\dots$

$\rightarrow$ receive a sample $(x^t,y^t) \in D$

$\rightarrow \hat{x}^t = \begin{bmatrix} x^t \\ 1 \end{bmatrix}$

$\rightarrow \hat{y}^t = \text{Perceptron}(\hat{x}^t, \tilde{w}^t)$ [Prediction]

## Update rule:

if $\hat{y}^t == y^t$: no update, $\tilde{w}^{t+1} = \tilde{w}^t$
else: $\boxed{\tilde{w}^{t+1} = \tilde{w}^t + y^t \hat{x}^t}$