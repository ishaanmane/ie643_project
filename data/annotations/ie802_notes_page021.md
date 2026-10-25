④ $3x_2-2x_3+x_4-4x_5 \geq \dfrac{y_1}{1+x_1+x_{10}}$

$$50\geq x\geq0$$
$$y\in\{0,1\}$$
$y_1$ is binary.

What will be good relaxation.

$$\frac{(3x_2-2x_3+x_4-4x_5)}{w_1}\underbrace{(1+x_1+x_{10})}_{w_2}\geq y_1$$

$$w_1\cdot w_2\geq y_1$$

we can come up with relaxations to different cases of $y=0, y=1$.

**Trick:** $y_1\in\{0,1\} \Leftrightarrow y_1=y_1^2$

add a square to $y$: $\to y_1^2$

can try adding $y_1^2$, this makes constraint convex. We can induce convex.

$$H/W: \quad w_1\geq\frac{x_1^2}{x_2}$$

Trying to see some things works.

$$\text{Min } y_1^2+y_2^2-y_3^2+7y_4^2-8y_5^2$$
$$Ay=b$$
$$y\in\{0,1\}^p$$

**Add squares to make nonlinear to linear integer model**
$$y_1+y_2-y_3+7y_4-8y_5$$
