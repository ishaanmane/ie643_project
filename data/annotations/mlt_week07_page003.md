# K-Nearest Neighbours

## Simplest Algorithm for Classification

- Given a point $x_{test} \in \mathbb{R}^d$, find the closest point $x^*$ to $x_{test}$ in the training set.
- Predict $y_{test} = y^*$

**Issue:** $x^*$ can be an outlier
**Fix:** "ask" more "neighbours"

---

## K-NN Algorithm

- Given $x_{test}$, find the k-closest points in the training set: $(x_1^*,x_2^*,\dots,x_k^*)$
- Predict $y_{test} = \text{majority}(y_1^*,y_2^*,\dots,y_k^*)$

---

## Decision Boundary

[Diagram: Two scatter plots showing K-NN decision regions. Left, $K=1$: a jagged, highly irregular red/green boundary — "Sensitive to outliers!". Right, $K=n$: entire region uniformly green — "every point is predicted y=-1!".]
