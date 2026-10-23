# K-Means Clustering (Lloyd's Algorithm)

**Initialization:** $z_1^0, z_2^0, \dots, z_n^0 \in \{1,\dots,k\}$ (iteration)

**Step 1:** Compute mean. $\Rightarrow \forall k$ compute $\mu_k^t$ ($t^{th}$ iteration)
$$\mu_k^t = \frac{\sum_{i=1}^{n} x_i\mathbb{1}(z_i^t=k)}{\sum_{i=1}^{n}\mathbb{1}(z_i^t=k)}$$

**Step 2:** Reassignment step
$$\Rightarrow \forall i \; z_i^{t+1} = \operatorname*{argmin}_k \|x_i-\mu_k^t\|_2^2 \quad \text{[if mean of current assignment is shortest, then don't reassign]}$$

The algorithm will now run (until convergence)

In the algorithm, the partition is changing in each round. There will come a point when there is no jumping of points from one partition/box/cluster [distance of each point with it's own clusters' mean is strictly less than any other box's mean] then no jumping will happen & the algorithm will be said to have converged.

\* Will it always converge?
$\rightarrow$ Yes, Lloyd's Algorithm always converges.
