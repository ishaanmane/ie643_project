$$\sum_{i=1}^{n}\mathbb{1}(z_i=k) \quad \leftarrow \text{Cluster}$$

$z_i=k$ refers to assignment in the $k^{th}$ cluster.

## Example

$\{x_1,x_2,x_3,x_4,x_5\}, \; k=2$

$z_1=1,z_2=2,z_3=1,z_4=1,z_5=2$

**5 points assigned to 2 boxes/clusters:** $x_1,x_3,x_4$ go to 1st & $x_2,x_5$ go into 2nd

$$\mu_1 = \frac{x_1+x_3+x_4}{3}, \quad \mu_2 = \frac{x_2+x_5}{2}$$

$\therefore$ Goodness of this partition $= F(z_1,\dots,z_n)$

$$= (x_1-\mu_1)^2+(x_2-\mu_2)^2+(x_3-\mu_1)^2+(x_4-\mu_1)^2+(x_5-\mu_2)^2$$

Now that we've established a way to measure goodness,

Goal: $\min_{(z_1,\dots,z_n)} \sum_{i=1}^{n}\|x_i-\mu_{z_i}\|_2^2$

$\Rightarrow$ Doing this will be difficult as there will be too many calculations ($n^k$).