# Convergence of K-Means Algorithm

We know that Lloyd's Algorithm always converges.

**Proof:**

Let $x_1,\dots x_l \in \mathbb{R}^d$

$$v^* = \min_{v\in\mathbb{R}^d}\sum_{i=1}^{l}\|x_i-v\|^2$$

We are looking for a vector that minimizes the over all possible vectors $v$, Sum of the distance to the bunch of points

$$v^* = \frac{1}{l}\sum_{i=1}^{l}x_i$$

---

- Let's say we are in the $t^{th}$ iteration of Lloyd's algorithm
- Current assignment:
  $$z_1^t,z_2^t,\dots,z_n^t \in \{1,\dots,k\}$$
  $\mu_k^t$ ← mean of cluster $k$ in iteration $t$
- Suppose convergence doesn't happen. We will update our assignments
  $$z_1^{t+1},z_2^{t+1},\dots,z_n^{t+1} \in \{1,\dots,k\}$$