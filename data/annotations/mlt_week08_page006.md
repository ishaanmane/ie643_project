$$P(y^{test}=1/x^{test}) = \frac{P(x^{test}/y^{test}=1)\cdot P(y^{test}=1)}{P(x^{test})}$$
$$P(y^{test}=0/x^{test}) = \frac{P(x^{test}/y^{test}=0)\cdot P(y^{test}=0)}{P(x^{test})}$$

Now as we just need to compare them, the denominator is irrelevant. We can simply use the numerator to see which has the higher value.

So, $P(x^{test}/y^{test}=1)\cdot P(y^{test}=1) = ?$

$$= P(x^{test}=[f_1\;f_2\;\dots\;f_d]/y_{test}=1)\cdot P(y^{test}=1)$$
$$= \left(\prod_{j=1}^{d}(\hat{p}_j')^{f_j}(1-\hat{p}_j')^{(1-f_j)}\right)\cdot\hat{p}$$

if,
$$\left(\prod_{j=1}^{d}(\hat{p}_j')^{f_j}(1-\hat{p}_j')^{(1-f_j)}\right) > \left(\prod_{j=1}^{d}(\hat{p}_j^0)^{f_j}(1-\hat{p}_j^0)^{(1-f_j)}\right)(1-\hat{p}^0)$$

then $y^{test}=1$, $y^{test}=0$ otherwise

This algorithm is called **NAIVE BAYES ALGORITHM.**
Because coz Bayes Rule
