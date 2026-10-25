Consider a round $t$ at which perceptron makes a mistake

$$\hat{y}^t \neq y^t$$

$$w^{t+1} = w^t + y^t x^t$$

$\hookrightarrow \langle w^{t+1}, w^* \rangle$

$$= \langle w^t + y^t x^t, w^* \rangle$$
$$= \langle w^t, w^* \rangle + \langle y^t x^t, w^* \rangle$$
$$= \langle w^t, w^* \rangle + y^t \langle x^t, w^* \rangle$$

after mistake $\quad$ before mistake

$\langle w^*, w^{t+1} \rangle$ and $\langle w^*, w^t \rangle$ behave?