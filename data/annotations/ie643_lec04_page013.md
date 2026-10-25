**Finite data:** $D = \{(x^i, y^i)\}_{i=1}^{N} < \infty$

$$w^0 = \vec{0} \quad \text{(or random value)}$$

$\rightarrow$ for $t = 0, 1, 2, 3, \dots$ (**epoch**)
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ for $i = 1$ to $N$:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ receive $(x^i, y^i) \in D$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ Predict $\hat{y}^i$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ if $\hat{y}^i = y^i$: no change to weights, else: update weights
