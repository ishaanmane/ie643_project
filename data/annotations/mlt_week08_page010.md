$$\sum_{i=1}^{d}\left[f_i\left(\log\left(\frac{\hat{p}_i'(1-\hat{p}_i^0)}{\hat{p}_i^0(1-\hat{p}_i')}\right)\right) + \log\left(\frac{(1-\hat{p}_i')\hat{p}'}{(1-\hat{p}_i^0)(1-\hat{p}^0)}\right)\right] \geq 0$$

Suppose $x_{test} = [f_1\;f_2\;\dots\;f_d]$

The Decision Function is of the form:
$$w^Tx_{test} + b \geq 0 \quad w\in\mathbb{R}^d$$

$$w_i = \log\left(\frac{\hat{p}_i'(1-\hat{p}_i^0)}{\hat{p}_i^0(1-\hat{p}_i')}\right) \quad \& \quad b = \log\left(\frac{(1-\hat{p}_i')\hat{p}'}{(1-\hat{p}_i^0)(1-\hat{p}^0)}\right)$$

[Diagram: A plane split by a line into two half-spaces labeled $w^Tx>0$ (yellow, shaded) and $w^Tx<0$, with normal vector $w$.]

**Conclusion**

Decision Function is **LINEAR!**
