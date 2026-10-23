- We can remedy this by restricting the search space.
- By imposing "structure" to reduce search space

**Simplest structure — Linear Structure**

[Diagram: A large circle $H$ (set of all functions $h:\mathbb{R}^d\to\mathbb{R}$) containing a smaller circle $H_{linear}$.]

$$H_{linear} = \left\{h_w: \mathbb{R}^d \to \mathbb{R} \text{ such that } h_w(x)=w^Tx, \; \forall w \in \mathbb{R}^d\right\}$$

**Goal:** $\min_{h_w \in H_{linear}} \sum_{i=1}^{n}(h_w(x_i)-y_i)^2$

or equivalently,

$$\min_{w \in \mathbb{R}^d} \sum_{i=1}^{n}[w^Tx_i-y_i]^2$$

This can also become 0. But that won't be considered as overfitting as our model will be corresponding
