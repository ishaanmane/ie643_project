## Train a perceptron:

$$D = \{(x^t, y^t)\} \quad (\text{online learning}), \qquad t=1,2,3,\dots$$

$\rightarrow \vec{w}^0 = \vec{0}$

$\rightarrow t=0,1,2,3,\dots$

$\rightarrow$ receive a sample $(x^t,y^t) \in D$

$\rightarrow \hat{x}^t = \begin{bmatrix} x^t \\ 1 \end{bmatrix}$

$\rightarrow \hat{y}^t = \text{Perceptron}(\hat{x}^t, \vec{w}^t)$ [Prediction]

**Update rule:**

if $\hat{y}^t == y^t$: no update, $\vec{w}^{t+1} = \vec{w}^t$
else: $\vec{w}^{t+1} = \vec{w}^t + y^t\hat{x}^t$