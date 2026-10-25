# Convergence of K-Means Algorithm

We know that Lloyd's Algorithm always converges.

**Proof:**

Let $x_1,\dots x_\ell \in \mathbb{R}^d$

$$v^* = \operatorname*{argmin}_{v \in \mathbb{R}^d} \sum_{i=1}^{\ell} \|x_i-v\|^2$$

We are looking for a vector that minimizes the over all possible vectors $v$, sum of the distance to the bunch of points

$$\boxed{v^* = \frac{1}{\ell}\sum_{i=1}^{\ell}x_i}$$

- Let's say we are in the $t^{th}$ iteration of Lloyd's algorithm
- Current assignment: $z_1^t, z_2^t, \dots, z_n^t \in \{1,\dots,k\}$

$\mu_k^t \leftarrow$ mean of cluster $k$ in iteration $t$

- Suppose convergence doesn't happen. We will update our assignments
$$z_1^{t+1}, z_2^{t+1}, \dots, z_n^{t+1} \in \{1,\dots,k\}$$
