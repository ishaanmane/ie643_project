```markdown
# Linear Separability Assumption

The dataset \( D = \left\{ (x^t, y^t) \right\}_{t=1}^{n} \) where \( x^t \in \mathbb{R}^d \) and \( y^t \in \{+1, -1\} \) is called linearly separable if there exists a non-zero vector \( w^* \in \mathbb{R}^d \) and a margin \( \gamma > 0 \) such that:

- If \( y^t = +1 \), then \( <w^*, x^t> > \gamma \)
- If \( y^t = -1 \), then \( <w^*, x^t> < -\gamma \)

This condition ensures that the data can be separated by a hyperplane defined by \( w^* \).
```