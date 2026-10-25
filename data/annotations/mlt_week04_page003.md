# Maximum Likelihood Estimation

## Likelihood

Data: $\{1,0,1,1\}$

[Diagram: A curve of $P(X_1=1,X_2=0,X_3=1,X_4=1)$ over $p \in [0,1]$, peaking near $p=3/4$.]

## Fisher's Principle of Maximum Likelihood

$$L(p; \{x_1,x_2,\dots,x_n\}) = P(x_1,x_2,\dots,x_n; p)$$

parameter $p$; Data $= \{x_1,\dots,x_n\}$; underlying parameter $p$; $x_1=a_1, x_2=a_2,\dots,x_n=a_n$

$$= P(x_1;p)\cdot P(x_2;p) \cdots P(x_n;p) \quad \text{because of independence of data}$$

$$= \prod_{i=1}^{n} p^{x_i}(1-p)^{(1-x_i)}$$

$$\begin{cases} \text{if } x_i=1 \Rightarrow p^1(1-p)^{1-1} = p \\ \text{if } x_i=0 \Rightarrow p^0(1-p)^{1-0} = (1-p) \end{cases}$$

maximum likelihood estimator:
$$\hat{p}_{ML} = \operatorname*{argmax}_p \prod_{i=1}^{n} p^{x_i}(1-p)^{(1-x_i)}$$
