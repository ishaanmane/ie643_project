```markdown
Suppose we have the small dataset

\[
X = \{(7,4), (8,3), (5,9), (3,3), (1,3), (10,1)\}
\]

to which we wish to assign 3 clusters.

We begin by randomly selecting $(7,4)$ to be a cluster center.

| $x$ | $\min(d(x,z_i)^2)$ |
| --- | ------------------- |
| $(7,4)$ | - |
| $(8,3)$ | 2 |
| $(5,9)$ | + 29 |
| $(3,3)$ | + 17 |
| $(1,3)$ | + 37 |
| $(10,1)$ | + 18 |

[Diagram: Scatter plot with points labeled according to their distances from the initial cluster center.]

Next, calculate probabilities:

| $x$ | prob |
| --- | ---- |
| $(7,4)$ | - |
| $(8,3)$ | 2/103 |
| $(5,9)$ | 29/103 |
| $(3,3)$ | 17/103 |
| $(1,3)$ | 37/103 |
| $(10,1)$ | 18/103 |

The point with the lowest probability is $(8,3)$, so it will be chosen as the next mean: $\mu_2^0$.

[Diagram: Updated scatter plot with the new cluster center marked.]

Re-calculate distances and probabilities:

| $x$ | $\min(d(x,z_i)^2)$ |
| --- | ------------------- |
| $(7,4)$ | - |
| $(8,3)$ | 2 |
| $(5,9)$ | + 29 |
| $(3,3)$ | + 4 |
| $(1,3)$ | - |
| $(10,1)$ | + 18 |

[Diagram: Further updated scatter plot showing the progression of clustering.]

The point with the highest probability is now $(3,3)$, so it will be chosen as the next mean: $\mu_3^0$.

[Diagram: Final scatter plot showing all cluster centers.]

Week 3 Page 10
```