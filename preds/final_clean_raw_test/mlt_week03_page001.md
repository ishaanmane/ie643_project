# Introduction to Clustering

Given the data $\{X_1,\dots,X_n\} \in \mathbb{R}^d$, we want to partition it into $k$ different clusters.

There are multiple ways to partition the data into $k$ different boxes/clusters. We want to know how many ways are there in total. Naively speaking these are $n^k$ numbers of ways where $n$ is the number of data points & $k$ is the number of clusters/boxes.

Goal: performance measure of partitioning data points into clusters.

$$X_1,\dots,X_n \leftarrow \text{Data points}, \quad z_1,\dots,z_n \leftarrow \text{cluster indicator}, \; z_i \in \{1,\dots,k\}$$

eg- 10th point in 4th box $\Rightarrow X_{10}$ in 4, $z_{10} \to 4$

Question: Given a cluster assignment, how good is it?

$$F(z_1,\dots,z_n) = \sum_{i=1}^{n}\|x_i-\underbrace{\mu_{z_i}}_{\text{mean/average of } z_i^{th} \text{ cluster}}\|_2^2 \quad (\text{sum of distance of each point from clusters mean})$$

$$\mu_k = \frac{\sum_{i=1}^{n} x_i \mathbb{1}(z_i=k)}{n} \quad (\text{average of all data points which go to the } k^{th} \text{ cluster})$$