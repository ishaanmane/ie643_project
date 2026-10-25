# Linear Regression

Input/Training Data: $\{x_1,\dots,x_n\}$, $x_i \in \mathbb{R}^d$; $\{y_1,\dots,y_n\}$, $y_i \in \mathbb{R}$

**Goal:** Learn $h: \mathbb{R}^d \to \mathbb{R}$ (learn to map an input to a label)

- How to measure "goodness" of the function $h: \mathbb{R}^d \to \mathbb{R}$
- $\text{error}(h_i) = \sum_{i=1}^{n}[h(x_i)-y_i]^2$

**Goal:** Find function $h: \mathbb{R}^d \to \mathbb{R}$ which will have the smallest error.

- How small can this error be? **0**
- Which $h(x_i)$ achieves 0 error? This $h(x_i)=y_i \; \forall i$ will achieve 0 error.

- The problem with this is "overfitting" of data.
- We can get 0 error in training data but the function will not do well in the test data.
- Test performance is important
