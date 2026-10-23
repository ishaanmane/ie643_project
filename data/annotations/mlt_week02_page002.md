## Time Complexity Issue with PCA

$[d \gg n]$ — $d \rightarrow$ no. of features, $n \rightarrow$ no. of datapoints

$$X = \begin{bmatrix} | & | & & | \\ x_1 & x_2 & \cdots & x_n \\ | & | & & | \end{bmatrix}, \quad x \in \mathbb{R}^d \qquad C = \frac{1}{n}\sum_{i=1}^{n}x_ix_i^T$$

$$XX^T = \begin{bmatrix} | & & | \\ x_1 & \cdots & x_n \\ | & & | \end{bmatrix}\begin{bmatrix} -x_1- \\ \vdots \\ -x_n- \end{bmatrix} = \sum_{i=1}^{n}x_ix_i^T$$

$$\Rightarrow C = \frac{1}{n}XX^T$$

Let $w_k$ be the eigenvector corresponding to the $k^{th}$ largest eigenvalue of $C$ ($\lambda_k$)

$$Cw_k = \lambda_kw_k \quad \text{(by definition)}$$
$$\left(\frac{1}{n}\sum_{i=1}^{n}x_ix_i^T\right)w_k = \lambda_kw_k$$
$$w_k = \frac{1}{n}\sum_{i=1}^{n}\left(\frac{x_i^Tw_k}{n\lambda_k}\right)x_i$$

$w_k$ is a linear combination of data points

$$w_k = X\alpha_k \quad \text{for some } \alpha_k \in \mathbb{R}^n$$
