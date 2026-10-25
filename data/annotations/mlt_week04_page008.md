$$\underbrace{f_{p/\text{Data}}(p)}_{\text{Posterior}} \propto \underbrace{\left[\prod_{i=1}^{n}p^{x_i}(1-p)^{1-x_i}\right]}_{\text{Likelihood}} \; \underbrace{p^{\alpha-1}(1-p)^{\beta-1}}_{\text{Prior}}$$

$$f_{p/\text{Data}}(p) \propto p^{\sum x_i+\alpha-1} \cdot (1-p)^{\sum(1-x_i)+\beta-1}$$

Same functional form as Prior!

Beta Prior $\xrightarrow{\text{Data: Bernoulli}}$ Beta Posterior$(\alpha+n_h, \beta+n_t)$

$n_h \rightarrow$ no. of heads, $n_t \rightarrow$ no. of tails

$$E[\text{Posterior}] = E[\text{Beta}(\alpha+n_h,\beta+n_t)] = \frac{\alpha+n_h}{(\alpha+\beta)+n}$$
