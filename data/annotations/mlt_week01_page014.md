# Principal Component Analysis (2)

We want to solve: $\max_{w, \|w\|^2=1} w^TCw$, $\quad C = \frac{1}{n}\sum_{i=1}^{n} x_ix_i^T$

**Solution:** $w_1$ - the largest eigenvector of $C$.

In fact $\{w_1, \dots, w_d\}$ the eigenvectors of $C$ form an orthonormal basis.

$w_k \rightarrow$ best line one can get after $k$ rounds.

What do the eigenvalues of $C$ mean?

we know:
$$Cw_1 = \lambda_1w_1$$
$$w_1^TCw_1 = w_1^T\lambda_1w_1$$
$$w_1^TCw_1 = \lambda_1$$
$$\lambda_1 = w^T\left(\frac{1}{n}\sum_{i=1}^{n}x_ix_i^T\right)w_1$$
$$\lambda_1 = \frac{1}{n}\sum_{i=1}^{n}(x_i^Tw_1)^2$$

$Cw_1 \rightarrow$ eigenvector; $\lambda_1 \rightarrow$ largest eigenvalue corresponding to eigenvector $w_1$

$\lambda_k^{(i)} \rightarrow k^{th}$ largest eigenvalue of $C$

[Diagram: A scatter/decreasing-dot plot with $\lambda_k^{(i)}$ on the y-axis and $k \rightarrow k^{th}$ rounds of the [algorithm] on the x-axis, dots dropping off sharply.]
