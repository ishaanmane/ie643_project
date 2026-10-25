# Nature of clusters produced by K-Means

Let $K=2$. Lloyd's algorithm will produce 2 clusters with means: $\mu_1$ & $\mu_2$

What can we say about the points assigned to cluster 1?

$\rightarrow$ By the algorithm's convergence, each data point in cluster 1 is now closer to $\mu_1$ than $\mu_2$: $\boxed{\|x-\mu_1\|^2 \leq \|x-\mu_2\|^2}$

$$= \|x\|^2+\|\mu_1\|^2-2x^T\mu_1 \leq \|x\|^2+\|\mu_2\|^2-2x^T\mu_2$$
$$= \|\mu_2\|^2-\|\mu_1\|^2 \geq 2x^T(\mu_2-\mu_1)$$
$$= x^T(\mu_2-\mu_1) \leq \frac{\|\mu_2\|^2-\|\mu_1\|^2}{2} \quad [\forall x \text{ in cluster 1}]$$

[Diagram: 2D plane split by a line into "Cluster 1 region" (yellow) and "Cluster 2 region" (green), with means $\mu_1, \mu_2$ marked and the orange separating line labeled $x^T(\mu_2-\mu_1) = \frac{\|\mu_2\|^2-\|\mu_1\|^2}{2}$, parallel to the green line through the origin labeled $x^T(\mu_2-\mu_1)=0$.]

What happens when $K=3$?
