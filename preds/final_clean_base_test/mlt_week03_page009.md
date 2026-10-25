```markdown
# Initialization of Centroids, K-Means++

Suppose we have 1000 points & we need to put them in 5 different clusters/boxes. We can pick 5 points uniformly at random & imagine these 5 points as the cluster centers. It means that we are initializing the cluster means & not the cluster indicators.

Now for every datapoint we will see the closest mean & assign it to that cluster. We may have to repeat this exercise with n different means to get the best clustering. However, this is a naive way & a better way to do this is the K-Means++.

## K-Means++

The idea behind this is that the means (μ_i) should be as far away from each other as possible. If the means are close then there is no need of separate clusters; we can just make it one big cluster.

→ Choose first mean μ_1^0 uniformly at random from the dataset {x_1, ..., x_n}

→ For l = 2, ..., k (l → l<sup>th</sup> mean) choose μ_l^0 probabilistically proportional to score.

$$
S(x) = \min_{j=1, ..., l-1} \|x - μ_j^0\|^2 \quad ∀x
$$

### Example

Suppose we have the small dataset
```
```