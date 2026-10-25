# Proof of Convergence of Perceptron Algorithm

## Radius Assumption

$$\forall i \in \text{Dataset}, \quad \|x_i\|_2 < R, \text{ for some } R > 0$$

[Diagram: A circle of radius $R$ centered at the origin, with several data points (dots) inside it and arrows pointing from the origin toward them.]

Without loss of generality, assume $\|w^*\| = 1$

[Diagram: A dot (data point) inside a red circle of radius $r$, with an arrow $w^*$ pointing outward, labeled $w^*$. To the right, two sets of points — one set $\{x: w^*x > y'\}$ (with $y'$ marked) and another set $\{x: w^*x > y\}$ (with $y$ marked).]

$$\{x: w^*x > y'\} \qquad \{x: w^*x > y\}$$

$$\frac{\|w^*\|^2}{\|w^*\|^2} \frac{x}{\|w^*\|} = \frac{y'}{\|w^*\|} \implies y' = \frac{y}{\|w^*\|}$$

$$\boxed{(w^*)^Tx > y'}$$

---

## Analysis of "Mistakes" of Perceptron

- Observe that an update happens only when a mistake occurs.
- Let $w^l$ be the current $w$ & a mistake occurs wrt $(x,y)$
  $$\therefore w^{l+1} = w^l + x \cdot y$$