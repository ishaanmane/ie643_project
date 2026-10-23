$$= \sum_{i=1}^{n}\sum_{k=1}^{K}\lambda_k^i\log(a_{ik}) - \lambda_k^i\log\lambda_k^i, \quad \text{where } a_{ik} = \frac{\pi_k e^{-(x_i-\mu_k)^2/2\sigma^2}}{\sigma\sqrt{2\pi}}$$

Taking the derivative wrt $\mu,\sigma$ to get: (only these terms matter)

$$\hat{\mu}_k^{ML} = \frac{\sum_{i=1}^{n}\lambda_k^ix_i}{\sum_{i=1}^{n}\lambda_k^i} \quad \text{weighted mean}$$

$$\hat{\sigma}_k^{2\,ML} = \frac{\sum_{i=1}^{n}\lambda_k^i(x_i-\hat{\mu}_k^{ML})^2}{\sum_{i=1}^{n}\lambda_k^i} \quad \text{weighted sample variance}$$

$$\max_{\pi_1,\dots,\pi_k} \sum_{i=1}^{n}\left(\sum_{k=1}^{K}\lambda_k^i\log\pi_k\right) \text{ such that } \sum_k\pi_k=1; \pi_k\geq0$$

can be solved using method of Lagrange Multiplier

$$\hat{\pi}_k^{ML} = \frac{\sum_{i=1}^{n}\lambda_k^i}{n} \quad \text{weighted probab. of point belonging, weights are given by } \lambda_k^i$$

Fixing $\theta$ & maximizing $\lambda$

$$\max_\theta \sum_{i=1}^{n}\sum_{k=1}^{K}\lambda_k^i\left[\log\left(\pi_k e^{-(x_i-\mu_k)^2/2\sigma_k^2}\right)\Big/\sigma\sqrt{2\pi}\Big/\lambda_k^i\right]$$

$$= \sum_{i=1}^{n}\sum_{k=1}^{K}\lambda_k^i\log(a_{ik}) - \lambda_k^i\log\lambda_k^i$$
