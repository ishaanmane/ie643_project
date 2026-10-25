# Proof of Convergence of Perceptron Algorithm

## Radius Assumption
$\forall i \in$ Dataset, $\|x\|_2 < R$, for some $R > 0$

[Diagram: A circle of radius $R$ centered at the origin with several data points (green crosses and red dots) inside it, each labeled with an arrow pointing from the origin.]

Without loss of generality, assume $\|w^*\| = 1$

[Diagram: A dot product decision boundary around the origin — a circle of radius $y'/\|w^*\|$ — with a green vector $w^*$ inside it, and two sets of data points ($+$'s and $-$'s) on either side of the boundary.]

$$\{x: w^*^Tx = y'\} \qquad \{x: w^Tx = y\}$$

$$\frac{w^*^Tx}{\|w^*\|} = \frac{y}{\|w^*\|}, \qquad y' = \frac{y}{\|w^*\|}$$

$$\boxed{(w^*)^Tx = y'} \qquad \boxed{(w^*)^Tx = y}$$

---

## Analysis of "Mistakes" of Perceptron

- Observe that an update happens only when a mistake occurs.
- Let $w^l$ be the current $w$ & a mistake occurs in wrt $(x,y)$
  $$\therefore w^{l+1} = w^l + x \cdot y$$