Suppose we have the small dataset $X = [(7,4),(8,3),(5,9),(3,3),(1,3),(10,1)]$ to which we wish to assign 3 clusters. $k=3$

We begin by randomly selecting $(7,4)$ to be a cluster center: $\mu_1^0$

[Diagram: Table with columns x and S(x).]

| $x$ | $S(x)$ |
|---|---|
| (7,4) | - |
| (8,3) | 2 |
| (5,9) | 29 |
| (3,3) | 17 |
| (1,3) | 37 |
| (10,1) | 18 |

Total = 103

[Diagram: Scatter plot with six points; red segments connect the selected center (7,4) to the other five points. The horizontal ticks run from 2 to 10 and vertical ticks from 1 to 9.]

[Diagram: Table with columns x and prob.]

| $x$ | prob |
|---|---|
| (7,4) | - |
| (8,3) | 2/103 ← lowest probability |
| (5,9) | 29/103 |
| (3,3) | 17/103 |
| (1,3) | 37/103 ← highest probability, so we'll choose this as the next mean: $\mu_2^0$ |
| (10,1) | 18/103 |

[Diagram: Table with columns x and S(x).]

| $x$ | $S(x)$ |
|---|---|
| (7,4) | - |
| (8,3) | 2 |
| (5,9) | 29 |
| (3,3) | 4 |
| (1,3) | - |
| (10,1) | 18 |

Total = 53

[Diagram: Scatter plot with red segments joining (7,4) to (5,9), (8,3), and (10,1), and a green segment joining (1,3) to (3,3).]

[Diagram: Table with columns x and prob.]

| $x$ | prob |
|---|---|
| (7,4) | - |
| (8,3) | 2/55 |
| (5,9) | 29/55 ← highest probability & the next mean: $\mu_3^0$ |
| (3,3) | 4/55 |
| (1,3) | - |
| (10,1) | 18/55 |
