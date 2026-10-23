Suppose we have the small dataset $X = [(7,4),(8,3),(5,9),(3,3),(1,3),(10,1)]$ to which we wish to assign 3 clusters. $k=3$

We begin by randomly selecting $(7,4)$ to be a cluster center: $\mu_1^0$

| $x$ | $\min(d(x,\mu_1^0)^2) = S(x)$ |
|---|---|
| (7,4) | - |
| (8,3) | 2 |
| (5,9) | 29 |
| (3,3) | 17 |
| (1,3) | 37 |
| (10,1) | 18 |

Total = 103

| $x$ | prob |
|---|---|
| (7,4) | - |
| (8,3) | 2/103 ← lowest probability |
| (5,9) | 29/103 |
| (3,3) | 17/103 |
| (1,3) | 37/103 ← highest probability, so we'll choose this as the next mean: $\mu_2^0$ |
| (10,1) | 18/103 |

| $x$ | $\min(d(x,z_i)^2) = S(x)$ |
|---|---|
| (7,4) | - |
| (8,3) | 2 |
| (5,9) | 29 |
| (3,3) | 4 |
| (1,3) | - |
| (10,1) | 18 |

Total = 53

| $x$ | prob |
|---|---|
| (7,4) | - |
| (8,3) | 2/55 |
| (5,9) | 29/55 ← highest probability & the next mean: $\mu_3^0$ |
| (3,3) | 4/55 |
| (1,3) | - |
| (10,1) | 18/55 |
