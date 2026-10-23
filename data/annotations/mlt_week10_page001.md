# Perceptrons and Margin

$$\#\text{mistakes of Perceptron} \leq \frac{R^2}{\gamma^2}$$

[Diagram: Two parallel green lines $\{x:w^Tx=\gamma\}$, $\{x:w^Tx=-\gamma\}$ around a blue separating line through the origin with normal $w$, with "x" marked points beyond the margin.]

$\|x_i\|^2 < R^2$
Data is linearly separable with margin $\gamma$
$(w^{*T}x_i)y_i \geq \gamma \; \forall i$, $\gamma>0$

---

## "Quality" of Final Solution

In this dataset, $w^*$ is not necessarily the only $w^*$ that separates the dataset with some margin.

[Diagram: Green "x" points and red "-" points separated by two candidate lines with margins shown as shaded bands, normal vector $w^*$.]

Let's see $w_2^*$. The margin is smaller than $w^*$. Which one to prefer?

As the no. of mistakes
