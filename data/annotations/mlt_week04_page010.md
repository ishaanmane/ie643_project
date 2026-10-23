[Diagram: Three overlapping Gaussian bumps over the same number line, one centered on each cluster of points.]

Mixed Gaussian Models are required

How to create a story (probabilistic mechanism) now?

**Step 1:** Pick which mixture/cluster a datapoint comes from. Generate a mixture component among $\{1,\dots,k\}$ mixtures. It will be denoted by $z_i \in \{1,\dots,k\}$
$$P(z_i=\ell) = \pi_\ell \qquad \left[\sum_{i=1}^{k}\pi_i=1, \; 0\leq\pi_i\leq1 \;\forall i\right]$$

**Step 2:** Generate datapoint from that mixture. Generate $x_i \sim N(\mu_{z_i}, \sigma_{z_i}^2)$

[Diagram: A box labeled $\pi$ branching to $k$ boxes labeled $\mu_1,\sigma_1^2$ through $\mu_k,\sigma_k^2$, one of which produces $x_i$.]

The mixture indicator models: $\{z_1,\dots,z_k\}$ are unobserved quantities.
