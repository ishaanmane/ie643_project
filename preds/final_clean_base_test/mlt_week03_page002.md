```markdown
# Clustering Example

## Problem Statement
Given a set of points $\{x_1, x_2, x_3, x_4, x_5\}$ and $k=2$, we need to assign these points into two clusters.

### Assignment
- $z_1 = 1$
- $z_2 = 2$
- $z_3 = 1$
- $z_4 = 1$
- $z_5 = 2$

This means:
- Points $x_1, x_3, x_4$ go to the first cluster.
- Points $x_2, x_5$ go to the second cluster.

### Cluster Centers
- $\mu_1 = \frac{x_1 + x_3 + x_4}{3}$
- $\mu_2 = \frac{x_2 + x_5}{2}$

### Goodness Measure
The goodness of this partition is defined as:

$$
F(z_1, \ldots, z_n) = (x_1 - \mu_1)^2 + (x_2 - \mu_2)^2 + (x_3 - \mu_1)^2 + (x_4 - \mu_1)^2 + (x_5 - \mu_2)^2
$$

### Optimization Goal
Our goal is to minimize:

$$
\min_{(z_1, \ldots, z_n)} \sum_{i=1}^{n} \|x_i - \mu_{z_i}\|^2_2
$$

### Computational Complexity
This optimization problem will be difficult because there are too many calculations ($n^k$).

---

**Week 3 Page 2**
```