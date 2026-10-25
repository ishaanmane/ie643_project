# Perceptron Learning Algorithm

## Discriminative Model for Classification

How to model $P(y=1/x)$?

Simplest assumption: $P(y=1/x) = \begin{cases} 1 & \text{if } w^Tx \geq 0 \\ 0 & \text{otherwise} \end{cases}$

$\therefore$ Data is Linearly Separable.

[Diagram: Two scatter plots — one with a linear separator (blue line) through the origin separating red and green points (linear separable), labeled "Linear separate exists, ALLOWED under our model"; the other with no linear separator, labeled "No linear separator, DARKER is NOT allowed under our model".]

Can we develop algorithms with the assumption that the data is linearly separable?

**Goal:** $\min_{h\in H_{\text{linear}}} \sum_{i=1}^{n}\mathbb{I}(h(x_i)\neq y_i)$

$$H_{\text{linear}} = \left\{ h_w: h_w(w) = \text{sign}(w^Tx) \right\}$$

assuming "Linear Separability"

---

## Perceptron Algorithm

Input: $\{(x_1,y_1),\dots,(x_n,y_n)\}, \quad x_i\in\mathbb{R}^d$
$$y_i\in\{+1,-1\}$$