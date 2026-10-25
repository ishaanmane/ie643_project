Now what if $n$ is large? Then $(XX^T)$ will be computationally expensive.

We can solve this using a variant of G.D.

## Stochastic Gradient Descent

For $t=1,\dots,T$
- At each step, sample a bunch of datapoints ($k$) uniformly at random, from the set of all data points
- Consider this sample as the entire dataset & run GD on: $2(\tilde{X}\tilde{X}^Tw-\tilde{X}\tilde{y})$
  ↳ sample of datapoints, $\tilde{X} \in \mathbb{R}^{d\times k}$

- This will be a noisy gradient & we'll be moving towards the direction of the noise.
- The good news is that over time the noise will cancel out & we'll reach $w^*$ eventually.
- After $T$ rounds take $w_T$ as average of previous $w_t$s

$$\boxed{w_T^{SGD} = \frac{1}{T}\sum_{i=1}^{T}w_t}$$
