## Estimating the Parameters

$$\log L(\theta) = \sum_{i=1}^{n}\log\left(\sum_{k=1}^{K}\pi_k \frac{e^{-(x_i-\mu_k)^2/2\sigma_k^2}}{\sigma_k\sqrt{2\pi}}\right)$$

For every data point $i$, we are going to introduce the parameters: $\{\lambda_1^i,\dots,\lambda_k^i\}$ such that $\forall i \sum_{k=1}^{K}\lambda_k^i=1, \; 0\leq\lambda_k^i\leq1$

Now,
$$\log L(\theta) = \sum_{i=1}^{n}\log\left(\sum_{k=1}^{K}\lambda_k^i \left(\frac{\pi_k e^{-(x_i-\mu_k)^2/2\sigma_k^2}}{\sigma_k\sqrt{2\pi}}\right)\Big/\lambda_k^i\right)$$

By Jensen's,
$$\log L(\theta) \geq \sum_{i=1}^{n}\sum_{k=1}^{K}\lambda_k^i\log\left(\frac{\pi_k e^{-(x_i-\mu_k)^2/2\sigma_k^2}}{\sigma_k\sqrt{2\pi}}\Big/\lambda_k^i\right)$$

Fixing $\lambda$ & maximizing $\theta$

$$\max_\theta \sum_{i=1}^{n}\sum_{k=1}^{K}\lambda_k^i\left[\log\left(\pi_k e^{-(x_i-\mu_k)^2/2\sigma_k^2}\right)\Big/\sigma\sqrt{2\pi}\right]$$

$$\max_\theta \sum_{i=1}^{n}\sum_{k=1}^{K}\left[\lambda_k^i\log\pi_k - \lambda_k^i\frac{(x_i-\mu_k)^2}{2\sigma_k^2} - \lambda_k^i\log\sigma_k\sqrt{2\pi}\right]$$
