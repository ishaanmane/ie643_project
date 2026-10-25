$$M\gamma < \langle w^*, w^{T+1} \rangle \leq \|w^*\|_2 \|w^{T+1}\|_2$$

(at $t$, mistake is made:)
$$\|w^{t+1}\|^2 = \|w^t + y^t x^t\|^2$$
$$\Rightarrow \|w^{t+1}\|^2 - \|w^t\|^2 \leq \|x^t\|^2 = R^2$$

$$\sum_{t=0}^{T} \|w^{t+1}\|^2 - \|w^t\|^2 \leq MR^2$$
$$\|w^{T+1}\|^2 \leq MR^2$$

$$M < \frac{\|w^*\|^2 R^2}{\gamma^2}$$

| $x_1$ | $x_2$ | $y$ |
|---|---|---|
| 1 | 1 | -1 |
| 0 | 0 | -1 |
| 0 | 1 | +1 |
| 1 | 0 | +1 |
