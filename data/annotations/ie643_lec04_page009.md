$$\|w^{t+1}\|_2^2 = \|w^t\|_2^2 + \|y^t x^t\|_2^2 + 2y^t \langle w^t, x^t \rangle$$

$$= \|w^t\|_2^2 + (y^t)^2 \|x^t\|_2^2 + 2y^t \langle w^t, x^t \rangle$$

$$= \|w^t\|_2^2 + \|x^t\|_2^2 + 2y^t \langle w^t, x^t \rangle$$

$$\|w^{t+1}\|^2 - \|w^t\|^2 = \|x^t\|_2^2 + 2y^t \langle w^t, x^t \rangle$$

Perceptron prediction: $\text{sign}(\langle w^t, x^t \rangle) = \hat{y}^t \neq y^t$
