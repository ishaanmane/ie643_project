# Perceptron Learning Algorithm

## Discriminative Model for Classification

How to model $P(y=1/x)$?

Simplest assumption: $P(y=1/x) = \begin{cases}1 & \text{if } w^Tx\geq0\\0 & \text{otherwise}\end{cases}$

$\therefore$ Data is Linearly Separable.

[Diagram: Green (+1) and red (-1) points separated by a line through the origin with normal $w$, labeled "ALLOWED under our model!!" and "Linear separate exists".]

[Diagram: Green points and a red outlier toward the upper right, and red points toward the lower left, with no separator drawn; labeled "DATASET is NOT allowed under our model" and "No linear separator".]

Can we develop algorithms with the assumption that the data is linearly separable?

$$\text{Goal:} \min_{h\in H_{linear}} \sum_{i=1}^{n}\mathbb{1}(h(x_i)\neq y_i) \qquad H_{linear}=\{h_w: h_w(w)=\text{sign}(w^Tx)$$

assuming "Linear Separability"

---

## Perceptron Algorithm

Input: $\{(x_1,y_1),\dots,(x_n,y_n)\}$, $x_i\in\mathbb{R}^d$, $y_i\in\{+1,-1\}$
