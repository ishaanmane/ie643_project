$$\text{where } a_{ik} = \pi_k \frac{e^{-(x_i-\mu_k)^2/2\sigma^2}}{\sigma\sqrt{2\pi}}$$

$$\hat{\lambda}_k^{i\,ML} = \left[\left(\frac{1}{\sigma_k\sqrt{2\pi}}e^{-(x_i-\mu_k)^2/2\sigma^2}\right)\cdot\pi_k\right] \Big/ \left[\sum_{\ell=1}^{K}\left(\frac{1}{\sigma_\ell\sqrt{2\pi}}e^{-(x_i-\mu_\ell)^2/2\sigma_k^2}\cdot\pi_\ell\right)\right]$$

$P(x_i|z_i=k) \rightarrow$ this equals $P(z_i=k|x_i)$

It represents the probability that the $i^{th}$ point goes to the $k^{th}$ cluster. $P(z_i=k|x_i)$ — $z_i \rightarrow$ cluster indicator, $x_i \rightarrow$ data point

$$P(z_i=k|x_i) = \frac{P(x_i|z_i=k)\cdot P(z_i=k)}{P(x_i)}$$
