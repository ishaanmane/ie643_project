# Soft Margin SVM

What if there are outliers in the dataset? How will SVM handle them? Kernels are not the best option.

$$\min_w \frac{1}{2}\|w\|^2 \quad \text{s.t. } (w^Tx_i)y_i\geq1 \; \forall i$$

We are now going to make every $w$ feasible
- Fix any $w$. It will classify some points correctly & some incorrectly.
- The incorrectly classified points will "pay bribe" to go to the "correct side"

## Modified Formulation

**Soft Margin Formulation**
$$\min_{w,\epsilon} \frac{1}{2}\|w\|^2 + c\sum_{i=1}^{n}\epsilon_i \quad \text{(Hyperparameter, } c\geq0\text{)}$$
$$\text{s.t. } (w^Tx_i)y_i+\epsilon_i\geq1 \; \forall i \; \text{(Bribe)}, \quad \epsilon_i\geq0 \; \forall i$$

If $c=0$ then Bribes don't cost, & $w=0\in\mathbb{R}^d$ is the solution.
If $c=\infty$ then all $w$'s are equally bad.
