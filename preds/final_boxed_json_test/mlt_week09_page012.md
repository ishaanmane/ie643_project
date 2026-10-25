# Logistic Regression

$$P(y=1/x) = \frac{1}{1+e^{-w^Tx}} \quad \text{Dataset: } \{(x_1,y_1),\dots,(x_n,y_n)\}$$

How to find $w$: Maximum Likelihood

$$L(w;\text{Data}) = \prod_{i=1}^{n}(g(w^Tx_i))^{y_i}(1-g(w^Tx_i))^{(1-y_i)}$$

$$\log L(w;\text{Data}) = \sum_{i=1}^{n}y_i\log(g(w^Tx_i))+(1-y_i)\log(1-g(w^Tx_i))$$

$$= \sum_{i=1}^{n}y_i\log\left(\frac{1}{1+e^{-w^Tx_i}}\right)+(1-y_i)\log\left(\frac{e^{-w^Tx_i}}{1+e^{-w^Tx_i}}\right)$$

$$\log L(w) = \sum_{i=1}^{n}[y_i(-w^Tx_i)-\log(1+e^{-w^Tx_i})]$$

**Goal:** $\max_w \sum_{i=1}^{n}(1-y_i)(-w^Tx_i)-\log(1+e^{-w^Tx_i})$

No closed form expression — Can perform gradient descent (ascent)

$$\nabla\log L(w) = [y_i(-x_i)-(\frac{e^{-w^Tx_i}}{1+e^{-w^Tx_i}})(-x_i)] = [-x_i+y_ix_i+x_i\frac{e^{-w^Tx_i}}{1+e^{-w^Tx_i}}]$$