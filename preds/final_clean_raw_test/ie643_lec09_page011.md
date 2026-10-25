$$e(y^i,\hat{y}^i) = \text{KL}(y^i,\hat{y}^i)$$

$\rightarrow$ KL = 0 when $y^i \equiv \hat{y}^i$
$\rightarrow$ KL > 0 when $y^i \neq \hat{y}^i$

**Logistic regression**

$$\min_{\text{weights of NN}} \sum_{i=1}^{N} \text{KL}(y^i,\hat{y}^i)$$

$$\rightarrow \min_{\text{weights}} \sum_{i=1}^{N} C(\hat{y}^i,y^i)$$

$$E[y|x=\vec{x}] \rightarrow \text{Bernoulli r.v.} \rightarrow \text{likelihood}$$