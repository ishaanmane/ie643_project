If we have more variable it will be Non Convex with/without squares.

$$y_1^2+y_2^2\pm y_3^2\dots+y_1y_2-3y_2y_3+y_4y_5 \quad \text{not positive definite}$$

$\to$ Min $\frac{1}{2}y^TQy+c^Ty$ ← equivalent concave model

$$Ay=b$$
$$y\in\{0,1\}^p$$

We can always add & subtract $y_i^2-y_i$, both are same so we get original model.

$$\text{min } \frac{1}{2}y^TQy+c^Ty+\sigma_1y_1^2+\sigma_2y_2^2+\dots\sigma_ny_n^2-\sigma_1y_1-\sigma_2y_2-\dots-\sigma_ny_n$$

Convex? if choose $\sigma$ to be big enough, this expression will be convex.

$$\boxed{\sigma\geq|\text{most negative (or) smallest eigen value of }Q|} \to \text{mod}$$

Solve QP then branch, then QP then branch.

$$\min y_1^2+y_2^2-y_3^2+7y_4^2 \to +y_3^2-y_3 \; \text{now convex.}$$

1) $\underbrace{x_1x_2}_{w_1}+\underbrace{x_2x_4}_{w_2}+\underbrace{x_1x_3}_{w_3}+x_1x_4+x_1x_5\leq100$

2) $\dfrac{x_1x_4}{w_1}+x_1\underbrace{(x_2+x_3+x_4+x_5)}_{w_3}\leq100$

option 2) is best as we have 2 bilinear terms.

Consider $0\leq x_i\leq10$
