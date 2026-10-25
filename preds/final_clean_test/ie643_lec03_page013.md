Consider a round $t$ at which perceptron makes a mistake.

$$\hat{y}^t \neq y^t$$

$$w^{t+1} = w^t + y^t x^t \quad \text{before mistake}$$

$$\langle w^*, w^{t+1} \rangle \text{ and } \langle w^*, w^t \rangle \text{ behave?}$$

$$\langle w^{t+1}, w^* \rangle = \langle w + y^t x^t, w^* \rangle = \langle w, w^* \rangle + \langle y^t x^t, w^* \rangle = \langle w, w^* \rangle + y^t \langle x^t, w^* \rangle$$