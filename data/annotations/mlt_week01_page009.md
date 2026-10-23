# Representation Learning (3)

What we have done so far:
- Datapoint $x \in \mathbb{R}^d$
- Find a line $w$ for the dataset
- Use a proxy to represent that datapoint on the line $w$: $(x^Tw)w$
- The error $x-(x^Tw)w$ might not be useless but has some "information"

## Possible Algorithm

Input: $\{x_1, x_2, \dots, x_n\} \in \mathbb{R}^d$

$\rightarrow$ Centre the dataset by finding mean ($\mu$) & subtract it from $x_i$
$$\mu = \frac{1}{n}\sum_{i=1}^{n} x_i \qquad x_i = x_i - \mu \; \forall i$$

$\rightarrow$ Find the best line ($w_1$) for minimizing error or maximizing $[w^TCw]$

$\rightarrow$ Replace $x_i$ with the residue $[x_i - (x_i^Tw)w]$

$\rightarrow$ Repeat the steps to obtain $w_2$

## Questions

$\rightarrow$ How to solve $\max_{w, \|w\|^2=1} w^TCw$?

$\rightarrow$ How many times should we repeat the procedure?

$\rightarrow$ Where exactly is "compression" happening?
