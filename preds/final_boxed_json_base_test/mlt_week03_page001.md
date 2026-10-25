```markdown
# Introduction to Clustering

Given the data $\{X_1, \ldots, X_n\} \in \mathbb{R}^d$, we want to partition it into $k$ different clusters.

There are multiple ways to partition the data into $k$ different boxes/clusters. We want to know how many ways are there in total. Naively speaking, there are $\binom{n}{k}$ numbers of ways where $n$ is the number of data points and $k$ is the number of clusters/boxes.

## Goal: Performance Measure of Partitioning Data Points into Clusters

- $X_1, \ldots, X_n \leftarrow$ Data points
- $Z_1, \ldots, Z_n \leftarrow$ Cluster indicators, $z_i \in \{1, \ldots, k\}$

Example:
- 10th point in 4th box $\Rightarrow X_{10}$ in 4
- $Z_{10} \rightarrow 4$

Question: Given a cluster assignment, how good is it?

$$
F(z_1, \ldots, z_n) = \sum_{i=1}^{n} \|x_i - \overline{\mu_{z_i}}\|^2
$$

- Sum of distance of each point from cluster mean
- $\overline{\mu_{z_i}}$ is the mean/average of the $z_i$th cluster

$$
\overline{\mu_k} = \frac{\sum_{i=1}^{n} x_i \Pi(z_i = k)}{n}
$$

- Average of all data points which go to the $k$th cluster

Page Footer: Week 3 Page
```