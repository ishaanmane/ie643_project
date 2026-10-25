```markdown
# Linear Separability Assumption

The dataset \( D = \left\{ (x^t, y^t) \right\}_{t=1,2,\ldots} \) is called linearly separable if there exists a non-zero vector \( w^* \in \mathbb{R}^d \) and a scalar \( \gamma > 0 \) such that:

- If \( y^t = +1 \):
  $$ 
  <w^*, x^t> > \gamma 
  $$

- If \( y^t = -1 \):
  $$ 
  <w^*, x^t> < -\gamma 
  $$

Here, the inequality conditions ensure that the data points can be separated by a hyperplane defined by \( w^* \).
```