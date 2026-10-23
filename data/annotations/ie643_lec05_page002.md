$$w^0 = 0$$

for $t = 0,1,2,\dots$
- $(x^t, y^t)$
- $\hat{y}^t = \text{Perceptron}(\cdot)$
- if $y^t = \hat{y}^t$: no update, $w^{t+1} = w^t$
- else: $w^{t+1} = w^t + y^t x^t$

$$T \rightarrow \infty$$

Num of mistakes: $M$, $\quad M < \infty, \quad M \leq B$

> At $t$ where perceptron makes a mistake: $\langle w^*, w^{t+1} \rangle - \langle w^*, w^t \rangle > \gamma$
>
> $$\sum_{t=0}^{T} \; \Rightarrow \; \langle w^{T+1}, w^* \rangle > M\gamma$$
