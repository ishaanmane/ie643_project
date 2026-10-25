```markdown
# Property

If \( u \) (a non-zero vector) is a descent direction of \( f \) in \( f: \mathbb{R}^d \to \mathbb{R} \) at \( x \), then:

- There exists some \( \epsilon > 0 \) such that
- For every \( \alpha \in [0, \epsilon] \),
  $$ \lim_{\alpha \downarrow 0} \frac{f(x + \alpha u) - f(x)}{\alpha} < 0 $$
- This implies:
  $$ f(x + \alpha u) < f(x) $$
- Therefore,
  $$ f'(x; u) < 0 $$
```