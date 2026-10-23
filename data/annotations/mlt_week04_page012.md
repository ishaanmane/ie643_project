# Likelihood of GMM

$$L\left(\mu_1,\dots,\mu_k;\sigma_1^2,\dots,\sigma_k^2;\pi_1,\dots,\pi_k;\{x_1,\dots,x_n\}\right) = \prod_{i=1}^{n}f_{\max}\left(x_i;\mu_1,\dots,\mu_k,\sigma_1^2,\dots,\sigma_k^2,\pi_1,\dots,\pi_k\right)$$

$$= \prod_{i=1}^{n}\left[\sum_{k=1}^{K}\pi_kf(x_i;\mu_k,\sigma_k^2)\right]$$

$$L(\theta) = \prod_{i=1}^{n}\left[\sum_{k=1}^{K}\pi_k \frac{e^{-(x_i-\mu_k)^2/2\sigma_k^2}}{\sigma_k\sqrt{2\pi}}\right] \quad \theta \rightarrow \text{all parameters}$$

$$\log L(\theta) = \sum_{i=1}^{n}\log\left[\sum_{k=1}^{K}\pi_k \frac{e^{-(x_i-\mu_k)^2/2\sigma_k^2}}{\sigma_k\sqrt{2\pi}}\right]$$

- Not possible to solve this analytically
- Need an alternate way to solve the maximization of log likelihood wrt the 3 parameters efficiently.
