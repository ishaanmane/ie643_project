```markdown
# Proof of Convergence of Perceptron Algorithm

## Radius Assumption

For all \( i \in \text{Dataset} \),
$$ \| x_i \|_2 < R \quad \text{for some } R > 0 $$

[Diagram: A circle with radius \( R \) centered at the origin, with several vectors inside it.]

## Without Loss of Generality, Assume \( \| w^* \| = 1 \)

[Diagram: A vector \( w^* \) of length 1, pointing from the origin to a point on the unit sphere.]

## Analysis of "Mistakes" of Perceptron

- Observe that an update happens only when a mistake occurs.
- Let \( w^l \) be the current \( w \) & a mistake occurs in \( w \) wrt \( (x, y) \).
  - Therefore,
    $$ w^{l+1} = w^l + x \cdot y $$
```
