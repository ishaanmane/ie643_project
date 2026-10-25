## Choice of K

Our goal is to minimize the objective function:
$$F(z_1,\dots,z_n) = \sum_{i=1}^{n}\|x_i-\mu_{z_i}\|^2$$

Let the number of clusters be the same as the number of data points. $K=n$.

How will our objective function behave then?

- If every data point will be it's own cluster, then it will be the mean of that cluster. Thus the distance between $x_i$ & $\mu_{z_i}$ will be 0 & $F(z_1,\dots,z_n)=0$.
- The problem we now have is that our goal is being fulfilled as 0 is the minimum value the objective function can have but we don't want all data points to be a separate cluster as it defeats the purpose of clustering.
- So we want $K$ to be as small as possible as having the largest value will minimize the objective function to zero.
- We want to penalize large values of $K$

We want to find $K$ that has the **Smallest objective function value + Penalty(K)** — Perfect balance