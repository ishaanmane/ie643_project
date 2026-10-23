$$\sum_{t=0}^{T} \|w^{t+1}\|^2 - \|w^t\|^2$$

$$= \sum_{t: \text{mistake is made}} \|w^{t+1}\|^2 - \|w^t\|^2 \leq MR^2$$

$$+ \sum_{t: \text{no mistake is made}} \|w^{t+1}\|^2 - \|w^t\|^2 \to 0$$

Expanding this sum we get:
$$\|w^{T+1}\|_2^2 - \|w^0\|^2 \implies \|w^{T+1}\|_2^2 \leq MR^2$$
