Equivalently:

$$\max_{w, \|w\|^2=1} w^TCw \qquad C = \frac{1}{n}\sum_{i=1}^{n} x_ix_i^T$$

**Sol$^n$:** $w$ is the eigenvector corresponding to the maximum eigenvalue of $C$.

If we just solve it, are we done then? Started with datapoints $\rightarrow$ find a line for proxies... doing by solving [above optimization problem].

# All points lies on a plane

[Diagram: A rectangular blue plane through the origin containing several red error vectors ($e_1$ through $e_6$) radiating from a central point, a "proxy line on plane" drawn diagonally across it, labeled "proxy."]

these error vectors also lie on 1 plane (the part that we leave out) — contains some information here, lying on 1 direction. If it was error should be all over the plane.

[Diagram: A small axis with a red double-headed arrow along one diagonal direction.]
