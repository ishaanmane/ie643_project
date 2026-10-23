$$w_3=e^{w_2}$$

due to $=$, it is not convex, as we have to be on the curve.

$$w_3\geq e^{w_2} \quad \text{this is convex, as we can have feasible region on & above curve}$$

**Ex:**
$$\text{min } \sum_{i=1}^{5}x_i$$
$$\sqrt{x_1^2+\ln(1+x_2^2)} \leq e^{\frac{x_2^2}{x_3}}+4x_4+x_5$$
$$1\leq x_i\leq10 \; \forall i$$

Start substituting things out. (closed intervals)

$w_1\in[1,100]$
$w_2\in[e,e^{100}]$
$w_3\in[1,100]$
$w_4\in[2,101]$
$w_5\in[\ln2,\ln(101)]$
$w_6\in[1,100]$

$$w_1=x_1^2, \quad w_2=e^{w_1}, \quad w_3=x_2^2, \quad w_4=(1+w_3), \quad w_5=\ln(w_4)$$
$$w_6=x_1^2, \quad w_7=w_6+w_5, \quad w_8=\sqrt{w_7}, \quad w_8\leq w_2+4x_4+x_5$$

← we use bounds for secants
