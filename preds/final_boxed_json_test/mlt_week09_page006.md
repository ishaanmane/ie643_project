# Proof of Convergence of Perceptron Algorithm

## Radius Assumption
$$\forall i \in \text{Dataset}, \quad \|x_i\|_2 < R, \text{ for some } R > 0$$

[Diagram: A circle of radius $R$ centered at the origin, with several data points (dots) inside it, each labeled with an arrow pointing from the origin toward the point, illustrating the direction of the weight vector update.]

Without loss of generality, assume $\|w^*\| = 1$

[Diagram: A dot at the origin with a green arrow $w^*$ pointing right, surrounded by a red circle of radius $R$. A blue line through the origin separates two classes of points ($+$'s and $-$'s). A green arrow $w^+$ is shown near the boundary, with a green arrow $w^-$ further away.]

$$\{x: w^+{}^T x = y'\} \quad \{x: w^-{}^T x = y\}$$

$$w^+{}^T x = y', \qquad w^-{}^T x = y$$

$$y' = \frac{y}{\|w^*\|}, \qquad y = \frac{y}{\|w^*\|}$$

---

## Analysis of "Mistakes" of Perceptron

- Observe that an update happens only when a mistake occurs.
- Let $w^l$ be the current $w$ & a mistake occurs in wrt $(x,y)$:
  $$\therefore w^{l+1} = w^l + x \cdot y$$