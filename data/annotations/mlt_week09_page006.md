# Proof of Convergence of Perceptron Algorithm

## Radius Assumption

$\forall i \in$ Dataset, $\|x\|_2 < R$, for some $R>0$

[Diagram: A circle of radius $R$ enclosing several green and red points, with vectors from the origin to each point.]

Without loss of generality, assume $\|w^*\|=1$

[Diagram: A unit circle with vector $w^*$ pointing toward a cluster of "+" points, a shorter collinear vector $w'$, and dashed lines marking the margin boundaries $\{x:w^{*T}x=\gamma\}$ and $\{x:w^{*T}x=-\gamma\}$.]

$$\frac{w^{*T}x}{\|w^*\|} = \frac{\gamma}{\|w^*\|}, \qquad \gamma' = \frac{\gamma}{\|w^*\|}$$
$$\left(\frac{w^*}{\|w^*\|}\right)^Tx = \gamma' \qquad (w^{*'})^Tx = \gamma'$$

---

## Analysis of "Mistakes" of Perceptron

- Observe that an update happens only when a mistake occurs.
- Let $w^\ell$ be the current $w$ & a mistake occurs in wrt $(x,y)$
$$\therefore w^{\ell+1} = w^\ell + x\cdot y$$
