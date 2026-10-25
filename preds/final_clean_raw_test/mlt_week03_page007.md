## Nature of clusters produced by K-Means

Let $k=2$. Lloyd's algorithm will produce 2 clusters with means: $\mu_1$ & $\mu_2$

What can we say about the points assigned to cluster 1?

> By the algorithm's convergence, each data point in cluster 1 is now closer to $\mu_1$ than $\mu_2$: $\|x-\mu_1\|^2 \leq \|x-\mu_2\|^2$

$$\|x\|^2 + \|\mu_1\|^2 - 2x^T\mu_1 \leq \|x\|^2 + \|\mu_2\|^2 - 2x^T\mu_2$$
$$\|\mu_2\|^2 - \|\mu_1\|^2 \geq 2x^T(\mu_2-\mu_1)$$
$$x^T(\mu_2-\mu_1) \leq \frac{\|\mu_2\|^2 - \|\mu_1\|^2}{2} \quad \text{∀ } x \text{ in cluster 1}$$

[Diagram: A 2D scatter plot showing two clusters — yellow shaded region labeled "Cluster 1 region" on the left, green shaded region labeled "Cluster 2 region" on the right. A dashed line from $\mu_1$ to $\mu_2$ is drawn through the origin, with an arrow pointing to $(x_2-\mu_1)$ and another to $(x_2-\mu_2)$. A horizontal line at the origin shows $x^T(\mu_2-\mu_1)=0$, with an arrow above it pointing to "$x^T(\mu_2-\mu_1) = \frac{\|\mu_2\|^2 - \|\mu_1\|^2}{2}$".]

What happens when $K=3$?