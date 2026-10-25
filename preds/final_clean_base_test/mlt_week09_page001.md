```markdown
# Perceptron Learning Algorithm

## Discriminative Model for Classification

### How to Model P(y=1/x)?

The simplest assumption is:
$$
P(y=1/x) = 
\begin{cases} 
1 & \text{if } w^T x \geq 0 \\
0 & \text{otherwise}
\end{cases}
$$

This implies that the data is linearly separable.

[Diagram: Linearly Separable Data]

- **Linearly Separable Data:** The data can be separated by a hyperplane.
- **No Linear Separator:** The data cannot be separated by a hyperplane.

### Can We Develop Algorithms with the Assumption That the Data Is Linearly Separable?

#### Goal:
Minimize
$$
\min_{h \in H_{\text{linear}}} \sum_{i=1}^{n} I(h(x_i) \neq y_i)
$$
where
$$
H_{\text{linear}} = \left\{
h_w : h_w(w) = \text{sign}(w^T x)
\right\}
$$
assuming "Linear Separability".

#### Perceptron Algorithm

Input: $\{(x_1, y_1), \ldots, (x_n, y_n)\}$, $x_i \in \mathbb{R}^d$, $y_i \in \{+1, -1\}$

```
```