```markdown
# Nature of clusters produced by K-Means

Let \( k = 2 \). Lloyd's algorithm will produce 2 clusters with means: \( \mu_1 \) & \( \mu_2 \).

## What can we say about the points assigned to cluster 1?

By the algorithm's convergence, each data point in cluster 1 is now closer to \( \mu_1 \) than \( \mu_2 \):

\[
\| x - \mu_1 \|^{2} \leq \| x - \mu_2 \|^{2}
\]

\[
= \| x \|^{2} + \| \mu_1 \|^{2} - 2 x^T \mu_1 \leq \| x \|^{2} + \| \mu_2 \|^{2} - 2 x^T \mu_2
\]

\[
= \| \mu_2 \|^{2} - \| \mu_1 \|^{2} \geq 2 x^T (\mu_2 - \mu_1)
\]

\[
= x^T (\mu_2 - \mu_1) \leq \frac{\| \mu_2 \|^{2} - \| \mu_1 \|^{2}}{2}
\]

### Diagram: Clusters

[Diagram: Clusters]

What happens when \( k = 3 \)?
```