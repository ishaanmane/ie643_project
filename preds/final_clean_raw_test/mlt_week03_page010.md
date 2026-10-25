Suppose we have the small dataset $X = [(7,4),(8,3),(5,9),(3,3),(1,3),(10,1)]$ to which we wish to assign 3 clusters.

We begin by randomly selecting $(7,4)$ to be a cluster center.

[Diagram: A scatter plot of the data points with a red dot at $(7,4)$ labeled "cluster center".]

| $x$ | $\min(d(x,z_i)^2) \rightarrow s(x)$ |
|-----|--------------------------------------|
| $(7,4)$ | - |
| $(8,3)$ | 2 |
| $(5,9)$ | +29 |
| $(3,3)$ | +17 |
| $(1,3)$ | +37 |
| $(10,1)$ | +18 |

$\rightarrow 103$

| $x$ | prob |
|-----|------|
| $(7,4)$ | - |
| $(8,3)$ | $2/103$ $\leftarrow$ lowest probability |
| $(5,9)$ | $29/103$ |
| $(3,3)$ | $17/103$ |
| $(1,3)$ | $37/103$ |
| $(10,1)$ | $18/103$ |

$\leftarrow$ highest probability so we'll choose this as the next mean: $\mu_2^0$

[Diagram: A scatter plot of the data points with a red dot at $(8,3)$ labeled "cluster center", and a green dot at $(5,9)$ labeled "cluster center".]

| $x$ | $\min(d(x,z_i)^2) \rightarrow s(x)$ |
|-----|--------------------------------------|
| $(7,4)$ | - |
| $(8,3)$ | 2 |
| $(5,9)$ | +29 |
| $(3,3)$ | +4 |
| $(1,3)$ | - |
| $(10,1)$ | +18 |

$\rightarrow 53$

| $x$ | prob |
|-----|------|
| $(7,4)$ | - |
| $(8,3)$ | $2/55$ |
| $(5,9)$ | $29/55$ |
| $(3,3)$ | $4/55$ |
| $(1,3)$ | - |
| $(10,1)$ | $18/55$ |

$\leftarrow$ highest probability & the next mean: $\mu_3^0$