$$\frac{\sum_{i=1}^{n}\|x_i - \mu_{z_i^{t+1}}^{t+1}\|^2}{\text{mean of clusters where } x_i \text{ wants to go}} < \frac{\sum_{i=1}^{n}\|x_i - \mu_{z_i^t}^{t}\|^2}{F(z_1^t,\dots,z_n^t) \text{ mean of current clusters where } x_i \text{ is assigned}} \quad \text{[By algorithm's choice]}$$

$$\sum_{i=1}^{n}\|x_i - \mu_{z_i^{t+1}}^{t+1}\|^2 \leq F(z_1^{t+1},\dots,z_n^{t+1})$$

$$\Rightarrow \sum_{i=1}^{n}\sum_{k=1}^{K}\|x_i-\mu_k^{t+1}\|^2\mathbb{1}(z_i^{t+1}=k)$$

$\Rightarrow$ The objective function strictly reduces after each reassignment:
$$F(z_1^{t+1},\dots,z_n^{t+1}) < F(z_1^t,\dots,z_n^t)$$

$\Rightarrow$ There are only a finite number of partitions
$\Rightarrow$ Algorithm must converge