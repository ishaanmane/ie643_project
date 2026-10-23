$$L(\mu,\sigma^2; \{x_1,\dots,x_n\}) = P(x_1\cdots x_n; \mu,\sigma^2)$$

$$= \prod_{i=1}^{n} P(x_i;\mu,\sigma^2) = \prod_{i=1}^{n} f_{x_i}(x_i;\mu,\sigma^2)$$

$$= \prod_{i=1}^{n}\left[\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x_i-\mu)^2}{2\sigma^2}}\right]$$

Taking log we get,

$$= \sum_{i=1}^{n}\log\left(\frac{1}{\sigma\sqrt{2\pi}}\right) - \frac{(x_i-\mu)^2}{2\sigma^2}$$

$$\hat{\mu}_{ML} = \operatorname*{argmax}_\mu \sum_{i=1}^{n}\left[-(x_i-\mu)^2\right]$$

Taking derivative & setting it to 0 we get,

$$\boxed{\hat{\mu}_{ML} = \frac{1}{n}\sum_{i=1}^{n}x_i}$$
