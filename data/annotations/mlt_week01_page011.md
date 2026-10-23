# Principal Component Analysis (1)

$$D = \{x_1, x_2, \dots, x_n\}, \; x_i \in \mathbb{R}^d$$

$$w_1 = \operatorname*{argmax}_{w, \|w\|^2=1} w^TCw \qquad C = \frac{1}{n}\sum_{i=1}^{n} x_ix_i^T$$

our new dataset in $\mathbb{R}^d$:
$$x_1' = x_1 - (x_1^Tw_1)w_1$$
$$x_2' = x_2 - (x_2^Tw_1)w_1$$
$$\vdots$$
$$x_n' = x_n - (x_n^Tw_1)w_1$$

Best line that fits residues:
$$w_2 = \operatorname*{argmax}_{w, \|w\|^2=1} w^TC'w \qquad C' = \frac{1}{n}\sum_{i=1}^{n} x_i'x_i'^T$$

Now we have 2 lines $w_1$ & $w_2$. What can we say about their relationship?

[Diagram: Two orthogonal lines $w_1$ (purple) and $w_2$ (blue) through the origin, with data points $x_1, x_2$ and their projections $(x_1^Tw_1)w_1$, $(x_2^Tw_1)w_1$ marked with dashed red lines.]

In 2D $\rightarrow$ line $\perp$ to $w_1$; in higher dim $\rightarrow$ hyperplane $\perp$ to $w_1$

## Observations

$\rightarrow$ All errors (residues) are orthogonal to $w_1$

$\rightarrow$ Any line which minimizes the sum of errors wrt residues must also be orthogonal to $w_1$. [Argue why]

$$\Rightarrow \boxed{w_2^Tw_1 = 0}$$

$w_2$ is perpendicular to $w_1$ & they are both of unit length.
