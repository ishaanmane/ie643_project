# Gaussian Model Mixtures

Let's say we have a few 1 Dimensional data points

[Diagram: A number line with points $x_7, x_3, x_4$ clustered on the left, $x_6, x_1, x_5$ clustered in the middle, and $x_8, x_2, x_9$ clustered on the right.] $x_i \in \mathbb{R} \; \forall i$

- What could be a good "generative" story?

$\rightarrow$ We can assume that the model is Gaussian. The maximum likelihood will find the best possible mean to explain the data under the assumed model. Let's say this is the $\hat{\mu}_{ML}$:

[Diagram: A single Gaussian bell curve fitted over the same number line, centered near the middle cluster with $\hat{\mu}_{ML}$ marked.]

The problem is that the regions of $x_7,x_3,x_4,x_8,x_2,x_9$ are very less dense. Implying that the probability of having datapoints there is very less. However, as we can see, it is not true. The model which we've assumed is just not good enough!

To solve the problem, we want a density like this:
