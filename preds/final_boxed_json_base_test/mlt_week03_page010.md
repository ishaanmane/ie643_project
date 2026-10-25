```markdown
# Clustering with K-Means

Suppose we have the small dataset:

\[ X = \{(7,4), (8,3), (5,9), (3,3), (1,3), (10,1)\} \]

to which we wish to assign 3 clusters.

We begin by randomly selecting $(7,4)$ to be a cluster center.

| $x$ | $\min(d(x,z_i)^2)$ |
| --- | ------------------- |
| $(7,4)$ | -                  |
| $(8,3)$ | 2                  |
| $(5,9)$ | + 29               |
| $(3,3)$ | + 17               |
| $(1,3)$ | + 37               |
| $(10,1)$ | + 18               |

$\sum_{i=1}^{k} u_i^0$

[Diagram: Scatter plot showing initial cluster centers.]

| $x$ | prob |
| --- | ---- |
| $(7,4)$ | -    |
| $(8,3)$ | 2/103 |
| $(5,9)$ | 29/103 |
| $(3,3)$ | 17/103 |
| $(1,3)$ | 37/103 |
| $(10,1)$ | 18/103 |

$\leftarrow$ lowest probability

$\leftarrow$ highest probability so we'll choose this as the next mean: $\mu_2^0$

| $x$ | $\min(d(x,z_i)^2)$ |
| --- | ------------------- |
| $(7,4)$ | -                  |
| $(8,3)$ | 2                  |
| $(5,9)$ | + 29               |
| $(3,3)$ | + 4                |
| $(1,3)$ | -                  |
| $(10,1)$ | + 18               |

$\sum_{i=1}^{k} u_i^0$

[Diagram: Scatter plot showing updated cluster centers.]

| $x$ | prob |
| --- | ---- |
| $(7,4)$ | -    |
| $(8,3)$ | 2/55  |
| $(5,9)$ | 29/55 |
| $(3,3)$ | 4/55  |
| $(1,3)$ | -    |
| $(10,1)$ | 18/55 |

$\leftarrow$ highest probability & the next mean: $\mu_3^0$

(Week 3 Page 10)
```