Idea: Transform features from low dimension $\mathbb{R}^d$ to high dimension $\mathbb{R}^D$ where $D>d$

$$x \xrightarrow{\phi} \phi(x)$$
$$\mathbb{R}^d \qquad \mathbb{R}^D$$

What if $D$ is very large? $\rightarrow$ We already know how to deal with that! (previous lecture)

In general if we had $d$ features & want to model upto $p^{th}$ power relationships then, no. of features the mapped $\phi$ would have be:
$$\sum_{i=1}^{p} {}^dC_i \; \left(\binom{d}{k} = \text{"d choose k"}\right) \approx O(d^p)$$
