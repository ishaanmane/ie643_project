$$= \operatorname*{argmax}_p \log\left(\prod_{i=1}^{n}p^{x_i}(1-p)^{1-x_i}\right) \quad [\text{log is monotonically increasing function}]$$

$$= \operatorname*{argmax}_p \sum_{i=1}^{n} x_i\log p + (1-x_i)\log(1-p)$$

Taking the derivative of $\log L(p)$ & setting it to 0 we get,

$$\boxed{\hat{p}_{ML} = \frac{1}{n}\sum_{i=1}^{n}x_i} \leftarrow \text{Fraction of 1's}$$

What if the data is not just 0's & 1's? What if the data is real numbers?

$$\text{Data} = \{x_1,\dots,x_n\}, \; x_i \in \mathbb{R} \; \forall i$$

Heights of random people.

Now the box will be: (Gaussian) parameters $(\mu,\sigma^2)$ $\rightarrow x_1, x_2, \dots, x_n$ (Data generated), $X_i \sim \text{Gaussian}(\mu,\sigma^2) \; \forall i$

Assuming $\mu \rightarrow$ unknown & $\sigma^2 \rightarrow$ known,
