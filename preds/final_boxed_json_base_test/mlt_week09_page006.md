```markdown
# Proof of Convergence of Perceptron Algorithm

## Radius Assumption

For all \( i \in \) Dataset, \( \|x_i\|_2 < R \), for some \( R > 0 \)

[Diagram: A circle with radius \( R \) containing several points inside it]

## Without loss of generality, assume \( \|w^*\| = 1 \)

[Diagram: A vector \( w^* \) of length 1, a circle centered at the origin with radius \( R \), and a point \( x \) inside the circle]

## Analysis of "Mistakes" of Perceptron

- Observe that an update happens only when a mistake occurs.
- Let \( w^k \) be the current \( w \) & a mistake occurs in \( w \) wrt \( (x, y) \)
  
\[ w^{k+1} = w^k + x \cdot y \]
```
```