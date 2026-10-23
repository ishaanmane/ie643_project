[Diagram: A plot of "obj + penalty(K)" vs $K$ — the red "objective function" curve decreases monotonically from $K=1$ toward $K=n$, the blue "penalty(K)" curve increases, and their sum (purple) has a minimum marked $K^*$ where the two curves cross.]

Some common criterion for choosing [Obj + Penalty]:

- **AIC** — Akaike Information Criterion
$$[2K - 2\log(L(\theta^*))]$$

- **BIC** — Bayesian Information Criterion
$$[K(\log n) - 2\log(L(\theta^*))]$$
