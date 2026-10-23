# EM Algorithm

## Expectation Maximization

$\rightarrow$ Initialize $\theta^0 = \left\{\mu_1^0,\dots,\mu_K^0; \; \sigma_1^{0\,2},\dots,\sigma_K^{0\,2}; \; \pi_1^0,\dots,\pi_K^0\right\}$ (iteration)

$\rightarrow$ Until Convergence $\left(\|\theta^{t+1}-\theta^t\| \leq \epsilon\right)$ ($\epsilon \rightarrow$ tolerance parameter)

$$\lambda^{t+1} = \operatorname*{argmax}_\lambda \text{ modified } \log L(\theta^t,\lambda) \quad \leftarrow \text{Expectation Step}$$

$$\theta^{t+1} = \operatorname*{argmax}_\theta \text{ modified } \log L(\theta,\lambda^{t+1}) \quad \leftarrow \text{Maximization Step}$$

$\rightarrow$ end

EM converges to a local maximum at log likelihood.
$\therefore$ Our initialization is important.

What we should do is run Lloyd's in a bunch of data points with $K$ clusters & get the hard clustering & use the $\mu$s, $\sigma_k^2$ & $\pi_k$s as the initialization of EM.
