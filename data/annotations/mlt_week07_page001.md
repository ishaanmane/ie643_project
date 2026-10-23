# Introduction to Binary Classification

$$\{x_1,\dots,x_n\} \in \mathbb{R}^d, \qquad y_1,\dots,y_n \in \{0,1\} \text{ or } \{-1,+1\}$$

**Goal:** $h: \mathbb{R}^d \to \{0,1\}$

## Loss/Error

$$\text{Loss}(h) = \frac{1}{n}\sum_{i=1}^{n}\mathbb{1}(h(x_i)\neq y_i) \quad \text{0-1-Loss}$$

$$\mathbb{1}(z) = \begin{cases}1 & \text{if true}\\0 & \text{otherwise}\end{cases}$$

$$\min_{h\in H_{linear}} \sum_{i=1}^{n}\mathbb{1}(h(x_i)\neq y_i) \quad \text{NP Hard Problem}$$

$$H_{linear} = \{h_w: h_w(x) = \text{sign}(w^Tx)\}, \qquad \text{sign}(z) = \begin{cases}1 & \text{if } z>0\\0 & \text{otherwise}\end{cases}$$

[Diagram: A plane split by a line through the origin, normal vector $w$, into green region $\{x: w^Tx<0\}$ and yellow region $\{x: w^Tx>0\}$.]

- Can we use linear regression to solve a classification problem?

Meaning: we will input the data in a linear regression model
