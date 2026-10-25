```markdown
# K-Means Clustering (Lloyd's Algorithm)

## Initialization:
$z_i^0, z_j^0, \ldots, z_n^0 \in \{1, \ldots, k\}$

### Step 1: Compute mean.
$\Rightarrow \forall k$, compute $\mu_k^{t} = \frac{\sum_{i=1}^{n} x_i \mathbf{1}(z_i^t = k)}{\sum_{i=1}^{n} \mathbf{1}(z_i^t = k)}$

### Step 2: Reassignment step
$\Rightarrow \forall i$, $z_i^{t+1} = \arg\min_k \|x_i - \mu_k^t\|_2$

If the mean of current assignment is shortest, then don't reassign.

The algorithm will now run until convergence.

In the algorithm, the partition is changing in each round. There will come a point when there is no jumping of points from one partition/box/cluster [distance of each point with its own clusters' mean is strictly less than any other box's mean] then no jumping will happen & the algorithm will be said to have converged.

*Will it always converge?
-> Yes, Lloyd's Algorithm always converges.*

Week 3 Page 3
```