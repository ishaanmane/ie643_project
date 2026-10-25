# Perceptron Learning Algorithm

## Discriminative Model for Classification

How to model $P(y=1/x)$?

Simplest assumption: $P(y=1/x) = \begin{cases} 1 & \text{if } w^Tx \geq 0 \\ 0 & \text{otherwise} \end{cases}$

$\therefore$ Data is Linearly Separable.

[Diagram: Two scatter plots — one with a clear linear separator (left, "Linear separate exists"), the other with overlapping clusters (right, "No linear separator").]

Can we develop algorithms with the assumption that the data is linearly separable?

**Goal:** $\min_{h \in H_{\text{linear}}} \sum_{i=1}^{n} I(h(x_i) \neq y_i)$

$$H_{\text{linear}} = \{ h_w : h_w(w) = \text{sign}(w^Tx) \}$$

assuming "Linear Separability"

---

## Perceptron Algorithm

Input: $\{(x_1,y_1),\dots,(x_n,y_n)\}, \quad x_i \in \mathbb{R}^d, \quad y_i \in \{+1,-1\}$