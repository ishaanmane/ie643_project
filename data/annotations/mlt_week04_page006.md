# Bayesian Estimation

**Goal:** Incorporate "hunch/belief" about the parameters of interest in the estimation process.

**Approach:** Think of the parameter as a "random variable"

Hunch $\rightarrow$ codified using probability distribution over $\theta$. $P(\theta) \rightarrow$ Prior Distribution

We will update our hunch after looking at the data. It could be either correct or wrong.

It can be codified as probability distribution $P(\theta/\text{Data}) \rightarrow$ Posterior Distribution

## Bayes Law

$$P(A/B) = \frac{P(B/A)P(A)}{P(B)}$$

in our case $\begin{cases} A \rightarrow \text{parameter} \\ B \rightarrow \text{Data } \{x_1,\dots,x_n\} \end{cases}$

$$\underbrace{P(\theta/\{x_1,\dots,x_n\})}_{\text{Posterior}} = \frac{\overbrace{P(\{x_1,\dots,x_n\}/\theta)}^{\text{Likelihood}} \; P(\theta)}{\underbrace{P(\{x_1,\dots,x_n\})}_{\text{Evidence}}} \; \text{Prior}$$
