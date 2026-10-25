```markdown
# Initialization of Centroids, K-Means++

Suppose we have 1000 points & we need to put them in 5 different clusters/boxes. We can pick 5 points uniformly at random & imagine these 5 points as the cluster centers. It means that we are initializing the cluster means & not the cluster indicators.

Now for every datapoint we will see the closest mean & assign it to that cluster. We may have to repeat this exercise with n different means to get the best clustering. However, this is a naive way & a better way to do this is the K-Means++.

## K-Means++

The idea behind this is that the means ($\mu_i$) should be as far away from each other as possible. If the means are close then there is no need of separate clusters, we can just make it one big cluster.

### Iteration

→ Choose first mean $\mu^0_1$ uniformly at random from the dataset $\{x_1, \ldots, x_n\}$

→ For $l = 2, \ldots, k$ ($l \rightarrow l^{th}$ mean) choose $\mu^0_l$ probabilistically proportional to score.

$$ S(x) = \min_{j=1,\ldots,l-1} \|x - \mu^0_j\|^2 \quad \forall x $$

## Example

Suppose we have the small dataset
```