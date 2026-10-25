$$\langle w^*, w^{t+1} \rangle = \langle w^*, w^t + y^t x^t \rangle$$

$$\langle \alpha \vec{u} + \beta \vec{v}, \vec{z} \rangle = \alpha \langle \vec{u}, \vec{z} \rangle + \beta \langle \vec{v}, \vec{z} \rangle$$

$$= \langle w^*, w^t \rangle + y^t \langle w^*, x^t \rangle$$

$$\langle w^*, w^{t+1} \rangle - \langle w^*, w^t \rangle > \gamma$$

> At round $t$ when perceptron doesn't make a mistake:
> $$\langle w^*, w^{t+1} \rangle - \langle w^*, w^t \rangle = 0$$

Over $T$ rounds:
$$\sum_{t=0}^{T} \langle w^{t+1}, w^* \rangle - \langle w^t, w^* \rangle$$
