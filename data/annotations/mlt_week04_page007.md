[Note: Evidence "Does not depend..." (on $\theta$)]

## Example:

[Diagram: "Hunch" — a peaked curve over $[0,1]$ centered near 0.9. "Data" $\{0,1,0,0,0,0,0,0,1,0\}$. "Updated Hunch" — a peaked curve centered near 0.27, narrower than the original hunch.]

Data $\rightarrow$ Bernoulli($p$)
Prior $\rightarrow$ Beta Prior

$$f(p;\alpha,\beta) = \frac{p^{\alpha-1}(1-p)^{\beta-1}}{Z} \quad \forall p \in [0,1]$$

[Diagram: Beta distribution density curves over $p \in [0,1]$ for three parameter settings — $\alpha=2,\beta=5$ (green, left-skewed peak), $\alpha=2,\beta=2$ (orange, centered bump), $\alpha=0.5,\beta=0.5$ (blue, U-shaped, peaks at both ends).]

$$P(\theta/\text{Data}) \propto \underbrace{P(\text{Data}/\theta)}_{\text{Likelihood}} \cdot \underbrace{P(\theta)}_{\text{Prior}}$$
$$\underbrace{\hphantom{P(\theta/\text{Data})}}_{\text{Posterior}}$$
