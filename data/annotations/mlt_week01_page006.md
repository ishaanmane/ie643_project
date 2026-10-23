# Representation Learning (2)

**Goal:** Develop a way to find a "compressed" representation when data points do not fall on the line. (will always happen in real datasets.)

There could be an infinite number of lines which will [give the] same amount of compression. We need to choose the one with the least amount of reconstruction error.

**Goal:** Find the line with the least "reconstruction" error.

Dataset: $\{x_1, \dots, x_n\} \in \mathbb{R}^d$

$$\text{Error(line, dataset)} = \sum_{i=1}^{n} \text{error(line}, x_i\text{)}$$

$w$, such that $\|w\|^2=1$

$$= \sum_{i=1}^{n} (x_i - (x_i^Tw)w)$$

$(x_i^Tw)w \rightarrow$ projection vector; $(x_i - (x_i^Tw)w) \rightarrow$ stray vector far away from line

$f(w) \rightarrow$ some function of $w$ which we wanna minimize

$$f(w) = \sum_{i=1}^{n} \|x_i - (x_i^Tw)w\|^2$$

$$f(w) = \frac{1}{n}\sum_{i=1}^{n} \|x_i - (x_i^Tw)w\|^2 \quad \text{[let this be average error instead of sum of error]}$$

$$f(w) = \frac{1}{n}\sum_{i=1}^{n} (x_i - (x_i^Tw)w)^T(x_i - (x_i^Tw)w)$$
