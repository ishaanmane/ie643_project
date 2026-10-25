[Diagram: A plot of objective function vs. $k$, with a red dashed line showing the objective, a blue solid line showing $\text{penalty}(k)$, and their sum (purple) crossing at $k^*$.]

Some common criterion for choosing $\boxed{\text{Obj} + \text{Penalty}}$

- **AIC** - Akaike Information Criterion: $2k - 2\log(L(\hat{\theta}^*))$
- **BIC** - Bayesian Information Criterion: $k(\log n) - 2\log(L(\hat{\theta}^*))$