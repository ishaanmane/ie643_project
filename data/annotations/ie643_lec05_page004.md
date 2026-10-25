## Perceptron Decision Rule

[Diagram: A single perceptron neuron (circle) with two inputs. Input $x_1$ arrives via weight $w_1$, input $x_2$ arrives via weight $w_2$. The neuron has two labeled output branches: if the weighted input is $\geq \theta$, output is $+1$; if $< \theta$, output is $-1$.]

$$\text{sign}(w_1 x_1 + w_2 x_2 - \theta) \Rightarrow \hat{y}$$

## Truth Table

| $x_1$ | $x_2$ | $y$ | $\hat{y}$ |
|---|---|---|---|
| 1 | 1 | -1 | $\text{sign}(w_1 + w_2 - \theta)$ |
| 0 | 0 | -1 | $\text{sign}(-\theta)$ |
| 1 | 0 | +1 | $\text{sign}(w_1 - \theta)$ |
| 0 | 1 | +1 | $\text{sign}(w_2 - \theta)$ |

Matching each row's required sign gives the system of constraints:

- $w_1 + w_2 - \theta < 0$
- $-\theta < 0$
- $w_1 - \theta \geq 0$
- $w_2 - \theta \geq 0$
