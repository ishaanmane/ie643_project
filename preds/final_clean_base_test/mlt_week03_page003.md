```markdown
# K-Means Clustering (Lloyd's Algorithm)

## Initialization:
$z_{1}^{0}, z_{2}^{0}, \ldots, z_{n}^{0} \in \{1, \ldots, k\}$

### Step 1: Compute mean.
$\forall k$, compute $\mu_{k}^{t} = \frac{\sum_{i=1}^{n} x_{i} \mathbf{1}(z_{i}^{t}=k)}{\sum_{i=1}^{n} \mathbf{1}(z_{i}^{t}=k)}$

### Step 2: Reassignment step
$\forall i, z_{i}^{t+1} = \arg\min_{k} \|x_{i} - \mu_{k}^{t}\|_{2}^{2}$

[If the mean of the current assignment is shortest, then don't reassign.]

The algorithm will now run until convergence.

In the algorithm, the partition is changing in each round. There will come a point when there is no jumping of points from one partition/box/cluster [distance of each point with its own cluster's mean is strictly less than any other box's mean] then no jumping will happen & the algorithm will be said to have converged.

* **Will it always converge?**
    -> Yes, Lloyd's Algorithm always converges.

Week 3 Page 3
```

This structured Markdown preserves the original content, including mathematical expressions formatted using LaTeX, headings, and the logical flow of the explanation.